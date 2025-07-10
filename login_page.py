import threading
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from database_json_ROK import login, sign_up


def page_gui():
    global user_name
    global password
    global gender
    global signup_window
    global window

    def on_log_in():
        name = login()
        li = []
        li = name.split("@")
        user_id = li[0]
        name = li[1],
        gender = li[2]
        password = li[3]

        window.withdraw()
        log = tk.Toplevel(window)
        log.title("log in")
        log.geometry("600x600")

        from SRIshti import srishti
        srishti(name, gender)



    def on_enter1(event):
        log_btn.config(bg='#7D3C98', fg="white")

    def on_leave1(event):
        log_btn.config(bg='#BB8FCE', fg="black")

    def on_enter2(event):
        sign_btn.config(bg='#7D3C98', fg="white")

    def on_leave2(event):
        sign_btn.config(bg='#BB8FCE', fg="black")

    def on_user_enter(e):
        global user_name
        user_name.delete(0, 'end')

    def on_user_leave(e):
        global user_name
        name = user_name.get()
        if name == '':
            user_name.insert(0, 'Username')

    def on_pass_enter(e):
        global password
        password.delete(0, 'end')

    def on_pass_leave(e):
        global password
        name = password.get()
        if name == '':
            password.insert(0, 'Password')

    def on_gender_enter(e):
        global gender
        gender.delete(0, 'end')

    def on_gender_leave(e):
        global gender
        name = gender.get()
        if name == '':
            gender.insert(0, 'Gender')

    def open_signup():
        global user_name
        global password
        global gender
        global signup_window

        window.withdraw()
        signup_window = tk.Toplevel(window)
        signup_window.title("Signup Page")
        signup_window.geometry("700x700")
        signup_window.resizable(False, False)
        signup_window.protocol("WM_DELETE_WINDOW", lambda: close_signup(signup_window))

        frame = tk.Label(signup_window, bg="red")
        frame.pack(fill="both", expand=True, padx=40, pady=40)

        image3 = Image.open("gui/ai.png")
        resize_image3 = image3.resize((300, 300))
        img3 = ImageTk.PhotoImage(resize_image3)
        top_img = tk.Label(frame, image=img3, width=160, height=200, bg="red")
        top_img.pack(side=tk.TOP, pady=20, padx=10)
        top_img.image = img3
        window.after(0, lambda: top_img.configure(image=img3))


        user_name = tk.Entry(frame, width=50, font=('Microsoft Yahei UI Light', 11), bd=0)
        user_name.pack(side=tk.TOP, pady=20)
        user_name.insert(0, 'Username')
        user_name.bind("<FocusIn>", on_user_enter)
        user_name.bind("<FocusOut>", on_user_leave)

        gender_values = ['Male', 'Female', 'Other']
        gender = ttk.Combobox(frame, values=gender_values, font=('Microsoft Yahei UI Light', 11), width=47)
        gender.set('Select Gender')
        gender.pack(side=tk.TOP, pady=5)

        password = tk.Entry(frame, width=50, font=('Microsoft Yahei UI Light', 11), bd=0)
        password.pack(side=tk.TOP, pady=20)
        password.insert(0, 'Password')
        password.bind("<FocusIn>", on_pass_enter)
        password.bind("<FocusOut>", on_pass_leave)

        submit = tk.Label(frame, bg="#BB8FCE", bd=0, width=60, height=10)
        submit.pack(side=tk.TOP)

        next = tk.Button(submit, text="Next", font=('Microsoft Yahei UI Light', 8), width=10, height=2, bd=0, padx=20, command=validate_fields)
        next.pack(side=tk.LEFT, padx=20)

        cancel = tk.Button(submit, text="Cancel", font=('Microsoft Yahei UI Light', 8), width=10, height=2, bd=0, padx=20, command=lambda: close_signup(signup_window))
        cancel.pack(side=tk.RIGHT, padx=20)

    def close_signup(signup_window):
        signup_window.destroy()
        window.deiconify()

    def validate_fields():
        # Retrieve the values from Entry widgets
        username = user_name.get()
        user_gender = gender.get()
        user_password = password.get()

        user_name.bind("<FocusIn>", on_user_enter)
        user_name.bind("<FocusOut>", on_user_leave)
        password.bind("<FocusIn>", on_pass_enter)
        password.bind("<FocusOut>", on_pass_leave)

        if username == 'Username':
            user_name.config(fg="red")
        elif user_password == 'Password':
            password.config(fg="red")
        elif user_gender == 'Select Gender':
            gender.config(fg="red")
        else:
            sign_up(username, user_gender, user_password, signup_window)

    window = tk.Tk()
    window.title('Login page')
    window.configure(bg="#F2F4F4")
    window.resizable(False, False)

    def load_images():
        global img1, img2

        image1 = Image.open("gui/log.png")
        resize_image1 = image1.resize((500, 500))
        img1 = ImageTk.PhotoImage(resize_image1)
        label1.image = img1  # Assign the image to the label's attribute

        # Update label1 image using main thread
        window.after(0, lambda: label1.configure(image=img1))

        image2 = Image.open("gui/ai.png")
        resize_image2 = image2.resize((350, 350))
        img2 = ImageTk.PhotoImage(resize_image2)
        label2.image = img2  # Assign the image to the label's attribute

        # Update label2 image using main thread
        window.after(0, lambda: label2.configure(image=img2))

    label1 = tk.Label(window, bg="#F2F4F4")
    label1.pack(side=tk.LEFT, pady=20, padx=20)

    frame = tk.Frame(window, bg="#AED6F1", width=500, height=500)
    frame.pack(side=tk.RIGHT, padx=20, pady=20, expand=True)

    heading = tk.Label(frame, text="🤖SRIshti", fg="#A569BD", bg="#AED6F1", font=("Microsoft YaHei UI Light", 30, "bold"))
    heading.place(x=150, y=10)

    label2 = tk.Label(frame, bg="#AED6F1")
    label2.place(x=150, y=100, width=200, height=250)

    log_btn = tk.Button(frame, text="Log in", bg="#BB8FCE", bd=0, command=on_log_in)
    log_btn.place(x=140, y=400, width=100, height=50)
    log_btn.bind('<Enter>', on_enter1)
    log_btn.bind('<Leave>', on_leave1)

    sign_btn = tk.Button(frame, text="Sign Up", bg="#BB8FCE", bd=0, command=open_signup)
    sign_btn.place(x=270, y=400, width=100, height=50)
    sign_btn.bind('<Enter>', on_enter2)
    sign_btn.bind('<Leave>', on_leave2)

    threading.Thread(target=load_images).start()
    window.mainloop()

threading.Thread(target=page_gui).start()
