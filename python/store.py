# import os

# def main():
#     # Get the user's name
#     name = input("Please enter your name: ")

#     # Get the directory of the Python script
#     script_directory = os.path.dirname(os.path.abspath(__file__))

#     # Create the file path next to the script
#     file_path = os.path.join(script_directory, "user_name.txt")

#     # Write the name to a text file
#     with open(file_path, "w") as file:
#         file.write(name)

#     print("Your name has been stored in a text file next to your Python script.")

# if __name__ == "__main__":
#     main()
# import os
# !==========

# def main():
#     # Get the user's name
#     name = input("Please enter your name: ")

#     # Define the path to the desktop
#     desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

#     # Create the file path
#     file_path = os.path.join(desktop_path, "user_name.txt")

#     # Write the name to a text file
#     with open(file_path, "w") as file:
#         file.write(name)

#     print("Your name has been stored in a text file on your desktop.")

# if __name__ == "__main__":
#     main()

# import tkinter as tk
# import os

# def save_name():
#     name = name_entry.get()
#     file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_name.txt")
#     with open(file_path, "a") as file:
#         file.write(name)
#     result_label.config(text="Your name has been saved.")

# # Create the main application window
# app = tk.Tk()
# app.title("Save Name")

# # Create a label to ask for the name
# name_label = tk.Label(app, text="Please enter your name:")
# name_label.pack()

# # Create an entry field for the name
# name_entry = tk.Entry(app)
# name_entry.pack()

# # Create a button to save the name
# save_button = tk.Button(app, text="Save Name", command=save_name)
# save_button.pack()

# # Create a label to display the result
# result_label = tk.Label(app, text="")
# result_label.pack()

# # Run the application
# app.mainloop()
# ?===========
# import tkinter as tk
# from tkinter import ttk
# import os

# def save_name():
#     name = name_entry.get()
#     file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_name.txt")
#     with open(file_path, "w") as file:
#         file.write(name)
#     result_label.config(text="Your name has been saved.", foreground="green")

# # Create the main application window
# app = tk.Tk()
# app.title("Save Name")
# app.geometry("400x200")

# # Create a frame for input and button
# input_frame = ttk.Frame(app)
# input_frame.pack(pady=20)

# # Create a label to ask for the name
# name_label = ttk.Label(input_frame, text="Please enter your name:", font=("Arial", 12))
# name_label.grid(row=0, column=0, padx=10, pady=10)

# # Create an entry field for the name
# name_entry = ttk.Entry(input_frame, font=("Arial", 12))
# name_entry.grid(row=0, column=1, padx=10, pady=10)

# # Create a button to save the name
# save_button = ttk.Button(input_frame, text="Save Name", command=save_name)
# save_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# # Create a label to display the result
# result_label = ttk.Label(app, text="", font=("Arial", 12))
# result_label.pack()

# # Run the application
# app.mainloop()
# !===========
import tkinter as tk
from tkinter import ttk
import os

def save_name(directory):
    name = name_entry.get()
    file_path = os.path.join(directory, "user_name.txt")
    with open(file_path, "w") as file:
        file.write(name)
    result_label.config(text="Your name has been saved at: " + file_path, foreground="green")

# Create the main application window
app = tk.Tk()
app.title("Save Name")
app.geometry("400x250")

# Create a frame for input and button
input_frame = ttk.Frame(app)
input_frame.pack(pady=20)

# Create a label to ask for the name
name_label = ttk.Label(input_frame, text="Please enter your name:", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field for the name
name_entry = ttk.Entry(input_frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button to save the name
save_button = ttk.Button(input_frame, text="Save Name", command=lambda: save_name(directory_entry.get()))
save_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a label to ask for the directory
directory_label = ttk.Label(app, text="Please enter directory path to save the file:", font=("Arial", 12))
directory_label.pack()

# Create an entry field for the directory
directory_entry = ttk.Entry(app, font=("Arial", 12))
directory_entry.pack()

# Create a label to display the result
result_label = ttk.Label(app, text="", font=("Arial", 12))
result_label.pack()

# Run the application
app.mainloop()
