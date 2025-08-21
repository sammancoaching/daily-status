import unittest
from datetime import date

from daily_status_template import (
    daily_status_content,
    create_or_overwrite_with_content,
    create_files,
    image_prompt_content,
    chat_transcript_content,
)
from textwrap import dedent
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace


class DailyStatusContentTests(unittest.TestCase):
    def test_no_teams_uses_placeholder_section(self):
        d = date(2025, 8, 21)
        out = daily_status_content(d, [])
        expected = dedent(
            """\
            # Daily Status - Thursday - 2025-08-21
            If you would like to stop receiving these updates, reply with 'unsubscribe'.
            
            ![Image](2025-08-21_sample.png)
            
            ## <team name>: TODO - heading
            TODO - write daily status here
            
            ## Big-picture value:
            TODO - write big picture value here
            
            """
        )
        self.assertEqual(expected, out)

    def test_multiple_teams_rendered_separately(self):
        d = date(2025, 8, 21)
        teams = ["Rocket", "Sales"]
        out = daily_status_content(d, teams)
        expected = dedent(
            """\
            # Daily Status - Thursday - 2025-08-21
            If you would like to stop receiving these updates, reply with 'unsubscribe'.
            
            ![Image](2025-08-21_sample.png)
            
            ## Rocket: TODO - heading
            TODO - write daily status here
            
            ## Sales: TODO - heading
            TODO - write daily status here
            
            ## Big-picture value:
            TODO - write big picture value here
            
            """
        )
        self.assertEqual(expected, out)


class EnsureWithContentTests(unittest.TestCase):
    def test_creates_new_file_and_records_created(self):
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "file.md"
            result = create_or_overwrite_with_content(p, "hello", force=False)
            self.assertTrue(result)
            self.assertTrue(p.exists())
            self.assertEqual(p.read_text(encoding="utf-8"), "hello")

    def test_skips_non_empty_file_without_force(self):
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "file.md"
            p.write_text("original", encoding="utf-8")
            result = create_or_overwrite_with_content(p, "new", force=False)
            self.assertFalse(result)
            self.assertEqual(p.read_text(encoding="utf-8"), "original")

    def test_overwrites_when_force_true(self):
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "file.md"
            p.write_text("original", encoding="utf-8")
            result = create_or_overwrite_with_content(p, "forced", force=True)
            self.assertTrue(result)
            self.assertEqual(p.read_text(encoding="utf-8"), "forced")

    def test_overwrites_empty_file_treated_as_created(self):
        with TemporaryDirectory() as tmp:
            p = Path(tmp) / "file.md"
            p.write_text("", encoding="utf-8")
            result = create_or_overwrite_with_content(p, "filled", force=False)
            self.assertTrue(result)
            self.assertEqual(p.read_text(encoding="utf-8"), "filled")


class CreateFilesTests(unittest.TestCase):
    def test_creates_all_three_files_when_absent(self):
        d = date(2025, 8, 21)
        teams = ["Rocket", "Sales"]
        with TemporaryDirectory() as tmp:
            project_dir = Path(tmp)
            args = SimpleNamespace(force=False)

            created, skipped = create_files(args, project_dir, d, teams)

            base = "2025-08-21"
            expected_paths = {
                project_dir / f"{base}.md",
                project_dir / f"{base}.image_prompt.md",
                project_dir / f"{base}.chat.md",
            }

            self.assertEqual(set(created), expected_paths)
            self.assertEqual(skipped, [])


    def test_skips_existing_files_without_force(self):
        d = date(2025, 8, 21)
        teams = ["Rocket"]
        with TemporaryDirectory() as tmp:
            project_dir = Path(tmp)
            base = "2025-08-21"
            daily_p = project_dir / f"{base}.md"
            img_p = project_dir / f"{base}.image_prompt.md"
            chat_p = project_dir / f"{base}.chat.md"

            daily_p.write_text("old daily", encoding="utf-8")
            img_p.write_text("old image", encoding="utf-8")
            chat_p.write_text("old chat", encoding="utf-8")

            args = SimpleNamespace(force=False)
            created, skipped = create_files(args, project_dir, d, teams)

            self.assertEqual(created, [])
            self.assertEqual(set(skipped), {daily_p, img_p, chat_p})

            self.assertEqual(daily_p.read_text(encoding="utf-8"), "old daily")
            self.assertEqual(img_p.read_text(encoding="utf-8"), "old image")
            self.assertEqual(chat_p.read_text(encoding="utf-8"), "old chat")


if __name__ == "__main__":
    unittest.main()
