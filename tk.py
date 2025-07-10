import tkinter as tk
from PIL import Image, ImageTk
import cv2
import face_recognition
import os
import pickle

class FaceRegistrationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Registration")

        # Create a label to display the camera feed
        self.video_label = tk.Label(root)
        self.video_label.pack()

        # Create an entry for the name input
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=10)

        # Create a button to start face registration
        self.register_button = tk.Button(root, text="Register", command=self.register_face)
        self.register_button.pack(pady=5)

        # Open the webcam
        self.video_capture = cv2.VideoCapture(0)

        # Initialize a counter to keep track of the number of images captured
        self.counter = 0

        # Start the GUI update loop
        self.update()

    def register_face(self):
        name = self.name_entry.get()
        if name:
            # Create a directory for saving face encodings if it doesn't exist
            if not os.path.exists("saved_model/Face"):
                os.makedirs("saved_model/Face")

            # Capture a frame from the webcam
            ret, frame = self.video_capture.read()

            # Convert the image to RGB format
            rgb_frame = frame[:, :, ::-1]

            # Find the face location in the image
            face_locations = face_recognition.face_locations(rgb_frame)

            # If there is a face in the image, save it
            if len(face_locations) > 0:
                # Encode the face image
                face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]

                # Save the face encoding to a file
                with open(os.path.join("saved_model/Face", f"{name}.pkl"), "wb") as f:
                    pickle.dump(face_encoding, f)

                # Increment the counter
                self.counter += 1

    def update(self):
        # Capture a frame from the webcam
        ret, frame = self.video_capture.read()

        # Convert the image to RGB format
        rgb_frame = frame[:, :, ::-1]

        # Find the face location in the image
        face_locations = face_recognition.face_locations(rgb_frame)

        # Display the image with the face location marked
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Create an image from the frame
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)

        # Update the label with the new image
        self.video_label.configure(image=photo)
        self.video_label.image = photo

        # Schedule the next update
        self.root.after(1, self.update)

# Create the Tkinter root window
root = tk.Tk()

# Create an instance of the FaceRegistrationGUI
face_registration_gui = FaceRegistrationGUI(root)

# Run the Tkinter event loop
root.mainloop()
