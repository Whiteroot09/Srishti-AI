import cv2
import numpy as np
import face_recognition
import psycopg2

# Connect to the PostgreSQL database
DATABASE_URL = 'postgres://srishti_database_ai_user:JaYaL1A92lAp0ikj0RxGjgKihQ3etVWj@dpg-cic47a95rnuk9qb0sbc0-a.oregon-postgres.render.com/srishti_database_ai'

# Create a table to store face data if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS test_user (
        id SERIAL PRIMARY KEY,
        name TEXT,
        encoding BYTEA
    )
'''

# Register a face and save the data to the database
def register_face(name):
    # Open the webcam
    video_capture = cv2.VideoCapture(0)

    # Initialize a counter to keep track of the number of images captured
    counter = 0

    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Execute the create table query
    cursor.execute(create_table_query)

    # Keep capturing images until 50 images are captured or 'q' key is pressed
    while counter < 50:
        # Capture a frame from the webcam
        ret, frame = video_capture.read()

        # Convert the image to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find the face location in the image
        face_locations = face_recognition.face_locations(rgb_frame)

        # If there is a face in the image, save it to the database
        if len(face_locations) > 0:
            # Encode the face image
            face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]

            # Save the face data to the database
            cursor.execute('INSERT INTO test_user (name, encoding) VALUES (%s, %s)', (name, face_encoding.tobytes()))

            # Increment the counter
            counter += 1

        # Display the image with the face location marked
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.imshow("Face Registration", frame)

        # Wait for 'q' key to be pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Commit the changes to the database
    conn.commit()

    # Release the webcam
    video_capture.release()
    cv2.destroyAllWindows()

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Recognize faces from the database
def recognize_face():
    # Open the webcam
    video_capture = cv2.VideoCapture(0)
    count = 0

    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Execute the create table query
    cursor.execute(create_table_query)

    # Loop over each frame from the webcam
    while True:
        # Capture a frame from the webcam
        ret, frame = video_capture.read()

        # Convert the image to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find the face locations in the image
        face_locations = face_recognition.face_locations(rgb_frame)

        # Encode the faces in the image
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop over each face in the image
        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Query the database to find matching faces
            cursor.execute('SELECT name, encoding FROM test_user')
            rows = cursor.fetchall()

            # Compare the face encoding to the known face encodings
            for name, encoding_blob in rows:
                # Convert the encoding from blob to numpy array
                face_encoding_db = np.frombuffer(encoding_blob, dtype=np.float64)

                # Compare the face encoding with the encoding from the database
                matches = face_recognition.compare_faces([face_encoding_db], face_encoding)

                # If the face is recognized, show the name and break from the loop
                if matches[0]:
                    return name
                else:
                    return None
            break
        break

    # Release the webcam and close the window
    video_capture.release()
    cv2.destroyAllWindows()

# Register a face and save the data to the database
# register_face("JAT")

# Recognize faces from the database
# recognize_face()
