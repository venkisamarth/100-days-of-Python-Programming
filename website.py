import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import csv
import os

# Function for admin registration screen
def admin_registration_screen():
    admin_register_window = tk.Toplevel(root)
    admin_register_window.title("Admin Registration")
    admin_register_window.configure(bg="#e6f7ff")

    tk.Label(admin_register_window, text="Admin ID", bg="#e6f7ff").pack()
    reg_admin_userid = tk.Entry(admin_register_window)
    reg_admin_userid.pack()

    tk.Label(admin_register_window, text="Password", bg="#e6f7ff").pack()
    reg_admin_password = tk.Entry(admin_register_window, show="*")
    reg_admin_password.pack()

    def register_admin():
        admin_userid = reg_admin_userid.get()
        admin_password = reg_admin_password.get()
        # Save the admin data in a CSV file
        with open('admins.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([admin_userid, admin_password])
        messagebox.showinfo("Registration", "Admin Registered Successfully!")

    tk.Button(admin_register_window, text="Register", command=register_admin, bg="#1f77b4", fg="white").pack(pady=10)

# Function for admin login screen
def admin_login_screen():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Login")
    admin_window.configure(bg="#e6f7ff")

    tk.Label(admin_window, text="User ID", bg="#e6f7ff").pack()
    admin_userid = tk.Entry(admin_window)
    admin_userid.pack()

    tk.Label(admin_window, text="Password", bg="#e6f7ff").pack()
    admin_password = tk.Entry(admin_window, show="*")
    admin_password.pack()

    def admin_login():
        user_id = admin_userid.get()
        password = admin_password.get()
        # Admin login logic
        if user_id == "admin" and password == "admin123":
            messagebox.showinfo("Login", "Admin Login Successful!")
        else:
            messagebox.showerror("Login", "Invalid Admin Credentials")

    tk.Button(admin_window, text="Login", command=admin_login, bg="#1f77b4", fg="white").pack(pady=10)

# Function for user login screen
def user_login_screen():
    user_window = tk.Toplevel(root)
    user_window.title("User Login")
    user_window.configure(bg="#e6ffe6")

    tk.Label(user_window, text="User ID", bg="#e6ffe6").pack()
    user_userid = tk.Entry(user_window)
    user_userid.pack()

    tk.Label(user_window, text="Password", bg="#e6ffe6").pack()
    user_password = tk.Entry(user_window, show="*")
    user_password.pack()

    def user_login():
        user_id = user_userid.get()
        password = user_password.get()
        # User login logic
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == user_id and row[3] == password:
                    messagebox.showinfo("Login", "User Login Successful!")
                    return
            messagebox.showerror("Login", "Invalid User Credentials")

    tk.Button(user_window, text="Login", command=user_login, bg="#1f77b4", fg="white").pack(pady=10)

# Function for user registration screen
def user_registration_screen():
    register_window = tk.Toplevel(root)
    register_window.title("User Registration")
    register_window.configure(bg="#ffffe6")

    tk.Label(register_window, text="Name", bg="#ffffe6").pack()
    reg_name = tk.Entry(register_window)
    reg_name.pack()

    tk.Label(register_window, text="Phone Number", bg="#ffffe6").pack()
    reg_phone = tk.Entry(register_window)
    reg_phone.pack()

    tk.Label(register_window, text="User ID", bg="#ffffe6").pack()
    reg_userid = tk.Entry(register_window)
    reg_userid.pack()

    tk.Label(register_window, text="Password", bg="#ffffe6").pack()
    reg_password = tk.Entry(register_window, show="*")
    reg_password.pack()

    def register_user():
        name = reg_name.get()
        phone = reg_phone.get()
        user_id = reg_userid.get()
        password = reg_password.get()
        # Save the user data in a CSV file
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, user_id, password])
        messagebox.showinfo("Registration", "User Registered Successfully!")

    tk.Button(register_window, text="Register", command=register_user, bg="#1f77b4", fg="white").pack(pady=10)

# Function for resume upload screen
def resume_upload_screen():
    upload_window = tk.Toplevel(root)
    upload_window.title("Resume Upload")
    upload_window.configure(bg="#ffe6e6")

    tk.Label(upload_window, text="Upload Resume", bg="#ffe6e6").pack()
    resume_text = scrolledtext.ScrolledText(upload_window, width=40, height=10)
    resume_text.pack()

    def browse_resume():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                resume_text.insert(tk.END, file.read())

    def save_resume():
        resume_data = resume_text.get("1.0", tk.END)
        with open('resume.txt', 'w') as file:
            file.write(resume_data)
        messagebox.showinfo("Upload", "Resume Uploaded Successfully!")

    tk.Button(upload_window, text="Browse", command=browse_resume, bg="#1f77b4", fg="white").pack(pady=5)
    tk.Button(upload_window, text="Upload", command=save_resume, bg="#1f77b4", fg="white").pack(pady=5)

# Main application
def show_admin_registration():
    admin_registration_screen()

def show_admin_login():
    admin_login_screen()

def show_user_login():
    user_login_screen()

def show_user_registration():
    user_registration_screen()

def show_resume_upload():
    resume_upload_screen()

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Login System")
root.configure(bg="#f0f0f0")

tk.Button(root, text="Admin Registration", command=show_admin_registration, bg="#0000ff", fg="white").pack(pady=10)
tk.Button(root, text="Admin Login", command=show_admin_login, bg="#0000ff", fg="white").pack(pady=10)
tk.Button(root, text="User Login", command=show_user_login, bg="#0000ff", fg="white").pack(pady=10)
tk.Button(root, text="User Registration", command=show_user_registration, bg="#0000ff", fg="white").pack(pady=10)
tk.Button(root, text="Resume Upload", command=show_resume_upload, bg="#0000ff", fg="white").pack(pady=10)
tk.Button(root, text="Exit", command=exit_app, bg="#ff0000", fg="white").pack(pady=10)

root.mainloop()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

resumeDataSet = pd.read_csv('UpdatedResumeDataSet.csv' ,encoding='utf-8')
resumeDataSet['cleaned_resume'] = ''
resumeDataSet.head()
print ("Displaying the distinct categories of resume -")
print (resumeDataSet['Category'].unique())
print ("Displaying the distinct categories of resume and the number of records belonging to each category -")
print (resumeDataSet['Category'].value_counts())
import seaborn as sns
plt.figure(figsize=(15,15))
plt.xticks(rotation=90)
sns.countplot(y="Category", data=resumeDataSet)
plt.show()

from matplotlib.gridspec import GridSpec
targetCounts = resumeDataSet['Category'].value_counts()
targetLabels  = resumeDataSet['Category'].unique()
# Make square figures and axes
plt.figure(1, figsize=(25,25))
the_grid = GridSpec(2, 2)



cmap = plt.get_cmap('coolwarm')
colors = [cmap(i) for i in np.linspace(0, 1, 3)]
plt.subplot(the_grid[0, 1], aspect=1, title='CATEGORY DISTRIBUTION')
source_pie = plt.pie(targetCounts, labels=targetLabels, autopct='%1.1f%%', shadow=True, colors=colors)
plt.show()
