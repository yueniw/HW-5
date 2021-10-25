import psycopg2

conn = psycopg2.connect(
    database='postgres', 
    user='postgres', 
    password='mysecretpassword', 
    host='0.0.0.0', 
    port= '5432'
)
cursor = conn.cursor()

cursor.execute("INSERT INTO employee(id, fname, lname) VALUES (generate_series(1, 500), substr(MD5(random()::text), 0, 10), substr(MD5(random()::text), 0,10)) ")

conn.commit()
cursor.close()
conn.close()