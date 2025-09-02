## Purpose

Create a small Python script that generates the daily files used by the Daily Status process.

## Files to create (per day)

- Daily status: `yyyy-mm-dd.md`
- Image prompt: `yyyy-mm-dd.image_prompt.md`
- Chat/interview transcript: `yyyy-mm-dd.chat.md`

## Behavior

- Determine today’s date in ISO format `yyyy-mm-dd` (use local time).
- For each of the three target files:
  - If the file already exists, do nothing.
  - If the file does not exist, create it and write a first line with today’s date, e.g. `2025-06-03`.
- All files are Markdown.

## Minimal file contents

Each newly created file should contain a single first line with the date and the title of the file and the day of the week, eg:

```
# 2025-06-03 Daily Status - Wednesday
```

No other boilerplate is required here; section structure is guided by `DailyStatus.process.md`.

## Notes

- Keep the script idempotent so it can be safely re-run.
- Place the script in the repository root. Suggested name: `daily_status_template.py`.
