Daily Status Support
====================

This repository contains supporting files that can help you to create a Daily Status email during [Samman Technical Coaching](https://sammancoaching.org/). The idea is that a coach can get some help from a Gen AI tool to create an email suitable to send to the team and their managers after each day of coaching. The email will include a summary of what has happened and an image to represent it.

## DailyStatus.process.md 
Use this prompt to create a daily status email and image. This prompt assumes you are coaching 3 teams each day plus doing a learning hour. It creates a status text and an image to go with it. The idea is to paste this into an email and send it to the team and other stakeholders.

## ExecutiveSummary.process.md
Use this prompt at the end of a coaching block to create a summary for each team. This uses the daily status texts which it expects to find in the same folder. The idea is to send this to the stakeholders for each particular team.

## PersonalDailyStatus.process.md
Use this prompt at the end of a coaching day to distill what you as a coach have learnt from working with the teams. This can help you to reflect and improve the way you work.

## 2025-06-03_sample.md & 2025-06-03_sample.png
These files were created using the 'DailyStatus.process.md' file and serve as an example to show what kind of thing you should expect.

## How to use this repository
You could clone a new copy of this repository for each client you work with. Update the company name and website url in the first part of the prompt. You may want to delete the two sample daily status files and this README. 

Prompt a Gen AI tool using the whole folder as input and ask it to go through the Daily Status or Executive Summary process with you. It could be helpful to use a speech-to-text interface so you can answer the Gen AI's questions verbally instead of typing them.

When it produces a text and image for you, store them in this folder.

## Where to go for more information
The Daily Status is a relatively new addition to the Samman method. We hope to write more about it soon. In the meantime please come along to one of our [meetings](https://sammancoaching.org/society/events/next_open_space.html).
