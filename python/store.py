import tkinter as tk
from tkinter import ttk, messagebox
import os
# hello 
# -sdfs
def save_name():
    name = name_entry.get().strip()
    directory = directory_entry.get().strip()
    
    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return
    
    if not directory:
        messagebox.showerror("Error", "Please enter directory path to save the file.")
        return
    
    file_path = os.path.join(directory, "user_name.txt")
    try:
        with open(file_path, "w") as file:
            file.write(name)
        result_label.config(text="Your name has been saved at: " + file_path, foreground="green")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
app = tk.Tk()
app.title("Save Name")
app.geometry("450x300")
app.resizable(False, False)

# Styling
app.style = ttk.Style()
app.style.theme_use("clam")
app.style.configure("TLabel", foreground="white", background="#333333", font=("Arial", 12))
app.style.configure("TEntry", foreground="#333333", font=("Arial", 12))
app.style.configure("TButton", foreground="white", background="#007bff", font=("Arial", 12), padding=5)
app.style.map("TButton", background=[("active", "#0056b3")])

# Create a frame for input and button
input_frame = ttk.Frame(app, style="TFrame")
input_frame.pack(pady=20)

# Create a label to ask for the name
name_label = ttk.Label(input_frame, text="Please enter your name:", style="TLabel")
name_label.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field for the name
name_entry = ttk.Entry(input_frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label to ask for the directory
directory_label = ttk.Label(input_frame, text="Please enter directory path to save the file:", style="TLabel")
directory_label.grid(row=1, column=0, padx=10, pady=10)

# Create an entry field for the directory
directory_entry = ttk.Entry(input_frame, font=("Arial", 12))
directory_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a button to save the name
save_button = ttk.Button(input_frame, text="Save Name", command=save_name, style="TButton")
save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Create a label to display the result
result_label = ttk.Label(app, text="", style="TLabel")
result_label.pack()

# Run the application
app.mainloop()
