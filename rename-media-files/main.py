import os
import re
import json
import subprocess
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".m4v"}
TARGET_EXTS = IMAGE_EXTS | VIDEO_EXTS


def get_exif_data(filepath):
    """Return dict of relevant EXIF fields, or {}."""
    try:
        with Image.open(filepath) as img:
            exif = img._getexif()
        if not exif:
            return {}
        return {TAGS.get(tag, tag): val for tag, val in exif.items()}
    except Exception:
        return {}


def get_image_date(exif):
    for field in ("DateTimeOriginal", "DateTime", "DateTimeDigitized"):
        val = exif.get(field)
        if val:
            try:
                return datetime.strptime(val, "%Y:%m:%d %H:%M:%S")
            except ValueError:
                pass
    return None


def get_image_camera(exif):
    make = exif.get("Make", "").strip()
    model = exif.get("Model", "").strip()
    # Avoid redundancy like "Apple Apple iPhone 15"
    if make and model.lower().startswith(make.lower()):
        return model
    return f"{make} {model}".strip() or None


def get_video_metadata(filepath):
    """Use ffprobe to extract date and camera source from video."""
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "quiet",
                "-print_format", "json",
                "-show_format", "-show_streams",
                filepath
            ],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        tags = data.get("format", {}).get("tags", {})

        # Normalise keys to lowercase for consistent lookup
        tags = {k.lower(): v for k, v in tags.items()}

        # Date: try common tag names
        date_str = (
            tags.get("com.apple.quicktime.creationdate") or
            tags.get("creation_time") or
            tags.get("date")
        )
        dt = None
        if date_str:
            for fmt, n in [("%Y-%m-%dT%H:%M:%S", 19), ("%Y-%m-%d %H:%M:%S", 19), ("%Y-%m-%d", 10)]:
                try:
                    dt = datetime.strptime(date_str[:n], fmt)
                    break
                except ValueError:
                    pass

        # Camera: try Apple QuickTime tags first, then generic
        make = (
            tags.get("com.apple.quicktime.make") or
            tags.get("make") or ""
        ).strip()
        model = (
            tags.get("com.apple.quicktime.model") or
            tags.get("model") or ""
        ).strip()

        if make and model.lower().startswith(make.lower()):
            camera = model
        else:
            camera = f"{make} {model}".strip() or None

        return dt, camera

    except FileNotFoundError:
        return None, None
    except (json.JSONDecodeError, Exception) as e:
        raise RuntimeError(f"ffprobe failed: {e}") from e


def sanitize(text):
    """Lowercase and strip all non-alphanumeric characters. Returns 'unknown' if result is empty."""
    text = text.lower()
    return re.sub(r"[^a-z0-9]+", "", text) or "unknown"


def get_default_date(filepath, ext, exif, video_date):
    if ext in IMAGE_EXTS:
        return get_image_date(exif) or datetime.fromtimestamp(os.path.getmtime(filepath))
    return video_date or datetime.fromtimestamp(os.path.getmtime(filepath))


# --- Main ---
folder = input("Folder path (or Enter for current dir): ").strip() or "."
if not os.path.isdir(folder):
    print(f"Error: '{folder}' is not a valid directory.")
    exit(1)
album_raw = input("Album name (or Enter to skip): ").strip()
album_slug = sanitize(album_raw) if album_raw else "albumnone"
dry_run = input("Dry run? (Y/n): ").strip().lower() != "n"

files = sorted(
    f for f in os.listdir(folder)
    if os.path.splitext(f)[1].lower() in TARGET_EXTS
)

if not files:
    print("No image/video files found.")
    exit()

print(f"\nFound {len(files)} file(s).\n")

for filename in files:
    name, ext = os.path.splitext(filename)
    ext_lower = ext.lower()
    filepath = os.path.join(folder, filename)
    filetype = "img" if ext_lower in IMAGE_EXTS else "vid"

    # Skip already-renamed files
    if re.match(r"^\d{4}-\d{2}-(img|vid)-[a-z0-9]+-[a-z0-9]+-", filename):
        print(f"[SKIP] {filename}  (already renamed)\n")
        continue

    print(f"[FILE] {filename}")

    # Gather metadata
    if filetype == "img":
        exif = get_exif_data(filepath)
        default_dt = get_default_date(filepath, ext_lower, exif, None)
        default_camera = get_image_camera(exif)
    else:
        try:
            video_dt, default_camera = get_video_metadata(filepath)
        except RuntimeError as e:
            print(f"  ⚠️  Skipping — {e}\n")
            continue
        default_dt = get_default_date(filepath, ext_lower, {}, video_dt)

    year_month = default_dt.strftime("%Y-%m")
    camera_slug = sanitize(default_camera or "unknown")

    base_name = f"{year_month}-{filetype}-{camera_slug}-{album_slug}-{name}"
    new_name = f"{base_name}{ext}"
    new_path = os.path.join(folder, new_name)
    counter = 1
    while os.path.exists(new_path):
        new_name = f"{base_name}-{counter}{ext}"
        new_path = os.path.join(folder, new_name)
        counter += 1

    if dry_run:
        print(f"  → DRY RUN: {filename}\n         →  {new_name}\n")
    else:
        os.rename(filepath, new_path)
        print(f"  → RENAMED: {filename}\n        →  {new_name}\n")

print("Done!" + (" (dry run — no files changed)" if dry_run else ""))