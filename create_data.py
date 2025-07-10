import psycopg2

# Connection parameters
url = 'postgres://srishti_database_user:Db6wKof7pq0kXcvTJt27Ko5AMhZoGV8a@dpg-ci7f8lenqql0ldbdt070-a.oregon-postgres.render.com/srishti_database'

# Establish a connection
conn = psycopg2.connect(url)

# Create a cursor
cursor = conn.cursor()

# SQL statement to create a table
create_table_query = '''
    CREATE TABLE person_database (
  id VARCHAR(100),
  name VARCHAR(50),
  gender VARCHAR(10),
  password VARCHAR(50),
  email VARCHAR(100)
);

'''

# Execute the CREATE TABLE statement
cursor.execute(create_table_query)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
