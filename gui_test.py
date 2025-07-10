import tkinter as tk
import threading
from pippa import command

def close_program(root):
    root.quit()

def gui(name, gender):
    root = tk.Tk()
    root.title("SRIshti AI For college Project- ONLINE")
    root.configure(bg="#85929E")
    root.protocol("WM_DELETE_WINDOW", close_program(root))
    head_lable = tk.Label(root, text="🤖SRIshti", font=("Arial", 120, "bold"), background="#85929E", fg="#117A65")
    head_lable.pack(side=tk.TOP, fill="both")
    centerFrame = tk.Label(root, bd=0)
    centerFrame.pack(fill='both', expand=True)
    scrollbar = tk.Scrollbar(centerFrame)
    scrollbar.pack(side='right', fill='y')
    textarea = tk.Text(centerFrame, font=('Arial', 15, 'bold'), height=10, yscrollcommand=scrollbar.set,
                       wrap='word', background="#283747", fg="white", pady=4, padx=4, bd=0)
    textarea.pack(side=tk.LEFT, fill="both", expand=True)
    scrollbar.config(command=textarea.yview)
    bottom_lable = tk.Label(root, text="welcome", font=("Arial", 15, "bold"), background="white", fg="black")
    bottom_lable.pack(side=tk.BOTTOM, fill="both")
    threading.Thread(target=command, args=(root, head_lable, textarea, bottom_lable, name, gender)).start()
    root.mainloop()

# gui("Arnab", "Male")