#!/usr/bin/env python3
import argparse
from datetime import date, datetime
from pathlib import Path
from textwrap import dedent


def parse_team_names(arg):
    if not arg:
        return []
    parts = [p.strip() for p in arg.split(",")]
    return [p for p in parts if p]


def daily_status_content(d, teams):
    date_str = d.strftime("%Y-%m-%d")
    weekday = d.strftime("%A")
    header = dedent(
        f"""\
        # Daily Status - {weekday} - {date_str}
        If you would like to stop receiving these updates, reply with 'unsubscribe'.
    
        ![Image]({date_str}_sample.png)

        """)

    team_section = dedent(
        """\
        ## {team_name}: TODO - heading
        TODO - write daily status here

        """)

    footer = dedent(
        """\
        ## Big-picture value:
        TODO - write big picture value here

        """)

    if teams:
        team_sections = ""
        for team_name in teams:
            team_sections += team_section.format(team_name=team_name)
    else:
        team_sections = team_section.format(team_name="<team name>")

    return header + team_sections + footer


def image_prompt_content(d):
    date_str = d.strftime("%Y-%m-%d")
    return dedent(
        f"""\
        # Image Prompt - {date_str}

        Describe the image concept for today.

        """)


def chat_transcript_content(d):
    date_str = d.strftime("%Y-%m-%d")
    return dedent(
        f"""\
        # Chat / Interview Transcript - {date_str}

        Paste or write the transcript here.

        """)


def create_or_overwrite_with_content(path: Path, content: str, force: bool = False):
    exists = path.exists()
    is_empty = exists and path.stat().st_size == 0
    should_write = (not exists) or force or is_empty

    if should_write:
        path.write_text(content, encoding="utf-8")
        return True
    else:
        return False


def create_files(args, project_dir, target_date, teams):
    base = target_date.strftime("%Y-%m-%d")

    filepaths_and_content = [
        ((project_dir / f"{base}.md"), daily_status_content(target_date, teams)),
        ((project_dir / f"{base}.image_prompt.md"), image_prompt_content(target_date)),
        ((project_dir / f"{base}.chat.md"), chat_transcript_content(target_date)),
    ]

    created = []
    skipped = []

    for filepath, content in filepaths_and_content:
        if create_or_overwrite_with_content(filepath, content, force=args.force):
            created.append(filepath)
        else:
            skipped.append(filepath)

    return created, skipped


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
    teams = parse_team_names(args.team_names)

    created, skipped = create_files(args, project_dir, target_date, teams)

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
