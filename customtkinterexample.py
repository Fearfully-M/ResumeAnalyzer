import customtkinter as ctk

# Initialize the main application window
root = ctk.CTk()
root.geometry("400x300")

# Create two frames to represent the two columns
frame_left = ctk.CTkFrame(root)
frame_right = ctk.CTkFrame(root)

# Pack the frames side by side
frame_left.pack(side="left", fill="both", expand=True, padx=10, pady=10)
frame_right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Create and pack buttons into the left frame
button1 = ctk.CTkButton(frame_left, text="Button 1")
button2 = ctk.CTkButton(frame_left, text="Button 2")
button1.pack(pady=10, padx=10, fill="x")
button2.pack(pady=10, padx=10, fill="x")

# Create and pack buttons into the right frame
button3 = ctk.CTkButton(frame_right, text="Button 3")
button4 = ctk.CTkButton(frame_right, text="Button 4")
button3.pack(pady=10, padx=10, fill="x")
button4.pack(pady=10, padx=10, fill="x")



# Create three frames
frame_top = ctk.CTkFrame(root, height=200)
frame_middle = ctk.CTkFrame(root, height=200)
frame_bottom = ctk.CTkFrame(root, height=200)

# Pack frames vertically
frame_top.pack(fill="x", side="top", pady=5, padx=5)
frame_middle.pack(fill="x", side="top", pady=5, padx=5)
frame_bottom.pack(fill="x", side="top", pady=5, padx=5)

# Add widgets (example: buttons)
ctk.CTkButton(frame_top, text="Top Button").pack(pady=10)
ctk.CTkButton(frame_middle, text="Middle Button").pack(pady=10)
ctk.CTkButton(frame_bottom, text="Bottom Button").pack(pady=10)

root.mainloop()
