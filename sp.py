import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

root = tk.Tk()

imageurl = "https://raw.githubusercontent.com/ARNAB-BOTMAS/database_SRISHTI/main/ai.png"
u = urlopen(imageurl)
raw_data = u.read()
u.close()

# Create a file-like object from the raw data
image_file = BytesIO(raw_data)

# Open the image using PIL
image = Image.open(image_file)

# Define the desired width and height for resizing
new_width = 400
new_height = 300

# Resize the image using LANCZOS resampling
resized_image = image.resize((new_width, new_height), Image.LANCZOS)

# Convert the resized image to PhotoImage
photo = ImageTk.PhotoImage(resized_image)

# Create a label and display the resized image
label = tk.Label(image=photo)
label.image = photo
label.pack()

root.mainloop()
