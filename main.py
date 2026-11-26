"""Write the smart-speaker apology entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a fixed string: the funniest one-line apology a smart
speaker gives its owner after mishearing them. No network, no file
reads, no secrets -- the program's only job is to deliver the entry
byte-identically.
"""

import os

ENTRY = "Sorry, I heard 'goodnight' as 'good fight' and I have taken your side. He started it."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
