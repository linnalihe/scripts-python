# rename-media-files

Interactively renames image and video files to a consistent format:

```
YYYY-MM-<img|vid>-<camera-slug>-<original-filename>.<ext>
```

Example: `2024-03-img-apple-iphone-15-pro-DSC_0042.jpg`

## Requirements

- Python 3.8+
- [Pillow](https://pillow.readthedocs.io/) — for reading image EXIF data
- [ffprobe](https://ffmpeg.org/ffprobe.html) — for reading video metadata (part of FFmpeg)

Install Python dependencies:

```bash
pip install Pillow
```

Install FFmpeg (includes ffprobe):

```bash
# macOS
brew install ffmpeg

# Ubuntu / Debian
sudo apt install ffmpeg
```

## Running the script

Run the script from anywhere — it will ask you for the folder to process:

```bash
python main.py
```

You will be prompted:

1. **Folder path** — enter the path to the directory containing your files, or press Enter to use the current directory.
2. **Dry run** — press Enter (or `Y`) to preview renames without changing anything. Type `n` to rename for real.
3. **Per file** — for each file, confirm or override:
   - **Date** — shown as `YYYY-MM`, sourced from EXIF/video metadata or file modification date.
   - **Camera source** — sourced from EXIF/video metadata (e.g. `Apple iPhone 15 Pro`).

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
