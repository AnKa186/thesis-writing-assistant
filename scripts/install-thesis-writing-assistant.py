#!/usr/bin/env python3
"""Install only the thesis skill into one local Claude Code project."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile


SKILL_NAME = "thesis-writing-assistant"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path,
                        help="Existing local thesis project directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show the installation target without writing")
    parser.add_argument("--update", action="store_true",
                        help="Back up an existing installation before replacing it")
    args = parser.parse_args()

    project = args.project.expanduser().resolve()
    source = Path(__file__).resolve().parent.parent / "skills" / SKILL_NAME
    destination = project / ".claude" / "skills" / SKILL_NAME
    if not project.is_dir():
        parser.error(f"Project directory does not exist: {project}")
    if not (source / "SKILL.md").is_file():
        parser.error(f"Skill source is missing: {source}")
    for directory in (destination.parent.parent, destination.parent, destination):
        if directory.is_symlink():
            parser.error(f"Installation path is a symlink: {directory}")
    if destination.exists():
        if not destination.is_dir():
            parser.error(f"Installation target is not a directory: {destination}")
        if not args.update:
            parser.error("Skill is already installed; use --update to back it up and replace it")
    print(f"Source: {source}")
    print(f"Target: {destination}")
    if args.dry_run:
        print("Dry run: no files written")
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    backup = None
    with tempfile.TemporaryDirectory(prefix=".thesis-install-", dir=destination.parent) as tmp:
        staged = Path(tmp) / SKILL_NAME
        shutil.copytree(source, staged)
        if destination.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = project / ".claude" / "skill-backups" / SKILL_NAME / stamp
            backup.parent.mkdir(parents=True, exist_ok=True)
            destination.rename(backup)
        try:
            staged.rename(destination)
        except OSError:
            if backup is not None:
                backup.rename(destination)
            raise
    if backup is not None:
        print(f"Previous installation backed up to: {backup}")
    print(f"Installed /{SKILL_NAME}. Open Claude Code in {project} to use it.")


if __name__ == "__main__":
    main()
