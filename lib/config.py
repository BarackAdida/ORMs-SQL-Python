import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("db/hospital.db")

# Create a cursor object
cursor = conn.cursor()
