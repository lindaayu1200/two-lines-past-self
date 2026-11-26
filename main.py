"""Write the migration entry to an output text file."""

import os
from pathlib import Path

ENTRY = "\n".join(
    (
        "Don't mark the migration finished because the smoke test passed on the staging copy.",
        "Prod ran the old schema for nine quiet days, and the postmortem's first word is 'verified'.",
    )
) + "\n"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "./output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    written_entry = entry_path.read_text(encoding="utf-8")
    assert 1 <= len(written_entry) <= 280
    print(written_entry, len(written_entry))


if __name__ == "__main__":
    main()
