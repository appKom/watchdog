Watchdog
========
Latest version: 1.1

## What is watchdog?

Watchdog is a script-package that offers tools that keeps track of when people check in at the office. One part is client-side and handles the checkins and the other is server-side that handles reporting who showed up for their watch-hours.

## How to Install:
### Step 1:
Clone this repo, download the files or whatever you prefer. For easy install include all files on both sides.
You can remove watchreporter.py on the client-side and watchdog.py on the server-side if you want.

### Step 2:
Set up a MySQL database and create a user and password. Add the location, user and password of this database into config.py
The program will create a table for checkins if it doesn't exist, so don't worry about that

### Step 3:
Run pip install on requirements.txt. That will install all dependencies for the scripts

### Step 4:
Prepare a gmail user that will send out the daily reports. Fill in the mail-user, password and what mail will recieve the reports in config.py

### Step 5:
Follow these steps on the client and server and you'll be done.
Now you can run watchdog.py from the terminal and scan in cards using a card-reader. watchreporter.py will do it's work on the server-side.

### Part 1: watchdog.py

This script is runs in the terminal and takes in a cardnumber from a card-reader/scanner. It then gets the name associated with the cardnumber and saves it to an SQL-database.

### Part 2: watchreporter.py

This script reads from an ical file on the web, and compares it to the SQL-database that watchdog writes to. It gets the watch-hours from the ical and checks if people checked in during their watch-hours from the SQL-database.

## Notes and limitations:
- Currently very limited use as the scripts are written for a specific problem. It will be expanded later
- Written for MySQL atm, but will be customizable shortly
- Dependables will be added later as an "installation script" instead of manual install at client and server

## Version Log
### 1.1:
- Added a requirements text file for easy install with pip

### 1.0:
- Working for Online Linjeforening
- Daily report is up and running
- Config file added for easy configuration
- MySQL version complete
