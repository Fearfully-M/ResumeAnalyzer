from mainFunctions import extract_keywords, match_keywords, detect_keyword_stuffing
from saveResumes import save_resume_pickle, load_resume_pickle, save_slot_selection, read_text_file
from tkinter import filedialog
import customtkinter as ctk
import os

# Set up the appearance (optional)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main window
root = ctk.CTk()
root.geometry("750x1080")
root.title("Resume Keyword Analyzer")


# Define the function to handle shortcuts
def handle_shortcuts(event):
    textbox = event.widget # get widget that triggered the event
    if isinstance(textbox, ctk.CTkTextbox):
        if event.keysym == "a" and event.state & 0x4:  # Ctrl+A
            textbox.tag_add("sel", "1.0", "end")  # Select all text
            return "break"
        elif event.keysym == "c" and event.state & 0x4:  # Ctrl+C
            if textbox.tag_ranges("sel"):  # Check if text is selected
                root.clipboard_clear()
                root.clipboard_append(textbox.get("sel.first", "sel.last"))
            return "break"
        elif event.keysym == "v" and event.state & 0x4:  # Ctrl+V
            textbox.insert("insert", root.clipboard_get())
            return "break"  


# Create a label for the job description
job_label = ctk.CTkLabel(root, text="Input the Job Description Below:")
job_label.grid(row=0, column=1 , sticky = 'NSEW')

# Create the blank Textbox field with increased height to input job description
jobDescription_textbox = ctk.CTkTextbox(root, height=300, width=500)
jobDescription_textbox.insert("0.0", "Job Description Here...")
jobDescription_textbox.grid(row=1, column=1 , sticky = 'NSEW')

# Create a label for the resume
resume_label = ctk.CTkLabel(root, text="Input the Resume Below:")
resume_label.grid(row=2, column=1 , sticky = 'NSEW')

# Create the blank Textbox to input resume
resume_textbox = ctk.CTkTextbox(root, height=300, width=500)
resume_textbox.insert("0.0", "Resume Here...")
resume_textbox.grid(row=3, column=1 , sticky = 'NSEW')

# Initialize a textbox reference before it is initially made
results_textbox = None

# Bind the shortcuts to both textboxes
for textbox in [jobDescription_textbox, resume_textbox]:
    textbox.bind("<Control-a>", handle_shortcuts)
    textbox.bind("<Control-c>", handle_shortcuts)
    textbox.bind("<Control-v>", handle_shortcuts)

# Define a function to get input from the textbox
def on_submit():
    global results_textbox

    # used to store all error messages to be sent to generated textbox
    error_message = ""

    # if there is an existing textbox then remove it
    if results_textbox:
        results_textbox.destroy()

    job_description = jobDescription_textbox.get("0.0", "end-1c")
    print(f"User entered: {job_description}")

    # check if user didn't leave job description blank
    if not job_description:
        no_job_description = "Invalid Input. Paste the job description\n"
        error_message += no_job_description

    resume_text = resume_textbox.get("0.0","end-1c")
    print(f"User entered: {resume_text}")

    # check if user didn't leave resume textbox blank
    if not resume_text:
        no_resume = "Invalid Input. Paste the resume"
        error_message += no_resume
    
    # Clears text box inputs
    jobDescription_textbox.delete("0.0", "end")
    resume_textbox.delete("0.0", "end")

    # if there is an error let user know program usage
    if error_message:
        # Dynamically create a new textbox
        new_results_textbox = ctk.CTkTextbox(root, height=300, width=500)
        new_results_textbox.insert("0.0", error_message)
        new_results_textbox.grid(row=7, column=1)
        results_textbox = new_results_textbox

    # calculate the resume keywords
    else:
        # extract keywords from job description
        job_keywords = extract_keywords(job_description)

        # match the keywords in the job description with the keywords in the resume
        matched_keywords = match_keywords(resume_text,job_keywords)
        keyword_percentage = matched_keywords[1]
        matched_keywords = matched_keywords[0]

        # Detect if there is any possibe keyword stuffing in the resume
        print(detect_keyword_stuffing(resume_text, job_keywords))
     
        # If there are no keywords between the resume and the job description
        if not matched_keywords:
            matched_keywords = "There are no matched keywords."

        else:
            keywords = (', ').join(set(matched_keywords))
            matched_keywords = "The matched keywords are: " + keywords + "\nThe keyword percentage match is: " + str(keyword_percentage) + "%"

        # if keyword ratio of keywords in job description are high 
        if keyword_percentage > 70:
            s = f"""Your resume has a very high percentage of keywords (Keyword to word ratio: {keyword_percentage}%). This might suggest keyword stuffing and could be losing context.")
                Use keywords more sparingly and with more context - for example:")
                Instead of saying: 'Experienced in Python' give context such as: 'Developed a Python-based automation tool that improved efficiency by 30%'")
                Most resumes that are considered have a keyword to word ratio of 50-70%"""

        # if keyword ratio is low 
        elif keyword_percentage < 50:
                s = f"""Your resume has a relatively low number of keywords used compared to the job description. (Keyword to word ratio: {keyword_percentage}%)
                Make sure you are marketing your skills effectively. For example instead of saying:
                Responsible for developing backend solutions' you might want to rephrase it as 'Developed backend soltuions using Python and Flask to optimize performance'
                The former has fewer keywords and encapsulates the details of what was done whereas the later succintly describes but includes the actual tools used and what the tools used accomplished whilst leaving the reader wanting to know more."""
        
        # if the keyword ratio is good - inbetween 50-70 percent
        else:
            s = f"""The ratio of words to keywords used in your resume compared to the job description is excellent.
                Keyword to word ratio: {keyword_percentage}%"""

        # determine if there is keyword stuffing
        keyword_stuffing = detect_keyword_stuffing(resume_text, job_keywords)
        print(keyword_stuffing)

        stuffed_keywords = (', ').join(keyword_stuffing)
        print(stuffed_keywords)

        if stuffed_keywords:
            # Dynamically create a new textbox
            new_results_textbox = ctk.CTkTextbox(root, height=300, width=500)
            new_results_textbox.insert("0.0", matched_keywords + "\n" + f"The following words might be overused in your resume. {stuffed_keywords}. Make sure to check to see if enough context is given for these keywords.\n" + s)
            new_results_textbox.grid(row=7, column=1)
            results_textbox = new_results_textbox
        
        else:
            # Dynamically create a new textbox
            new_results_textbox = ctk.CTkTextbox(root, height=300, width=500)
            new_results_textbox.insert("0.0", matched_keywords + "\n" + s)
            new_results_textbox.grid(row=7, column=1)
            results_textbox = new_results_textbox


# Add a button to trigger the action
submit_button = ctk.CTkButton(root, text="Submit", command=on_submit)
submit_button.grid(row=6, column=1, sticky = 'W')


# Function to open the file dialog
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))  # Specify allowed file types
    )
    if file_path:  # If a file is selected
        print(f"Selected File: {file_path}")
        label.configure(text=f"Selected: {file_path}") 
    try:
        #load and save resume data
        print("hello")
        selected_resume_file = save_slot_selection(file_path)
        print("world")
        # Clears text box inputs and input the contents of the opened file
        resume_textbox.delete("0.0", "end")
        resume_textbox.insert("0.0", selected_resume_file)

    # if an exception print to screen
    except Exception as e:
        print("exception")
        print(f"Error: {e}")


# Create a button to trigger the file dialog
file_button = ctk.CTkButton(root, text="Select a File", command=select_file)
file_button.grid(row=4, column=1)


# Label to display the selected file
label = ctk.CTkLabel(root, text="No file selected")
label.grid(row=5, column=1)


# Callback function for whe
def select_resume(choice, resume_textbox):
    print(f"Selected Resume: {choice}")

    # Clears text box inputs
    resume_textbox.delete("0.0", "end")
    
    # Getting the absolute path of the current python script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # now append the file name to the absolute path of the python script
    file_path = os.path.join(current_directory , choice)

    # read the resume file contents
    resume_contents = read_text_file(choice)
    resume_textbox.insert("0.0", resume_contents)


# Dropdown menu with options
directory_path = '/home/fearfully_m/Desktop/ResumeAnalyzer/'

# Dropdown menu with options and filter the files to only search for .pkl files
resume_choices = [f for f in os.listdir(directory_path) 
         if os.path.isfile(os.path.join(directory_path, f)) and f.endswith('.pkl')]
dropdown = ctk.CTkOptionMenu(root, values=resume_choices, command = lambda choice: select_resume(choice,resume_textbox))
dropdown.grid(row=6, column=1 ,sticky = 'E')


# Run the main application loop
root.mainloop()