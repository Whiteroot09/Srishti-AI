import psycopg2

def add_data(id, name, gender, password, email):
    # Connection parameters
    url1 = 'postgres://srishti_database_user:Db6wKof7pq0kXcvTJt27Ko5AMhZoGV8a@dpg-ci7f8lenqql0ldbdt070-a.oregon-postgres.render.com/srishti_database'

    # Establish a connection
    conn = psycopg2.connect(url1)

    # Create a cursor
    cursor = conn.cursor()
    # SQL statement to create a table
    person_data = [id, name, gender, password, email]
    # Insert the person into the database
    insert_query = '''INSERT INTO person_database (id, name, gender, password, email)
            VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(insert_query, person_data)

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()
    return True
