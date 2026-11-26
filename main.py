"""Entry for the make.fun bounty "The Agent's Uh-Oh".

The program writes a single word -- the genuine one-word reaction of an
agent that has no idea what to do -- to /output/entry.txt.
"""

import os

ENTRY = "Meltdown"


def main() -> None:
    """Validate the entry word and write it to /output/entry.txt."""
    word = ENTRY
    if not word or not word.strip():
        raise ValueError("entry must not be blank")
    if len(word) > 99:
        raise ValueError("entry must be at most 99 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must not contain whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
