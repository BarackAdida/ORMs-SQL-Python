from doctor import Doctor

# Drop the existing doctors table to update the schema
Doctor.drop_table()

# Create the updated doctors table
Doctor.create_table()

# Create a new Doctor instance with the correct arguments
doctor1 = Doctor(1, "Barack", "Adida", "Male", "0110859228", 3, "Anesthesiology", "England")

doctor1.yop = 10

doctor1.update()

# Save the new Doctor instance to the database
doctor1.save()

# Print the doctor instance to verify
print(doctor1)

doctor2 = Doctor(2, "Lapilly", "Pilly", "Male", "0100699066", 8, "Dentistry", "Kenya")

doctor2.save()

print(doctor2)
