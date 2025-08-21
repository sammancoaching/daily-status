#!/usr/bin/env python3
import argparse
from datetime import date, datetime
from pathlib import Path


def build_filenames(d):
    base = d.strftime("%Y-%m-%d")
    return [
        f"{base}.md",
        f"{base}.image_prompt.md",
        f"{base}.chat.md",
    ]


def parse_team_names(arg):
    if not arg:
        return []
    parts = [p.strip() for p in arg.split(",")]
    return [p for p in parts if p]


def daily_status_content(d, teams):
    date_str = d.strftime("%Y-%m-%d")
    weekday = d.strftime("%A")
    header = f"""# Daily Status - {weekday} - {date_str}
If you would like to stop receiving these updates, reply with 'unsubscribe'.


![Image]({date_str}_sample.png)

"""

    if teams:
        team_sections = ""
        for t in teams:
            team_sections += f"""## {t}: TODO - heading
TODO - write daily status here

"""
    else:
        team_sections = """## <team name>: TODO - heading
TODO - write daily status here

"""

    footer = """## Big-picture value:
TODO - write big picture value here

"""

    return header + team_sections + footer


def image_prompt_content(d):
    date_str = d.strftime("%Y-%m-%d")
    return f"""# Image Prompt - {date_str}

Describe the image concept for today.

"""


def chat_transcript_content(d):
    date_str = d.strftime("%Y-%m-%d")
    return f"""# Chat / Interview Transcript - {date_str}

Paste or write the transcript here.

"""


def ensure_with_content(path: Path, content: str, created, skipped, force: bool = False):
    if path.exists():
        if force or path.stat().st_size == 0:
            path.write_text(content, encoding="utf-8")
            created.append(path)
        else:
            skipped.append(path)
    else:
        path.write_text(content, encoding="utf-8")
        created.append(path)


def main():
    ap = argparse.ArgumentParser(description="Create daily status files with templates")
    ap.add_argument(
        "--team-names",
        dest="team_names",
        default="",
        help="Comma-separated list of team names to include in the daily status file",
    )
    ap.add_argument(
        "--date",
        dest="date_str",
        default="",
        help="Date in YYYY-MM-DD format. Defaults to today.",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite files if they already exist",
    )
    args = ap.parse_args()

    if args.date_str:
        try:
            target_date = datetime.strptime(args.date_str, "%Y-%m-%d").date()
        except ValueError:
            raise SystemExit("--date must be in YYYY-MM-DD format")
    else:
        target_date = date.today()
    project_dir = Path(__file__).resolve().parent
    filenames = build_filenames(target_date)

    teams = parse_team_names(args.team_names)

    created = []
    skipped = []

    daily_path = project_dir / filenames[0]
    image_prompt_path = project_dir / filenames[1]
    chat_path = project_dir / filenames[2]

    ensure_with_content(daily_path, daily_status_content(target_date, teams), created, skipped, force=args.force)
    ensure_with_content(image_prompt_path, image_prompt_content(target_date), created, skipped, force=args.force)
    ensure_with_content(chat_path, chat_transcript_content(target_date), created, skipped, force=args.force)

    if created:
        print("Written:")
        for p in created:
            print(f"  {p.relative_to(project_dir)}")
    if skipped:
        print("Skipped (already had content):")
        for p in skipped:
            print(f"  {p.relative_to(project_dir)}")


if __name__ == "__main__":
    main()
