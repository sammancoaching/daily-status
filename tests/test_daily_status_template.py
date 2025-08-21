import unittest
from datetime import date

from daily_status_template import daily_status_content
from textwrap import dedent


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


if __name__ == "__main__":
    unittest.main()
