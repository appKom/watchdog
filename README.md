Watchdog
========

## What is watchdog?

Watchdog is a script-package that offers tools that keeps track of when people check in at the office. One part is client-side and handles the checkins and the other is server-side that handles reporting who showed up for their watch-hours.

### Part 1: watchdog.py

This script is runs in the terminal and takes in a cardnumber from a card-reader/scanner. It then gets the name associated with the cardnumber and saves it to an SQL-database.

### Part 2: watchreporter.py

This script reads from an ical file on the web, and compares it to the SQL-database that watchdog writes to. It gets the watch-hours from the ical and checks if people checked in during their watch-hours from the SQL-database.

## Notes and limitations:
