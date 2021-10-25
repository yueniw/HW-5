import psycopg2

conn = psycopg2.connect(
    database='postgres', 
    user='postgres', 
    password='mysecretpassword', 
    host='0.0.0.0', 
    port= '5432'
)
cursor = conn.cursor()
  
# execute your query
cursor.execute("SELECT * FROM EMPLOYEE LIMIT 10")
  
# fetch all the matching rows 
result = cursor.fetchall()
  
# loop through the rows
for row in result:
    print(row)