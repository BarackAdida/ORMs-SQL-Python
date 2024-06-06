from doctor import Doctor
from patient import cursor, conn, Patient
# Drop the existing doctors table to update the schema
Doctor.drop_table()
Patient.drop_table()
# Create the updated doctors table
Doctor.create_table()
Patient.create_table()

# Create a new Doctor instance with the correct arguments
doctor1 = Doctor(1, "Barack", "Adida", "Male", "0110859228", 3, "Anesthesiology", "England")

doctor1.yop = 10

doctor1.update()

# Save the new Doctor instance to the database
doctor1.save()

# Print the doctor instance to verify
# print(doctor1)

doctor2 = Doctor(2, "Lapilly", "Pilly", "Male", "0100699066", 8, "Dentistry", "Kenya")

doctor2.save()

# print(Doctor.all)

doctor3 = Doctor(3, "Extortionist", "Extortionista", "Male", "0757251844", 15, "Surgery", "South Africa")

doctor3.save()

sql = "SELECT * FROM doctors WHERE id = ?"
sql2 = "SELECT * FROM doctors"
rows = cursor.execute(sql2).fetchall()

row =cursor.execute(sql,(1,)).fetchone()

print(row)

print(rows)

# add patient to db
patient1 = Patient.create("Barack", "Pilly", 19, "Male", "0110859228",doctor1.id)
patient1 = Patient.create("Extortionista", "Balast", 19, "Female", "0110859228",doctor3.id)
patient1 = Patient.create("Lexicon", "Minions", 30, "Female", "0110859228",doctor2.id)
