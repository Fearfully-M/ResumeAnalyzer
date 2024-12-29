import customtkinter as ctk

# Initialize CustomTkinter
ctk.set_appearance_mode("System")  # Can be "Dark", "Light" or "System"
ctk.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"

# Create the main application window
app = ctk.CTk()
app.geometry("300x200")
app.title("Resume Selector")

# Callback function for when an option is selected
def select_resume(choice):
    print(f"Selected Resume: {choice}")

# Dropdown menu with options
resume_choices = ["Resume 1", "Resume 2", "Resume 3"]
dropdown = ctk.CTkOptionMenu(app, values=resume_choices, command=select_resume)
dropdown.pack(pady=20)

# Set a default value for the dropdown
dropdown.set("Select a Resume")  # Placeholder text

# Run the application
app.mainloop()
