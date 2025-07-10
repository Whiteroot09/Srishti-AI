import time
import threading
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from database_json_ROK import login, sign_up_data
import SRIshti
dashboard_called = False

def dashboard():
    # global dashboard_called
    # if dashboard_called:
    #     return
    # dashboard_called = True

    def on_enter1(event):
        log_btn.config(bg='#7D3C98', fg="white")

    def on_leave1(event):
        log_btn.config(bg='#BB8FCE', fg="black")

    def on_enter2(event):
        sign_btn.config(bg='#7D3C98', fg="white")

    def on_leave2(event):
        sign_btn.config(bg='#BB8FCE', fg="black")

    def close_window():
        window.destroy()

    window = tk.Tk()
    window.title("Dashboard")
    window.resizable(False, False)
    image1 = Image.open("gui/log.png")
    resize_image1 = image1.resize((500, 500))
    img1 = ImageTk.PhotoImage(resize_image1)
    label1 = tk.Label(window, bg="#F2F4F4", image=img1)
    label1.pack(side=tk.LEFT, pady=20, padx=20)
    label1.image = img1

    frame = tk.Frame(window, bg="#AED6F1", width=500, height=500)
    frame.pack(side=tk.RIGHT, padx=20, pady=20, expand=True)

    heading = tk.Label(frame, text="🤖SRIshti", fg="#A569BD", bg="#AED6F1", font=("Microsoft YaHei UI Light", 30, "bold"))
    heading.place(x=150, y=10)

    image2 = Image.open("gui/ai.png")
    resize_image2 = image2.resize((350, 350))
    img2 = ImageTk.PhotoImage(resize_image2)
    label2 = tk.Label(frame, bg="#AED6F1")
    label2.place(x=150, y=100, width=200, height=250)
    label2.image = img2

    log_btn = tk.Button(frame, text="Log in", bg="#BB8FCE", bd=0, command=lambda: log_in(window))
    log_btn.place(x=140, y=400, width=100, height=50)
    log_btn.bind('<Enter>', on_enter1)
    log_btn.bind('<Leave>', on_leave1)

    sign_btn = tk.Button(frame, text="Sign Up", bg="#BB8FCE", bd=0, command=lambda: sign_up(window))
    sign_btn.place(x=270, y=400, width=100, height=50)
    sign_btn.bind('<Enter>', on_enter2)
    sign_btn.bind('<Leave>', on_leave2)

    label1.config(image=img1)
    label2.config(image=img2)

    window.protocol("WM_DELETE_WINDOW", close_window)
    window.mainloop()

def log_in(window):
    window.destroy()
    root = tk.Tk()
    root.geometry("600x600")
    root.resizable(False, False)
    frame = tk.Label(root, bg="#CCD1D1")
    frame.pack(side=tk.TOP, expand=True, fill="both", padx=20, pady=20)
    image3 = Image.open("gui/ai.png")
    resize_image3 = image3.resize((300, 300))
    img3 = ImageTk.PhotoImage(resize_image3)
    top_img = tk.Label(frame, image=img3, width=160, height=200, bg="#CCD1D1")
    top_img.pack(side=tk.TOP, pady=20, padx=10)
    top_img.image = img3

    data = tk.Label(frame, bg="#CCD1D1", width=50)
    data.pack(side=tk.TOP, expand=True, fill="both")

    def countdown():
        def close_log(root):
            root.destroy()
            dashboard()

        def on_enter_ok(event):
            okey.config(bg='#1E8449', fg="white")

        def on_leave_ok(event):
            okey.config(bg='#A9DFBF', fg="black")

        def on_enter_cancel(event):
            cancel.config(bg='#1E8449', fg="white")

        def on_leave_cancel(event):
            cancel.config(bg='#A9DFBF', fg="black")

        def on_enter_go_back(event):
            can_btn.config(bg='#B03A2E', fg="white")

        def on_leave_go_back(event):
            can_btn.config(bg='#F1948A', fg="black")

        i = 0
        data.config(text="At first I start to scan your face\nand get your Face ID",
                    font=('Microsoft Yahei UI Light', 15, "bold"), fg="#34495E")
        time.sleep(4)
        data.config(text="make sure the camera is connected\nAnd the Internet is OK ")
        time.sleep(4)
        data.config(text="you have total 5 second to do that")
        time.sleep(4)
        data.config(
            text="After 5 second\nThe password section will appear\nand you need to provide the password\nfor your user account")
        time.sleep(4)
        while i <= 5:
            time.sleep(1)
            i += 1
            data.config(text=f"{i}")
        data.config(text="Your face is scanning now!!!")
        time.sleep(2)
        pack = login()
        time.sleep(2)
        lab_msg = tk.Frame(data, bg="#CCD1D1")
        lab_msg.pack(side=tk.TOP, fill="both")

        if pack == None:
            data.config(text="(Ծ‸ Ծ)", font=("Arial", 80, "bold"), fg="#CB4335")
            time.sleep(2)

            not_found = tk.Label(lab_msg)
            not_found.pack(side=tk.TOP, fill="both")
            not_found.config(text="Face ID not found", font=("Arial", 20))

            confirm_layer = tk.Frame(lab_msg, width=20)
            confirm_layer.pack(side=tk.TOP)

            can_btn = tk.Button(confirm_layer, bd=0, text="Go Back", bg="#F1948A", width=10,
                                command=lambda: close_log(root))
            can_btn.pack(side=tk.TOP, pady=10, padx=10)
            can_btn.bind("<Enter>", on_enter_go_back)
            can_btn.bind("<Leave>", on_leave_go_back)

            data.config(text="You need to go back and log in again!!\nOr if you not sign up in SING UP",
                        font=("Arial", 10, "bold"), fg="#B03A2E")
        else:
            data.config(text="(◍•ᴗ•◍)", font=("Arial", 80, "bold"), fg="#27AE60")
            time.sleep(2)
            data.config(text="Is that You?", font=("Arial", 10, "bold"), fg="#27AE60")
            userid = pack[0]
            name = pack[1]
            gender = pack[2]
            password = pack[3]

            user_id = tk.Label(lab_msg)
            user_id.pack(side=tk.TOP, fill="both")
            user_id.config(text=f"Face ID: {userid}", font=("Arial", 15))

            name_id = tk.Label(lab_msg)
            name_id.pack(side=tk.TOP, fill="both")
            name_id.config(text=f"Name: {name}", font=("Arial", 12))

            confirm_layer = tk.Frame(lab_msg)
            confirm_layer.pack(side=tk.TOP)

            okey = tk.Button(confirm_layer, width=10, text="Okey", bg="#A9DFBF", bd=0,
                             command=lambda: log_in_ai(root, name, gender, password))
            okey.pack(side=tk.LEFT, pady=10, padx=10)
            okey.bind('<Enter>', on_enter_ok)
            okey.bind('<Leave>', on_leave_ok)

            cancel = tk.Button(confirm_layer, width=10, text="Cancel", bg="#A9DFBF", bd=0,
                               command=lambda: close_log(root))
            cancel.pack(side=tk.RIGHT, pady=10, padx=10)
            cancel.bind('<Enter>', on_enter_cancel)
            cancel.bind('<Leave>', on_leave_cancel)

        def log_in_ai(root, name, gender, password):

            def on_pasd_enter(e):
                pasd.delete(0, 'end')

            def on_pasd_leave(e):
                name = pasd.get()
                if name == '':
                    pasd.insert(0, 'Password')

            lab_msg.destroy()
            confirm_layer.destroy()
            data.config(text="Confirm your password")
            pasd = tk.Entry(data, font=('Microsoft Yahei UI Light', 15, "bold"))
            pasd.pack(side=tk.TOP, fill="both")
            pasd.insert(0, "Password")
            pasd.bind("<FocusIn>", on_pasd_enter)
            pasd.bind("<FocusOut>", on_pasd_leave)
            check_btn = tk.Button(data, text="Confirm", command=lambda: check_btn_sri(root, name, gender, password))
            check_btn.pack(side=tk.TOP)

            def check_btn_sri(root, name, gender, password):
                psd = pasd.get()
                if psd == password:
                    root.destroy()
                    SRIshti.srishti(name, gender)
                else:
                    data.config(text="Wrong password", fg="red")

        top_img.config(image=img3)

    threading.Thread(target=countdown).start()
    root.mainloop()

def sign_up(window):
    window.destroy()

    def close_log(root):
        root.destroy()
        dashboard()

    def on_enter_ok(event):
        submit_btn.config(bg='#1E8449', fg="white")

    def on_leave_ok(event):
        submit_btn.config(bg='#A9DFBF', fg="black")

    def on_enter_cancel(event):
        cancel_btn.config(bg='#1E8449', fg="white")

    def on_leave_cancel(event):
        cancel_btn.config(bg='#A9DFBF', fg="black")

    def on_user_enter(e):
        user_name.config(fg="black")
        user_name.delete(0, 'end')

    def on_user_leave(e):
        name = user_name.get()
        if name == '':
            user_name.insert(0, 'USERNAME')

    def on_pass_enter(e):
        password_ent.config(fg="black")
        password_ent.delete(0, 'end')

    def on_pass_leave(e):
        name = password_ent.get()
        if name == '':
            password_ent.insert(0, 'PASSWORD')

    def on_email_enter(e):
        mail_ent.config(fg="black")
        mail_ent.delete(0, 'end')

    def on_email_leave(e):
        name = mail_ent.get()
        if name == '':
            mail_ent.insert(0, 'EMAIL')

    def on_selection(event):
        gender_combobox.config(foreground="black")
        selected_item = gender_combobox.get()
        print("Selected gender:", selected_item)

    root = tk.Tk()
    root.geometry("600x600")
    root.resizable(False, False)
    frame = tk.Label(root, bg="#CCD1D1")
    frame.pack(side=tk.TOP, expand=True, fill="both", padx=20, pady=20)
    image3 = Image.open("gui/ai.png")
    resize_image3 = image3.resize((300, 300))
    img3 = ImageTk.PhotoImage(resize_image3)
    top_img = tk.Label(frame, image=img3, width=160, height=200, bg="#CCD1D1")
    top_img.pack(side=tk.TOP, pady=20, padx=10)
    top_img.image = img3

    center_label = tk.Label(frame, bg="#CCD1D1")
    center_label.pack(side=tk.TOP, expand=True, fill="both")

    user_name = tk.Entry(center_label, font=('Microsoft Yahei UI Light', 10, "bold"), bd=0, fg="#AAB7B8")
    user_name.pack(side=tk.TOP, pady=10, padx=10, fill="both")
    user_name.insert(0, "USERNAME")
    user_name.bind("<FocusIn>", on_user_enter)
    user_name.bind("<FocusOut>", on_user_leave)

    password_ent = tk.Entry(center_label, font=('Microsoft Yahei UI Light', 10, "bold"), bd=0, fg="#AAB7B8")
    password_ent.pack(side=tk.TOP, pady=10, padx=10, fill="both")
    password_ent.insert(0, "PASSWORD")
    password_ent.bind("<FocusIn>", on_pass_enter)
    password_ent.bind("<FocusOut>", on_pass_leave)

    gender_combobox = ttk.Combobox(center_label, values=["Male", "Female", "Other"],
                                   font=('Microsoft Yahei UI Light', 10, "bold"), foreground="#AAB7B8")
    gender_combobox.pack(side=tk.TOP, pady=10, padx=10, fill="both")
    gender_combobox.set("GENDER")
    gender_combobox.bind("<<ComboboxSelected>>", on_selection)

    mail_ent = tk.Entry(center_label, font=('Microsoft Yahei UI Light', 10, "bold"), bd=0, fg="#AAB7B8")
    mail_ent.pack(side=tk.TOP, pady=10, padx=10, fill="both")
    mail_ent.insert(0, "EMAIL")
    mail_ent.bind("<FocusIn>", on_email_enter)
    mail_ent.bind("<FocusOut>", on_email_leave)

    bottom_label = tk.Label(center_label, bg="#CCD1D1", height=20)
    bottom_label.pack(side=tk.TOP)

    submit_btn = tk.Button(bottom_label, text="Submit", font=('Microsoft Yahei UI Light', 10, "bold"), bd=0,
                           bg='#A9DFBF', fg="black", command=lambda: submit_sign())
    submit_btn.pack(side=tk.LEFT, padx=10, pady=10)
    submit_btn.bind("<Enter>", on_enter_ok)
    submit_btn.bind("<Leave>", on_leave_ok)

    def submit_sign():
        username = user_name.get()
        password = password_ent.get()
        gender = gender_combobox.get()
        mail = mail_ent.get()

        if username == "USERNAME":
            user_name.config(fg="red")

        elif password == "PASSWORD":
            password_ent.config(fg="red")

        elif gender == "GENDER":
            gender_combobox.config(foreground="red")

        elif mail == "EMAIL":
            mail_ent.config(fg="red")

        else:
            sign_up_data(username, gender, password, mail, root)

    cancel_btn = tk.Button(bottom_label, text="Cancel", font=('Microsoft Yahei UI Light', 10, "bold"), bd=0,
                           bg='#A9DFBF', fg="black", command=lambda: close_log(root))
    cancel_btn.pack(side=tk.RIGHT, padx=10, pady=10)
    cancel_btn.bind("<Enter>", on_enter_cancel)
    cancel_btn.bind("<Leave>", on_leave_cancel)

    top_img.config(image=img3)
    root.mainloop()

if __name__ == "__main__":
    threading.Thread(target=dashboard).start()
