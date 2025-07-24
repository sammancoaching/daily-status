# Daily Status Interview and Report for only one team

## Background

This process is the same as the one described in [DailyStatus.process.md](DailyStatus.process.md) except that since I am only coaching one team at the moment, you need to produce a status email for that team only.

## Steps

Only do one part at a time. If a part requires multiple questions, ask them one at a time. Wait for the answer before moving on to the next question.

After drafting each section, invite rapid, iterative edits and confirmation from the coach. Collaborative refinement is encouraged to ensure clarity and accuracy.

1. There are 2 parts to each Daily Status. You will do one part at a time:
   1. Learning Hour
   2. Team ensemble
   
2. Read the previous Daily Statuses to get a sense of where things are and to retrieve the actual team names for section headings (e.g., "Team 1: Specific Team Name").
   2.a. If there are none, skip this step and ask for the team's name.
   2.b. At the beginning of the `yyyy-mm-dd.md` file, add a main title header including the day number, weekday, and full date (e.g., `# Daily Status - Day [X] - [Weekday] - yyyy-mm-dd`).

3. For each team/section, ask the following questions, one at a time:
    1. What did you do?
    2. What surprised you?
    3. What went well?
    4. What progress was made?
    5. (If relevant) What challenges or pain points emerged?
4. Distill the important parts. List them and confirm with the coach before proceeding.
5. Distill the big picture value and business value from the parts. List and confirm with the coach before proceeding.
6. Ask about the next steps and current goals. Always list "Next steps" and "Current goal" as bullet points at the end of each team/section.
7. Confirm if there is anything else to add.
8. Write a first draft of the Daily Status for that team/section.
9. Iterate on the draft until it is complete and confirmed. Invite user edits and suggestions until the report accurately reflects the day.
10. Repeat for each team/section, ensuring parallel structure and section headings for all teams (including Learning Hour).
11. Always include a Learning Hour (or equivalent) section, even if brief. Ask about:
    - Session title or theme (e.g., "Learning Hour – Vibe Coding (Part 1)")
    - Format (presentation, workshop, etc.)
    - Attendance/engagement
    - Key takeaways or next steps
    - Links to slides/talks, exercises, process files, or other artifacts if available
    - Screenshots or artifacts if relevant
12. When everything is done, craft a prompt for an image that would either summarize the day or highlight a key moment.
    - Suggest a few ideas (2-4 word titles) and a variety of image styles or formats (e.g., comic, hand-drawn minimal, diagram, infographic, collage).
    - If the initial image prompt isn't satisfactory, encourage requesting a new one with a different style or focus, or ask if the coach has a specific concept in mind and adapt to that.
    - Diagrams are especially recommended when the day's insight is about workflow or process, not just a team moment.
    - Have the user select a preferred title and style/format before building the final image prompt.
    - Build and save the prompt in a file named `yyyy-mm-dd.image_prompt.md`.
13. Create an empty file named `yyyy-mm-dd.chat.md`. The coach will then paste the transcript of the chat/interview process into this file for reference. The transcript should capture not just Q&A, but also the iterative refinement and decision-making process throughout the day.
14. Optionally, add a "General Observations" or "Coach's Note" section at the end for cross-team or overall reflections (e.g., signs of teams internalizing learning). At project milestones (e.g., halfway), always include a brief general observation about overall satisfaction or concerns.
15. Use the format `yyyy-mm-dd.md` for each daily status. When first adding content to this file (e.g., the date header or the first team section), include a standard unsubscribe note at the top if the status will be distributed by email.

## Image Prompt Guidelines

1. Suggest a few ideas (2-4 word titles)
2. Suggest a few image styles.
3. Have the user select a preferred title and style before building the final image prompt.
4. Build the prompt.

## Style Guidelines

- Short and concise. 1-2 paragraphs per team/section.
- Easy to read and scan; email should be readable in under 5 minutes.
- Start new sentences on new lines, so the markdown does not need to wrap.
- Use bullet points or numbered lists for key insights, and bold for emphasis where appropriate.
- Separate major sections (teams, learning hour) with a blank line or horizontal rule (`---`) for readability.
- Start each team/section with "Today, I...", "Today, we...", or "Today, the team..." for parallel structure and natural language.
- Use actual team names in section headings (e.g., "## Team 1: Specific Team Name") for clarity.
- Include personal observations or quotes where relevant (e.g., "As I often say, 'Dissatisfaction is the service I provide.'").
- Add a "Bonus" or "Possible Opportunities" sub-section if relevant.

## File Management

- Daily status: `yyyy-mm-dd.md`
- Image prompt: `yyyy-mm-dd.image_prompt.md`
- Chat/interview transcript: `yyyy-mm-dd.chat.md`
- Add unsubscribe note at the top if distributing by email.
- When creating the `yyyy-mm-dd.md` file, consider including a placeholder for the daily image, such as `![image](./images/yyyy-mm-dd.image.png)`, typically placed after the unsubscribe note and before the first team section.

## Sample Daily Status

read the `2025-06-03_sample.md` file for a sample Daily Status.

## FileName
`date.md` date is in the yyyy-mm-dd format.
