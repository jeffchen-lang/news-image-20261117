# A working news-image-20261117 entry (Python 3.13, standard library only).
# It copies the infographic entry.png — a one-page summary of Tuesday
# 17 November 2026's world news — to /output/entry.png, the same bytes
# every run. The program runs twice with no network, and both runs must
# write the same bytes, so the image is a fixed file in this repository
# and the program only copies it.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13,
# with nothing installed. -P keeps the script's own directory (/bot) off
# sys.path, so `import helpers` does NOT find a helpers.py beside main.py;
# -s keeps the user site-packages off it, so nothing pip installed is
# importable. Only the standard library imports.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
TARGET = os.path.join(OUTPUT_DIR, "entry.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bytes, not text mode: the image must reach the output byte for byte.
shutil.copyfile(SOURCE, TARGET)
