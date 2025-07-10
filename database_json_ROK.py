import threading
import time
import tkinter as tk
import requests
from face_recog import register_face, recognize_face
import random
import string

url = 'https://webpage-srishti.onrender.com/users_data'
valid_api_key = '1c92dfbe48e8efa60f7c8bb6ad55cb8775b267ebdbc1b4e2f5973f2d5a0062a5'
headers = {
    'X-API-Key': valid_api_key
}

def sign_up_data(name, gender, password, mail, root):
    def generate_random_code(length):
        digits = ''.join(random.choices(string.digits, k=length - 5))
        characters = ''.join(random.choices(string.ascii_uppercase, k=5))
        code = "SRISHTI00023" + digits + characters
        return code
    data = requests.get(url, headers=headers)
    print(data.status_code)
    if data.status_code == 200:
        datas = data.json()
        ids = []
        for person in datas:
            id = person['id']
            ids.append(id)
        while True:
            random_number = generate_random_code(10)
            if random_number not in ids:
                new_id = random_number
                break
            else:
                continue
        face = recognize_face()
        print(face)
        if face is None:
            register_face(new_id)
            print(gender)
            print(mail)
            print(password)
            data = {
                "id": new_id,
                "name": name,
                "gender": gender,
                "password": password,
                "email": mail
            }
            res = requests.post(url, headers=headers, data=data)
            print(res.status_code)

            if res:
                print("Database add successfully")
                root.destroy()
                open_sign(new_id, name, password, gender, mail)
            else:
                # Request failed
                print('Fail to add database, Error Code:')

    else:
        root.destroy()
        close_sign()

def open_sign(new_id, name, password, gender, mail):
    def go_back():
        root.destroy()
        import SRI
        SRI.dashboard()
    root = tk.Tk()
    root.title("Thank you for signing")
    root.geometry("1000x400")
    root.resizable(False, False)
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, expand=True, fill="both", pady=25, padx=25)
    center = tk.Label(frame)
    center.pack(side=tk.TOP, expand=True, fill="both")
    center.config(text=f"Your Face ID: {new_id}", font=("Microsoft YaHei UI Light", 30, "bold"))
    center_name = tk.Label(frame)
    center_name.pack(side=tk.TOP)
    center_name.config(text=f"Name: {name}", font=("Microsoft YaHei UI Light", 15, "bold"))
    center_thank = tk.Label(frame)
    center_thank.pack(side=tk.TOP)
    center_thank.config(text="Thank You", font=("Microsoft YaHei UI Light", 15, "bold"))
    back_btn = tk.Button(frame, text="Go Back", command=lambda: go_back())
    back_btn.pack(side=tk.TOP)
    root.mainloop()

def close_sign():
    def go_back():
        root.destroy()
        import SRI
        SRI.dashboard()
    root = tk.Tk()
    root.title("You are Already signing up")
    root.geometry("1000x400")
    root.resizable(False, False)
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, expand=True, fill="both", padx=25, pady=25)
    center = tk.Label(frame)
    center.pack(side=tk.TOP, expand=True, fill="both")
    center.config(text="You are already sign up", font=("Microsoft YaHei UI Light", 30, "bold"))
    back_btn = tk.Button(root, text="Go Back", command=go_back)
    back_btn.pack(side=tk.TOP)
    root.mainloop()
def login():
    face = recognize_face()
    print(face)
    try:
        if face is None:
            pack = None
            return pack
        else:
            data = requests.get(url, headers=headers)
            datas = data.json()
            for person in datas:
                id = person['id']
                if id == face:
                    name = person['name']
                    gender = person['gender']
                    password = person['password']
            # print(name)
            pack = f"{face},{name},{gender},{password}"
            # print(pack)
            pack = pack.split(",")
            return pack
    except Exception as e:
        return False