import psycopg2
from urllib.parse import urlparse

# Database connection URL
db_url = "postgres://srishti_database_ai_user:JaYaL1A92lAp0ikj0RxGjgKihQ3etVWj@dpg-cic47a95rnuk9qb0sbc0-a.oregon-postgres.render.com/srishti_database_ai"

def add_data_to_table():
    # Data to be inserted
    id = '001'
    name = 'John Doe'
    gender = 'Male'
    password = 'password123'
    email = 'johndoe@example.com'

    try:
        # Parse the URL to extract the connection details
        parsed_url = urlparse(db_url)

        # Get the connection details
        host = parsed_url.hostname
        port = parsed_url.port
        user = parsed_url.username
        password = parsed_url.password
        database = parsed_url.path.lstrip("/")

        # Connect to the database
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor
        cursor = conn.cursor()

        # SQL statement to insert data
        insert_query = "INSERT INTO person_database_sri (id, name, gender, password, email) VALUES (%s, %s, %s, %s, %s)"

        # Execute the SQL statement with the data
        cursor.execute(insert_query, (id, name, gender, password, email))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        print("Data added successfully.")

    except psycopg2.Error as e:
        print("Error connecting to the PostgreSQL database:", e)

# Call the function to add data to the table
def delete_data_from_table():
    # Data to be deleted
    id = 'test'

    try:
        # Parse the URL to extract the connection details
        parsed_url = urlparse(db_url)

        # Get the connection details
        host = parsed_url.hostname
        port = parsed_url.port
        user = parsed_url.username
        password = parsed_url.password
        database = parsed_url.path.lstrip("/")

        # Connect to the database
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor
        cursor = conn.cursor()

        # SQL statement to delete data
        delete_query = "DELETE FROM person_database_sri WHERE id = %s"

        # Execute the SQL statement with the data
        cursor.execute(delete_query, (id,))

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        print("Data deleted successfully.")

    except psycopg2.Error as e:
        print("Error connecting to the PostgreSQL database:", e)

# Call the function to delete data from the table
# delete_data_from_table()
add_data_to_table()

