import os
import datetime
import time
from models import checkin, metadata
from sqlalchemy import create_engine, MetaData


# Fill these out for your database. PS: THIS USES MYSQL CONNECTORS. EDIT FOR OTHER CONNECTIONS IF NEEDED
# Filled out with example case
username = "appkom"
password = "appKom123"
dbLocation = "localhost/test"

# Generates the variables used later
engine = create_engine('mysql+mysqlconnector://' + username + ':' + password + '@' + dbLocation, echo=False)
cardnumber = "0"
number = "0"
name = ""



#TODO: get the name associated with cardnumber from API
def returnName(numb):
	#Temp name until API is in place
	name = "Temp Name"
	return name


# Connects and safely creates the DB if it doesn't exist
try:
	conn = engine.connect()
	metadata.create_all(engine)

except:
	print("Oooops. Something went wrong while connecting to the database, is it up?")

# Main program that loops
while (number != 'exit'):
	print ("Skann kortet:")

	# Gets input from card-reader
	number = str(input())

	# Uses function to get name from API
	username = returnName(number)

	# Gets current date and trims it down to relevant size
	tempdate = datetime.datetime.now()
	date = str(tempdate.weekday()) + ':' + str(tempdate.hour) + ':' + str(tempdate.minute)

	# Formats name for later use in watchreporter PS: Uses first and last name. Will add exception handling later
	tempName = username.split(' ')
	username = (tempName[0] + " " + tempName[(len(tempName) - 1)])

	# Generates an SQL-query
	ins = checkin.insert().values(name = username, cardnumber = number, time = date)

	# Executes the SQL-query
	try:
		result = conn.execute(ins)
	except:
		print("Something went wrong writing to the database. Your check-in was not registered")
		continue

	print("You are checked in, " + username + ". Console will reset in 10 seconds")

	# Waits and then clears the console
	time.sleep(10)
	clear = lambda: os.system('cls')
	clear()

