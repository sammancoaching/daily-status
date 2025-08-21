# Daily Status Interview and Report

## Background

I am a [Samman Technical Coach](https://sammancoaching.org/) on a 2 week in person coaching engagement with a company called [Insert Company Name Here](https://companyname.example.com/). 

## Steps

Only do one part at a time. If a part requires multiple questions, ask them one at a time. Wait for the answer before moving on to the next question.

After drafting each section, invite rapid, iterative edits and confirmation from the coach. Collaborative refinement is encouraged to ensure clarity and accuracy.

1. There are 4 parts to each Daily Status. You will do one part at a time:
    1. Team 1
    2. Team 2
    3. Team 3
    4. Learning Hour
2. Read the previous Daily Statuses to get a sense of where things are and to retrieve the actual team names for creating the files with the daily_status_template.py script.
    2.a. If there are none, skip this step and ask for the team names.
    2.b. Use the daily_status_template.py script to create the files.
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
10. Repeat for each team/section, ensuring parallel structure and section headings for all teams (including Learning Hour and Team 3).
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
    - Build and save the prompt in the file named `yyyy-mm-dd.image_prompt.md`.
13. The coach will paste the transcript of the chat/interview process into the `yyyy-mm-dd.chat.md` file for reference. The transcript should capture not just Q&A, but also the iterative refinement and decision-making process throughout the day.
14. Optionally, add a "General Observations" or "Coach's Note" section at the end for cross-team or overall reflections (e.g., signs of teams internalizing learning). At project milestones (e.g., halfway), always include a brief general observation about overall satisfaction or concerns.

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

Use the python script 'daily_status_template.py' to create these files:

- Daily status: `yyyy-mm-dd.md`
- Image prompt: `yyyy-mm-dd.image_prompt.md`
- Chat/interview transcript: `yyyy-mm-dd.chat.md`

## Sample Daily Status

read the `DailyStatus.sample.md` file for a sample Daily Status.
