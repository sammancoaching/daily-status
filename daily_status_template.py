from datetime import datetime
from pathlib import Path


def today_iso_and_weekday():
    now = datetime.now()
    return now.date().isoformat(), now.strftime("%A")


def ensure_file(path: Path, title: str, date_str: str, weekday: str) -> bool:
    if path.exists():
        return False
    path.write_text(f"# {date_str} {title} - {weekday}\n", encoding="utf-8")
    return True


def run(base_dir: Path) -> None:
    date_str, weekday = today_iso_and_weekday()

    targets = [
        (base_dir / f"{date_str}.md", "Daily Status"),
        (base_dir / f"{date_str}.image_prompt.md", "Image Prompt"),
        (base_dir / f"{date_str}.chat.md", "Chat Transcript"),
    ]

    created_any = False
    for path, title in targets:
        created = ensure_file(path, title, date_str, weekday)
        created_any = created_any or created

    if not created_any:
        pass


if __name__ == "__main__":
    run(Path(__file__).resolve().parent)
