# Pitch
Tutoring at a Glance

tty tutoring information taken from current tutoring Google Spreadsheet. Made by ACM for ACM
## Goals
- Fill the whole screen, but keep it neat.
- SMALL animations like scrolling text for panels not being big enough
## Not Goals
- crowded/cluttered
- distracting
## Features
### p0:
- Basic screens
  - Name of tutor, what times they are available
  - Name of tutor, what classes they can tutor for
- Scalable framework to make other priorities available
### p1:
- Advanced screens:
  - Times that speicific classes are available
  - Tutors that are available on the current day
- UI elements like current time, date, who's in the ACM office now, check Discord for updates
- Pulls from GitHub after detecting an update
  - Quit, rebuild, restart
- 
### p2:
- Include up to date information that might not reflect the spreadsheet
  - Absence
  - Virtual
- Animations (ACM, ASCII)
- Database
# UX
## CUJ
### p0: p1:
- No interaction between admin and terminal
### p2:
- Second repo or API call that has updated info based on tutor, or the ACM Eboard calendar
# Engineering Design
## Stack
Python for API calls, C with vn_ui, json-c, crontab
## Rendering
- Sectioned off panels that information is displayed on
  - panels are hard coded and layered on top of text, which will make appropriate room
# Next Steps
## TODO
- Actual way to build and run that isn't hacked together