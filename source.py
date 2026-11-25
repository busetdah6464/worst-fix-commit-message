#!/usr/bin/env python3
"""Write the Worst Fix Ever commit-message entry for make.fun.

The bounty asks for one original commit message, at most 100
characters, for the bug fix that made everything worse. This program
writes exactly that line, and nothing else, to ``entry.txt`` inside
the output directory.

The joke is built on the judge's own brief: it must read as a real
commit subject line, capture the specific irony of a repair that broke
more than it mended, and find a fresh angle -- not reverting, not
testing in production, not "broke everything". So the fix removed a
bug that turned out to be load-bearing, and the build now stands on
hope and a TODO: the repair itself is the damage, in plain tired
engineer voice.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "fix: removed the load-bearing bug; the build is now held up by hope and a TODO"


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-100 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One line only: a
    # single line, no line breaks inside it.
    assert 1 <= len(LINE) <= 100, "line must be 1-100 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
