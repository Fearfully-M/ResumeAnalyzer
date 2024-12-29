import customtkinter as ctk
from tkinter import filedialog

# Initialize CustomTkinter
ctk.set_appearance_mode("System")  # Can be "Dark", "Light" or "System"
ctk.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"

# Create the main application window
app = ctk.CTk()
app.geometry("400x200")
app.title("File Selector")

# Function to open the file dialog
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))  # Specify allowed file types
    )
    if file_path:  # If a file is selected
        print(f"Selected File: {file_path}")
        label.configure(text=f"Selected: {file_path}")

# Create a button to trigger the file dialog
file_button = ctk.CTkButton(app, text="Select a File", command=select_file)
file_button.pack(pady=20)

# Label to display the selected file
label = ctk.CTkLabel(app, text="No file selected")
label.pack(pady=10)

# Run the application
app.mainloop()
