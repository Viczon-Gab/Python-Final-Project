import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Ecoseas"
)

cursor = db.cursor()


#table1 = "INSERT INTO Category (Category_ID, Category_Name) VALUES (%s, %s)"
#values1 = [
#    (1, "Mammals"),
#    (2, "Plants"),
#    (3, "Ocean Fishes"),
#    (4, "Others")
#]
#cursor.executemany(table1, values1)

#table2 = "INSERT INTO Species (Species_ID, Species_Name, Category_ID) VALUES (%s, %s, %s)"
#values2 = [
#    (101, "Dolphin", 1),
#    (102, "Whale", 1),
#    (103, "Seals", 1),
#    (104, "Sea Lions", 1),
#    (105, "Sea Otters", 1),
#    (106, "Manatees", 1),
#    (201, "Phytoplankton", 2),
#    (202, "Seagrasses", 2),
#    (203, "Algae", 2),
#    (204, "Kelp", 2),
#    (205, "Sargassum", 2),
#    (301, "Shark", 3),
#    (302, "Seahorse", 3),
#    (303, "Bluefin Tuna", 3),
#    (304, "Eel", 3),
#    (401, "Octopus", 4),
#    (402, "Crabs", 4),
#    (403, "Lobster", 4),
#    (404, "Shrimp", 4)
#]
#cursor.executemany(table2, values2)

#table3 = "INSERT INTO Threats (Threats_ID, Threats_Name) VALUES (%s, %s)"
#values3 = [
#    ("Threat1", "Plastic Pollution"),
#    ("Threat2", "Chemical Pollution"),
#   ("Threat3", "Climate Change"),
#    ("Threat4", "Overfishing"),
#   ("Threat5", "Loss of Habitat"),
#    ("Threat6", "Ocean Noise Pollution"),
#    ("Threat7", "Invasive Species")
#]
#cursor.executemany(table3, values3)


#table4 = "INSERT INTO Conservation_Tips (Tip_ID, Tip_Name) VALUES (%s, %s)"
#values4 = [
#    ("Tip1", "Reduce Plastic Usage"),
#    ("Tip2", "Support Sustainable Seafood"),
#    ("Tip3", "Participate in Beach Cleanups"),
#    ("Tip4", "Minimize Chemical Use"),
#    ("Tip5", "Conserve Water"),
#    ("Tip6", "Protect Marine Habitats"),
#    ("Tip7", "Raise Awareness")
#]
#cursor.executemany(table4, values4)

#table5 = "INSERT INTO Quizzes (Quiz_ID, Species_ID, Question, Correct_Answer, Wrong_Answers) VALUES (%s, %s, %s, %s, %s)"
#values5 = [
#    ("Quiz1", 404, "Question1", "B", "A C D"),
#    ("Quiz2", 103, "Question2", "B", "A C D"),
#    ("Quiz3", 202, "Question3", "A", "B C D")
#]
#cursor.executemany(table5, values5)

#db.commit()

print("All data committed successfully!")

#Retrieve data from tables
print("\nRetrieving data from 'Category' table:")
cursor.execute("SELECT * FROM Category")
categories = cursor.fetchall()
for category in categories:
    print(category)

print("\nRetrieving data from 'Species' table:")
cursor.execute("SELECT * FROM Species")
species = cursor.fetchall()
for specie in species:
    print(specie)

print("\nRetrieving data from 'Threats' table:")
cursor.execute("SELECT * FROM Threats")
threats = cursor.fetchall()
for threat in threats:
    print(threat)

print("\nRetrieving data from 'Conservation_Tips' table:")
cursor.execute("SELECT * FROM Conservation_Tips")
tips = cursor.fetchall()
for tip in tips:
    print(tip)

print("\nRetrieving data from 'Quizzes' table:")
cursor.execute("SELECT * FROM Quizzes")
quizzes = cursor.fetchall()
for quiz in quizzes:
    print(quiz)


cursor.close()
db.close()
print("\nMySQL connection closed.")
