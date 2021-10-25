import psycopg2

conn = psycopg2.connect(
    database='postgres', 
    user='postgres', 
    password='mysecretpassword', 
    host='0.0.0.0', 
    port= '5432'
)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql ='''CREATE TABLE EMPLOYEE(
   ID SERIAL,
   FNAME VARCHAR(10),
   LNAME VARCHAR(10)
)'''
cursor.execute(sql)

#for row in cursor:
    #print(row)

conn.commit()
cursor.close()
conn.close()