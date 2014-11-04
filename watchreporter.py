from icalendar import Calendar
from datetime import datetime, timedelta, date
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from tzlocal import get_localzone
from models import checkin
import urllib.request
import smtplib
import pytz

# Gets ical file and parses it to a calendar
# Example ical is used
req = urllib.request.Request('https://www.google.com/calendar/ical/b72fgdhuv6g5mpoqa0bdvj095k%40group.calendar.google.com/public/basic.ics')
response = urllib.request.urlopen(req)
data = response.read()
gcal = Calendar.from_ical(data)

# Creates empty list for future use and utc variable for timezone converting
people = {}
utc = pytz.UTC

# Here you can store some variables for customization purposes
# Sqlstring is filled with example case and uses mysql connectors
sqlString = 'mysql+mysqlconnector://appkom:appKom123@localhost/test'
frommail = 'frommail@mail.com'
tomail = 'tomail@mail.com'
subject = ('Daily Office Report ' + str(date.today()))

# The date that starts generating the calendar
defineDate = datetime(2014, 9, 22, 00, 00).replace(tzinfo=get_localzone())

# Sets up the engine to get information from SQL server
engine = create_engine(sqlString, echo=False)
conn = engine.connect()


# Generates a text-field for the e-mail report
def generateText():
    textField = "These people did not check in during their watch-hours: "

    for person in people:
        textField += ("\n" + person)

    return textField

# Sends the email with the content apropriate to the reciever
# TODO: Set up email syntax when comparing logic is finished
def sendEmail(content):
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(frommail, tomail, content)         
        print ("Successfully sent email")
    except SMTPException:
        print ("Error: unable to send email")

# Loops through the ical and looks for relevant events
for event in gcal.walk('vevent'):
    isFound = False

    start = event.decoded('dtstart')

    # Debug print
    print(event.get('summary'))

    todate = datetime.now().replace(tzinfo=get_localzone())

    today = todate.weekday()

    yesterday = today - 1

    # Debug print
    print(start.weekday())

    # Compares the dates of the ical events towards the current date
    if ((start > defineDate) and (start.weekday() >= yesterday) and (start.weekday() <= today)):
        name = event.get('summary')
        end = event.get('dtend')

        print('hello')

        # Gets the data from the database
        s = select([checkin])
        result = conn.execute(s)

        # Loops through the sql content
        for row in result:
            tempTime = row['time'].split(':')
            tempName = row['name']
            tempWeekDay = int(tempTime[0])
            tempHours = int(tempTime[1])
            tempMinutes = int(tempTime[2])

            tempNameList = name.split(' ')
            name = (tempNameList[0] + " " + tempNameList[(len(tempNameList) - 1)])

            # Todo: Update logic to handle date and weekday comparison as the ical is generated based on a week

            # Compares the date from server with current date
            if ((newTime > start) and (newTime < end) and (name == tempName)):
                isFound = True

        if (not(isFound)):
            people.append(name)

emailText = generateText()

# Debug Print
print(emailText)

# TODO: Generate email using function above and send to desired email

response.close()
