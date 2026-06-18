import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kamal975",
    database="company"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employee")

for emp_id, name, dept, salary, join_date in cursor:
    print(f"ID: {emp_id}")
    print(f"Name: {name}")
    print(f"Department: {dept}")
    print(f"Salary: {salary}")
    print(f"Joining Date: {join_date}")
    print("-" * 30)

cursor.close()
conn.close()