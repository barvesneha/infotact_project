from tkinter import *
from tkinter import messagebox


users = {"admin": "admin123", "user1": "password1"}

def open_login_window(parent):
    login_win = Toplevel(parent)
    login_win.geometry("400x250")  
    login_win.title("User Login / Registration")
    login_win['bg'] = 'lightblue'
    
    
    login_win.grab_set()
    
   
    login_win.authenticated = False
    
    Label(login_win, text="User Login", font="Arial 14 bold", bg='lightblue').pack(pady=5)
    
    
    Label(login_win, text="Username", font="arial 12", bg='lightblue').pack(pady=5)
    username_entry = Entry(login_win, width=30)
    username_entry.pack(pady=5)
    
    
    Label(login_win, text="Password", font="arial 12", bg='lightblue').pack(pady=5)
    password_entry = Entry(login_win, show="*", width=30)
    password_entry.pack(pady=5)
    
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username in users and users[username] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            login_win.authenticated = True
            login_win.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def register():
        username = username_entry.get()
        password = password_entry.get()
        if username in users:
            messagebox.showerror("Registration Failed", "Username already exists")
        else:
            users[username] = password
            messagebox.showinfo("Registration Successful", f"User {username} registered successfully")
    
   
    Button(login_win, text="Login", command=login, bg="green", fg="white", width=10).pack(pady=5)
    Button(login_win, text="Register", command=register, bg="blue", fg="white", width=10).pack(pady=5)
    
    return login_win
