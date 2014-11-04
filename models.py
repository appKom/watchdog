from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

# Sets up variable for simplification in script
metadata = MetaData()


# Generates a check-in table with associated columns
checkin = Table('checkin', metadata,
	Column('checkin_id', Integer, primary_key=True),
	Column('name', String(20)),
	Column('cardnumber', String(10)),
	Column('time', String(20))
	)