Watchdog
========
Latest version: 1.0

## What is watchdog?

Watchdog is a script-package that offers tools that keeps track of when people check in at the office. One part is client-side and handles the checkins and the other is server-side that handles reporting who showed up for their watch-hours.

### Part 1: watchdog.py

This script is runs in the terminal and takes in a cardnumber from a card-reader/scanner. It then gets the name associated with the cardnumber and saves it to an SQL-database.

### Part 2: watchreporter.py

This script reads from an ical file on the web, and compares it to the SQL-database that watchdog writes to. It gets the watch-hours from the ical and checks if people checked in during their watch-hours from the SQL-database.

## Notes and limitations:
- Currently very limited use as the scripts are written for a specific problem. It will be expanded later
- Written for MySQL atm, but will be customizable shortly
- Dependables will be added later as an "installation script" instead of manual install at client and server

##Version Log
###1.0:
- Working for Online Linjeforening
- Daily report is up and running
- Config file added for easy configuration
- MySQL version complete
