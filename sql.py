import sqlite3

## Connect to sqlite
conn = sqlite3.connect("student.db")

## Create a cursor object to insert, create table, retrieve data
cursor = conn.cursor()

##Create table
table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

## Insert data

cursor.execute('''INSERT INTO STUDENT VALUES('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sudhanshu', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Darius', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Vikash', 'DEVOPS', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Dipesh', 'DEVOPS', 'A', 35)''')

## Display all data
print("The inserted data is:")
data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

## Close connection
conn.commit()
conn.close()