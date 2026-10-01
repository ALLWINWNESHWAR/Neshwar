
import oracledb

connection= oracledb.connect(

user = "system",
password = "neshwar@492464",
dsn = "localhost:1521/xe"
    )


cursor = connection.cursor()

cursor = connection.cursor()

cursor.execute(
"""
select * from students
"""
    )

records=cursor.fetchall()
print(records)

print("\n")

for i in records:
    print(i)

print("success")

cursor.close()
connection.close()
