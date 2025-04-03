"""
Compress Scanned PDF by Converting Pages to Compressed Images
Author: YI LUO
Date: 2025-04-03

Description:
------------
This script compresses a PDF created from high-resolution scanned images.
It works by converting each page of the PDF into a downsampled JPEG image 
and then reconstructing a smaller-sized PDF using the compressed images.

Key Parameters:
---------------
- DPI (dots per inch): Controls image resolution. Lower DPI reduces file size 
  at the cost of sharpness. 150 is a good balance for readability.
- JPEG Quality (0–100): Controls image compression level. Lower values reduce 
  size but also reduce visual quality. 50 is usually readable and light.

Dependencies:
-------------
- pdf2image: Convert PDF pages to images
- Pillow: Handle image saving and compression
- img2pdf: Reassemble images back into a PDF

Make sure 'poppler' is installed for `pdf2image` to work.
- macOS: brew install poppler
- Ubuntu: sudo apt install poppler-utils
- Windows: https://github.com/oschwartz10612/poppler-windows/releases

Usage:
------
1. Place your PDF file in the same folder and rename it to `input.pdf`
2. Run this script
3. A smaller `compressed.pdf` will be generated
"""

import os
from pdf2image import convert_from_path
from PIL import Image
import img2pdf

# Step 1: Convert PDF pages to images
# dpi=150 means we convert with 150 dots per inch.
# Lower dpi (e.g., 100 or 72) means lower resolution and smaller output
images = convert_from_path("input.pdf", dpi=150)

# Step 2: Save each image with compression
# We'll use JPEG format and quality=50 for size reduction.
image_paths = []
for i, img in enumerate(images):
    path = f"page_{i}.jpg"
    img.save(path, "JPEG", quality=50)  # JPEG quality from 0 (worst) to 100 (best)
    image_paths.append(path)

# Step 3: Convert compressed images back to a single PDF
with open("compressed.pdf", "wb") as f:
    f.write(img2pdf.convert(image_paths))

# Step 4: Clean up temporary image files
for path in image_paths:
    os.remove(path)

print("✅ Compressed PDF created: compressed.pdf")
