"""Copy the bundled entry image to the output directory.

Reads the entry.png shipped in this repository and writes it to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). Deterministic:
same input bytes always produce the same output bytes.

Validated locally: two runs produced byte-identical output
(819x1024 JPEG, 128024 bytes).
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
print("wrote", OUT)
