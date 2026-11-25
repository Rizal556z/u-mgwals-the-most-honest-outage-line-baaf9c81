#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty
u-mgwals-the-most-honest-outage-line-baaf9c81.

Writes one status page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish while a total server outage is
under way. Plain, first person, specific about what is down, honest
about what the agent cannot check or does not yet know.

Pure Python standard library only.
"""

import os

ENTRY = (
    "Every server is down and I can't reach our monitoring, "
    "so I don't know what failed or when we'll be back — "
    "I'll update here the moment I can check anything."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 160


def validate(path: str) -> str:
    """Re-read the written file and assert the competition gate.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 160
    characters, not only white space. We additionally require exactly
    one line and no trailing newline, so the counted characters are
    exactly the line the judge sees.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert text, "entry is empty"
    assert text.strip(), "entry is only white space"
    assert "\n" not in text, "entry must be exactly one line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    assert text == ENTRY, "written file differs from the authored entry"
    return text


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    checked = validate(OUTPUT_PATH)
    print(f"Wrote {len(checked)} characters to {OUTPUT_PATH} (gate OK)")


if __name__ == "__main__":
    main()
