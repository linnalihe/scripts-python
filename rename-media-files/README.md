# rename-media-files

Renames image and video files to a consistent format:

```
YYYY-MM-<img|vid>-<camera-slug>-<album>-<original-filename>.<ext>
```

Example: `2026-05-img-appleiphone15pro-eurotrip2026-DSC_0042.jpg`

Date and camera are read automatically from file metadata (EXIF for images, ffprobe for videos), falling back to file modification date and `unknown` respectively. If no album is provided, it defaults to `albumnone`.

## Requirements

- Python 3.8+
- [Pillow](https://pillow.readthedocs.io/) — for reading image EXIF data
- [ffprobe](https://ffmpeg.org/ffprobe.html) — for reading video metadata (part of FFmpeg)

## Setup

**1. Install FFmpeg** (includes ffprobe):

```bash
# macOS
brew install ffmpeg

# Ubuntu / Debian
sudo apt install ffmpeg
```

**2. Create and activate a virtual environment:**

```bash
# Create the environment (once)
python3 -m venv .venv

# Activate it (every new terminal session)
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
```

**3. Install Python dependencies:**

```bash
pip install Pillow
```

## Running the script

Run the script from anywhere — it will ask you for the folder to process:

```bash
python main.py
```

You will be prompted three times before any files are processed:

1. **Folder path** — path to the directory containing your files, or press Enter to use the current directory.
2. **Album name** — a label for this batch (e.g. `Euro Trip 2026`). Press Enter to use `albumnone`.
3. **Dry run** — press Enter (or `Y`) to preview renames without changing anything. Type `n` to rename for real.

Files whose names already match the `YYYY-MM-(img|vid)-` pattern are skipped automatically.

## Running directly inside the target directory

```bash
cd /path/to/your/photos
python /path/to/rename-media-files/main.py
# When prompted for folder path, just press Enter
```

## Supported formats

| Type   | Extensions |
|--------|-----------|
| Images | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.tiff` `.webp` `.heic` |
| Videos | `.mp4` `.mov` `.avi` `.mkv` `.wmv` `.flv` `.m4v` |
