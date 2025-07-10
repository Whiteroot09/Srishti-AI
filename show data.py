import psycopg2
import json

# Connection parameters
url = 'postgres://srishti_database_user:Db6wKof7pq0kXcvTJt27Ko5AMhZoGV8a@dpg-ci7f8lenqql0ldbdt070-a.oregon-postgres.render.com/srishti_database'

# Establish a connection
conn = psycopg2.connect(url)

# Create a cursor
cursor = conn.cursor()

# SQL statement to select data
select_query = '''
    SELECT * FROM person_database
'''

# Execute the SELECT statement
cursor.execute(select_query)

# Fetch all the rows
rows = cursor.fetchall()

# Process the rows
results = {}
res = []
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
