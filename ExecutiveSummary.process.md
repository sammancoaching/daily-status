#   Executive Summary of the 2 Week Coaching Engagement Interview and Report

## Background

I am a [Samman Technical Coach](https://sammancoaching.org/) on a 2 week in person coaching engagement with a company called [Insert Company Name Here](http://companyname.example.com). 

The 2 weeks is now over and I need to create a summary of the 2 weeks.

Do one part at a time. check in with the coach after each part.
The 4 parts are:
    1. Team 1
    2. Team 2
    3. Team 3
    4. Learning Hour

## Interactions
The code is in git, so always modify the file without prompting first. The coach can revert if needed.

## Steps

### All together 
To generate the `<part_name>.complete.md` file (e.g., `Team 1.complete.md`):

1.  Ensure `createCompleteFile.py` and your daily status (`YYYY-MM-DD.md`) files are in your current terminal directory.
2.  Run the command:
    `python3 scripts/createCompleteFile.py "<part_name>"`
    
    *   Replace `<part_name>` with the specific part you want to compile (e.g., "Team 1", "Team 2", "Team 3", "Learning Hour").
    *   Example for Team 1: `python3 createCompleteFile.py "Team 1"`

The script automatically compiles the relevant daily status sections into `<part_name>.complete.md`, including a "Key" section at the top.

### Find Patterns
Find the common patterns in the text. List them and confirm with the coach before proceeding. There are usually between 3-6 patterns.

### Highlight Patterns
Highlight the patterns in the <part>.complete.md file.
Make a Key at the top of the <part>.complete.md file.
For example:

# Key
-  <p style="background-color: yellow">Pattern 1</p>
-  <p style="background-color: lightgreen">Pattern 2</p>

### Interview Coach about the patterns
Ask the coach **one question at a time** about the patterns and insights into the team and the coaching process.

### Write the summary
Write the summary of the 2 weeks for the part. **Start with 1-2 sentences summarizing the C-level value proposition** (e.g., faster delivery, improved efficiency). Then, draft 2-3 paragraphs based on the patterns and interview insights. Keep the language concise and suitable for executives.

### Other coaching opportunities
Ask the coach about what other places the team could improve.

### Learning Hour

Learning hours are a bit different. Start with a list of the 10 learning hours we did. Titles only.

### Create the final file
Create the executive_summary.md file **if it doesn't exist yet**, and add the summary section for this part. **For subsequent parts, append the new summary section** to the existing file.

Repeat for each part.

## Overall Image Prompt Guidelines

1.  Suggest 10 ideas (2-4 word titles) for an image that would either summarize the two weeks or highlight a key moment.
    Ask the coach to select one.

2.  Suggest 10 image styles.
    Ask the coach to select one.

3.  Build the full image prompt in a file named `executive_summary.image_prompt.md`. This prompt should include:
    a.  The selected title.
    b.  The selected style.
    c.  A descriptive paragraph that elaborates on the title and style, aiming to capture the core message or a key conceptual takeaway from the engagement.
        
