#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
import argparse
import re
from typing import Optional, List

def date_and_weekday(date_arg: Optional[str]):
    if date_arg:
        d = datetime.strptime(date_arg, "%Y-%m-%d").date()
    else:
        d = datetime.now().date()
    return d.isoformat(), d.strftime("%A")

def ensure_file(path: Path, content: str, overwrite: bool) -> bool:
    if path.exists() and not overwrite:
        return False
    path.write_text(content, encoding="utf-8")
    return True

def parse_team_names_arg(raw: Optional[str]):
    if not raw:
        return []
    return [x.strip() for x in raw.split(",") if x.strip()]


def content_for(title: str, date_str: str, weekday: str, team_names: Optional[List[str]]):
    lines = [f"# {date_str} {title} - {weekday}"]
    if title == "Daily Status" and team_names:
        for name in team_names:
            lines.append("")
            lines.append(f"## Team: {name}")
    lines.append("")
    return "\n".join(lines)

def run(base_dir: Path, overwrite: bool = False, date_arg: Optional[str] = None, team_names_arg: Optional[str] = None) -> None:
    date_str, weekday = date_and_weekday(date_arg)
    provided_team_names = parse_team_names_arg(team_names_arg)
    team_names = provided_team_names


    targets = [
        (base_dir / f"{date_str}.md", "Daily Status", team_names),
        (base_dir / f"{date_str}.image_prompt.md", "Image Prompt", None),
        (base_dir / f"{date_str}.chat.md", "Chat/Interview Transcript", None),
    ]

    for path, title, tnames in targets:
        content = content_for(title, date_str, weekday, tnames)
        ensure_file(path, content, overwrite)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--date")
    parser.add_argument("--team-names")
    args = parser.parse_args()
    run(
        Path(__file__).resolve().parent,
        overwrite=args.overwrite,
        date_arg=args.date,
        team_names_arg=args.team_names,
    )
