import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re
import string
import random

import requests
import crypto
import json

# info= '[{"web": "example1.com", "email": "user1@example.com", "password": "password1"},{"web": "example2.com", "email": "user2@example.com", "password": "password2"},{"web": "example3.com", "email": "user3@example.com", "password": "password3"},{"web": "example4.com", "email": "user4@example.com", "password": "password4"},{"web": "example5.com", "email": "user5@example.com", "password": "password5"}]'
# data=json.loads(info)
data = ''
loginUrl = 'https://localhost:8080/login'
updateUrl = 'https://localhost:8080/updatedata'
signupUrl = 'https://localhost:8080/signup'
loggedUsername = ''
loggedPassword = ''

def is_strong_password(password):
    # Define criteria
        length_criteria = len(password) >= 8
        uppercase_criteria = bool(re.search(r'[A-Z]', password))
        lowercase_criteria = bool(re.search(r'[a-z]', password))
        digit_criteria = bool(re.search(r'[0-9]', password))
        special_character_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

        # Check if all criteria are met
        if (length_criteria and uppercase_criteria and lowercase_criteria
            and digit_criteria and special_character_criteria):
            return True
        else:
            return False


def makeRequest(url, params, method='get'):
    if method == 'get':
        r = requests.get(url, params=params,verify=False)
    elif method == 'put':
        params['data'] = crypto.encrypt(params['password'], params['data'])
        r = requests.put(url, params=params,verify=False)
    elif method == 'post':
        r = requests.post(url, params=params,verify=False)
    else:
        return "failed"
    response = json.loads(r.content.decode('utf-8'))
    if(response['success']):
        if(response['data'] !=''):
            response['data'] = crypto.decrypt(params['password'], response['data'])
    return response

def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    if password == '':
        password=' '
    if username == '':
        username=' '
    params = {'username': username, 'password': password}
    request = makeRequest(loginUrl, params)
    
    if request['success']:
        messagebox.showinfo("Login Success", "Welcome, " + username + "!")
        global loggedUsername
        global loggedPassword
        global data
        if request['data'] != '':
            data = json.loads(request['data'])
            if type(data) == str:
                data=[]
        loggedUsername = username
        loggedPassword = password
        root.destroy()
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        
        
def signup():
    username = entry_username.get()
    password = entry_password.get()
    if is_strong_password(password):
        params = {'username': username, 'password': password}
        request = makeRequest(signupUrl, params, 'post')
        if request['success']:
            messagebox.showinfo("Signup Success", f"Welcome, {username}!")
            global loggedUsername
            global loggedPassword
            global data
            loggedUsername = username
            loggedPassword = password
            data = []
            root.destroy()
            open_main_window()
        else:
            messagebox.showerror("Signup Failed", "Username already exists")
            entry_username.delete(0, 'end')
            entry_password.delete(0, 'end')
    else:
        messagebox.showerror("Signup Failed", "Password is not strong enough")
        entry_password.delete(0, 'end')
        
        
def generate_hard_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    password += [random.choice(uppercase_letters + lowercase_letters + digits + special_characters) for _ in range(length - 4)]

    random.shuffle(password)
    return ''.join(password)

def fill_entry(entry, value):
    entry.delete(0, 'end')
    entry.insert(0, value)

def add(main_window):
    main_window.destroy()
    add_window = tk.Tk()
    add_window.title("Add Window")
    # Create and place widgets (labels, entry fields, and buttons)
    label_web = tk.Label(add_window, text="Web:")
    label_web.grid(row=0, column=0, padx=10, pady=10)

    entry_web = tk.Entry(add_window)
    entry_web.grid(row=0, column=1, padx=10, pady=10)

    label_email = tk.Label(add_window, text="Email:")
    label_email.grid(row=1, column=0, padx=10, pady=10)

    entry_email = tk.Entry(add_window)
    entry_email.grid(row=1, column=1, padx=10, pady=10)

    label_password = tk.Label(add_window, text="Password:")
    label_password.grid(row=2, column=0, padx=10, pady=10)

    entry_password = tk.Entry(add_window)
    entry_password.grid(row=2, column=1, padx=10, pady=10)

    button_add = tk.Button(add_window, text="Add",
                           command=lambda: save(add_window, entry_web.get(), entry_email.get(), entry_password.get()))
    button_add.grid(row=3, column=0, columnspan=1, pady=10)
    button_random=tk.Button(add_window, text="Random", command=lambda:fill_entry(entry_password, generate_hard_password()))
    button_random.grid(row=3, column=1, columnspan=1, pady=10)
    


def save(add_window, web, email, password):
    global data
    if data == '':
        data = []
    new_item = {"web": web, "email": email, "password": password}
    data.append(new_item)
    params = {'username': loggedUsername, 'password': loggedPassword, 'data': json.dumps(data)}
    request = makeRequest(updateUrl, params, 'put')
    if request['success']:
        messagebox.showinfo("Add Success", "New item added successfully!")
        data = json.loads(request['data'])
        add_window.destroy()  # Close the add window after saving
        open_main_window()  # Reopen the main window to reflect the changes
    else:
        messagebox.showerror("Add Failed", "Failed to add new item")
        add_window.destroy()  # Close the add window after saving


def open_main_window():
    main_window = tk.Tk()
    main_window.title("Main Window")

    web_label = tk.Label(main_window, text="Webite")
    web_label.grid(row=0, column=0)

    email_label = tk.Label(main_window, text="Email")
    email_label.grid(row=0, column=1)

    password_label = tk.Label(main_window, text="Password")
    password_label.grid(row=0, column=2)

    # parse json
    for idx, item in enumerate(data):
        data_string1 = tk.StringVar()
        data_string1.set(f"{item['web']}")
        ent = tk.Entry(main_window, textvariable=data_string1, fg="black", bg="white", bd=0, state="readonly",
                       width=len(data_string1.get()) + 10)
        ent.grid(row=idx + 1, column=0)
        data_string2 = tk.StringVar()
        data_string2.set(f"{item['email']}")
        ent = tk.Entry(main_window, textvariable=data_string2, fg="black", bg="white", bd=0, state="readonly",
                       width=len(data_string2.get()) + 10)
        ent.grid(row=idx + 1, column=1)
        data_string3 = tk.StringVar()
        data_string3.set(f"{item['password']}")
        ent = tk.Entry(main_window, textvariable=data_string3, fg="black", bg="white", bd=0, state="readonly",
                       width=len(data_string3.get()) + 10)
        ent.grid(row=idx + 1, column=2)
    tk.Button(main_window, text="Add", command=lambda: add(main_window)).grid(row=len(data) + 1, columnspan=3, padx=10,pady=10)
    label_welcome = tk.Label(main_window, text="Welcome to the Main Window!")
    # label_welcome.pack(padx=10, pady=10)

    # Add more widgets and functionalities to the main window as needed

    # Run the Tkinter event loop for the main window
    main_window.mainloop()
    


# Create the main login window
root = tk.Tk()
root.title("Login Screen")

# Create and place widgets (labels, entry fields, and buttons)
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")  # Entry field with hidden input (password)
entry_password.grid(row=1, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password must be at least 8 characters long\ncontain at least one uppercase letter\n one lowercase letter one digit, and one special character.")
label_password.grid(row=2, column=0, columnspan=2, padx=10, pady=3)

button_login = tk.Button(root, text="Login", command=validate_login)
button_login.grid(row=3, column=0, columnspan=1, pady=10)

button_signup = tk.Button(root, text="Sign Up", command=signup)
button_signup.grid(row=3, column=1, columnspan=1, pady=10,padx=10)

# Run the Tkinter event loop for the login window
root.mainloop()
