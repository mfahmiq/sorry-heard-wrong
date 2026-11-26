"""Write the smart-speaker apology entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a fixed string: the funniest one-line apology a smart
speaker gives its owner after mishearing them. No network, no file
reads, no secrets -- the program's only job is to deliver the entry
byte-identically.
"""

import os

ENTRY = "Sorry, I heard 'goodnight' as 'good fight' and I have taken your side. He started it."

# The competition wants a single line (the entry is 85 characters).
MAX_ENTRY_CHARS = 200


def validate_entry(text: str) -> str:
    """Check the entry is a well-formed one-line apology; return it unchanged.

    Guards against accidental edits to the fixed string: it must be one
    line, end with a period, and keep the misheard pair that makes the
    joke work ("goodnight" heard as "good fight").
    """
    if not text:
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_ENTRY_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_ENTRY_CHARS} cap")
    if not text.endswith("."):
        raise ValueError("entry must end with a period")
    if "goodnight" not in text or "good fight" not in text:
        raise ValueError("entry lost the 'goodnight' / 'good fight' mishearing")
    return text


def main() -> None:
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Verify the file on disk is byte-identical to the entry we validated.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != entry:
        raise ValueError("entry.txt on disk does not match the validated entry")
    print(entry)


if __name__ == "__main__":
    main()
