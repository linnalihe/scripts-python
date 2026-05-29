# rename-media-files

Renames image and video files to a consistent format:

```
YYYY-MM-<img|vid>-<camera-slug>-<album>-<original-filename>.<ext>
```

Example: `2026-05-img-appleiphone15pro-eurotrip2026-DSC_0042.jpg`

Date and camera are read automatically from file metadata — EXIF (via Pillow) for standard images, exiftool for HEIC and ARW, and ffprobe for videos. If metadata is missing, date falls back to the file modification date and camera falls back to `unknown`. If no album is provided, it defaults to `albumnone`.

Re-running the script on already-renamed files will re-rename them cleanly — it strips the existing prefix and uses the original filename as the base.

---

## Requirements

Before running the script, you need to install three tools and one Python library:

| Requirement | Used for |
|-------------|----------|
| Python 3.8+ | Running the script |
| [Pillow](https://pillow.readthedocs.io/) | Reading EXIF from standard images (JPG, PNG, etc.) |
| [FFmpeg](https://ffmpeg.org/) (includes ffprobe) | Reading metadata from video files |
| [exiftool](https://exiftool.org/) | Reading metadata from HEIC and ARW files |

---

## Setup

Follow these steps once before running the script for the first time.

### Step 1 — Install FFmpeg

FFmpeg includes `ffprobe`, which the script uses to read video metadata.

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu / Debian:**
```bash
sudo apt install ffmpeg
```

### Step 2 — Install exiftool

exiftool is used to read metadata from HEIC and ARW files.

**macOS:**
```bash
brew install exiftool
```

**Ubuntu / Debian:**
```bash
sudo apt install libimage-exiftool-perl
```

### Step 3 — Create a Python virtual environment

Run this once from inside the `rename-media-files` folder:

```bash
python3 -m venv .venv
```

### Step 4 — Activate the virtual environment

Run this each time you open a new terminal before using the script:

**macOS / Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

You should see `(.venv)` appear in your terminal prompt when it is active.

### Step 5 — Install Python dependencies

With the virtual environment active, run:

```bash
pip install Pillow
```

---

## Running the script

### Step 1 — Activate the virtual environment (if not already active)

```bash
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
```

### Step 2 — Run the script

```bash
python main.py
```

### Step 3 — Answer the prompts

The script will ask three questions before processing any files:

1. **Folder path** — Type the path to the folder containing your files, then press Enter. Press Enter without typing anything to use the current directory.

2. **Album name** — Type a label for this batch of files (e.g. `Euro Trip 2026`), then press Enter. Press Enter without typing anything to use `albumnone`.

3. **Dry run?** — Press Enter (or type `Y`) to preview what the files would be renamed to without making any changes. Type `n` and press Enter to rename for real.

### Tips

- Run with dry run first to check the output looks correct before committing to the rename.
- If you want to rename the files again with a different album name, just run the script again — it will detect the existing prefix and re-rename correctly.

---

## Supported formats

| Type       | Extensions |
|------------|------------|
| Images     | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.tiff` `.webp` |
| RAW / HEIC | `.heic` `.arw` |
| Videos     | `.mp4` `.mov` `.avi` `.mkv` `.wmv` `.flv` `.m4v` |
