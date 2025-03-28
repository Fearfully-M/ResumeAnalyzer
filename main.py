from mainFunctions import extract_keywords, match_keywords, detect_keyword_stuffing
from saveResumes import save_resume_pickle, load_resume_pickle, save_slot_selection, read_text_file
from tkinter import filedialog
import customtkinter as ctk
import os

# used so that the relative path is found for 'ResumeAnalyzer' on any user's machine
from pathlib import Path

# Global widget variables
root = None
jobDescription_textbox = None
resume_textbox = None
results_textbox = None
label = None

# Define the function to handle shortcuts
def handle_shortcuts(event):
    textbox = event.widget  # Get the widget that triggered the event
    if event.keysym == "a" and event.state & 0x4:  # Ctrl+A
        textbox.tag_add("sel", "1.0", "end")  # Select all text
        return "break"
    elif event.keysym == "c" and event.state & 0x4:  # Ctrl+C
        if textbox.tag_ranges("sel"):  # Check if text is selected
            root.clipboard_clear()
            root.clipboard_append(textbox.get("sel.first", "sel.last"))
        return "break"
    elif event.keysym == "v" and event.state & 0x4:  # Ctrl+V
        try:
            textbox.insert("insert", root.clipboard_get())
        except Exception as e:
            print(f"Clipboard error: {e}")
        return "break"

# Define a function to get input from the textbox
def on_submit():

    global results_textbox, jobDescription_textbox, resume_textbox

    # used to store all error messages to be sent to generated textbox
    error_message = ""

    # if there is an existing textbox then remove it
    if results_textbox:
        results_textbox.destroy()

    job_description = jobDescription_textbox.get("0.0", "end-1c")
    print(f"User entered: {job_description}")

    # check if user didn't leave job description blank
    if not job_description.strip():
        error_message += "Invalid Input. Paste the job description\n"

    resume_text = resume_textbox.get("0.0", "end-1c")
    print(f"User entered: {resume_text}")

    # check if user didn't leave resume textbox blank
    if not resume_text.strip():
        error_message += "Invalid Input. Paste the resume"

    # Clears text box inputs
    jobDescription_textbox.delete("0.0", "end")
    resume_textbox.delete("0.0", "end")


    # if there is an error let user know program usage
    if error_message:
        # Dynamically create a new textbox
        new_results_textbox = ctk.CTkTextbox(root, height=300, width=500)
        new_results_textbox.insert("0.0", error_message)
        new_results_textbox.grid(row=9, column=2)
        results_textbox = new_results_textbox

    # calculate the resume keywords
    else:

        # extract keywords from job description
        job_keywords = extract_keywords(job_description)

        # match the keywords in the job description with the keywords in the resume
        matched_keywords = match_keywords(resume_text, job_keywords)
        keyword_percentage = matched_keywords[1]
        matched_keywords = matched_keywords[0]

        # Detect if there is any possibe keyword stuffing in the resume
        # print(detect_keyword_stuffing(resume_text, job_keywords))
        
        # If there are no keywords between the resume and the job description
        if not matched_keywords:
            matched_keywords = "There are no matched keywords."
        else:
            keywords = ', '.join(set(matched_keywords))
            matched_keywords = f"The matched keywords are: {keywords}\nThe keyword percentage match is: {keyword_percentage}%"

        # if keyword ratio of keywords in job description are high
        if keyword_percentage > 70:
            s = f"Your resume has a very high percentage of keywords\n (Keyword to word ratio: {keyword_percentage}%). This might suggest keyword stuffing and could be losing context. Use keywords more sparingly and with more context - for example: Instead of saying: 'Experienced in Python' give context such as: 'Developed a Python-based automation tool that improved efficiency by 30%'. Most resumes that are considered have a keyword to word ratio of 50-70% \n"

        # if keyword ratio is low
        elif keyword_percentage < 50:
            s = f"Your resume has a relatively low number of keywords used compared to the job description. (Keyword to word ratio: {keyword_percentage}%) Make sure you are marketing your skills effectively. For example instead of saying: 'Responsible for developing backend solutions' you might want to rephrase it as 'Developed backend solutions using Python and Flask to optimize performance'. The former has fewer keywords and encapsulates the details of what was done whereas the latter succinctly describes but includes the actual tools used and what the tools accomplished whilst leaving the reader wanting to know more. \n"

        # if the keyword ratio is good - inbetween 50-70 percent
        else:
            s = f"The ratio of words to keywords used in your resume compared to the job description is excellent. Keyword to word ratio: {keyword_percentage}% \n"
        
        # determine if there is keyword stuffing
        keyword_stuffing = detect_keyword_stuffing(resume_text, job_keywords)
        #print(keyword_stuffing)
        stuffed_keywords = ', '.join(keyword_stuffing)
        #print(stuffed_keywords)

        if stuffed_keywords:
            # Dynamically create a new textbox
            new_results_textbox = ctk.CTkTextbox(root, height=300, width=500)
            new_results_textbox.insert("0.0", f"{matched_keywords}\nThe following words might be overused in your resume: {stuffed_keywords}. Make sure to check if enough context is given for these keywords.\n{s}")
            new_results_textbox.grid(row=9, column=2, sticky="S")
            results_textbox = new_results_textbox

        else:
            # Dynamically create a new textbox
            new_results_textbox = ctk.CTkTextbox(root, height=300, width=500)
            new_results_textbox.insert("0.0", f"{matched_keywords}\n{s}")
            new_results_textbox.grid(row=9, column=2, sticky="S")
            results_textbox = new_results_textbox

def job_description_keywords():

    global results_textbox, jobDescription_textbox

    # get job description
    job_description = jobDescription_textbox.get("0.0", "end-1c")

    # collect keywords from job description
    job_keywords = extract_keywords(job_description)

    # if there is nothing in the job description textbox
    if not job_keywords:
        job_keywords = "There are no keywords."

    # if user tries to calculate with the default "Job Description Here..." string default
    elif job_keywords[0] == 'Job' and job_keywords[1] == 'Description':
        job_keywords = "Enter in a job description."

    else:
        job_keywords = ', '.join(job_keywords)

    # recreate the textbox dynamically
    new_results_textbox = ctk.CTkTextbox(root, height=300, width=500)
    new_results_textbox.insert("0.0", job_keywords)
    new_results_textbox.grid(row=9, column=2, sticky="S")
    results_textbox = new_results_textbox

# Function to open the file dialog
def select_file():
    global resume_textbox, label
    file_path = filedialog.askopenfilename(
        title="Select a File",
        # Specify allowed file types
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path: # If a file is selected
        print(f"Selected File: {file_path}")
        label.configure(text=f"Selected: {file_path}")
        try:
            # load and save resume data
            selected_resume_file = save_slot_selection(file_path)

            # Clears text box inputs and input the contents of the opened file
            resume_textbox.delete("0.0", "end")
            resume_textbox.insert("0.0", selected_resume_file)

        # if an exception print to screen
        except Exception as e:
            print(f"Error: {e}")

# Callback function for when user selects an uploaded resume
def select_resume(choice):

    global resume_textbox

    print(f"Selected Resume: {choice}")

    # Clears text box inputs
    resume_textbox.delete("0.0", "end")

    # Getting the absolute path of the current python script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # now append the file name to the absolute path of the python script
    file_path = os.path.join(current_directory, choice)

    # read the resume file contents
    resume_contents = load_resume_pickle(choice)
    resume_textbox.insert("0.0", resume_contents)

def main():
    global root, jobDescription_textbox, resume_textbox, results_textbox, label

    # Set up the appearance (optional)
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    # Create the main window
    root = ctk.CTk()
    root.geometry("750x1080")
    root.title("Resume Keyword Analyzer")

    # Blank column so that widgets start in the second (or middle) column on the screen
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)

    # Create a label for the job description
    job_label = ctk.CTkLabel(root, text="Input the Job Description Below:")
    job_label.grid(row=0, column=2, sticky='NSEW')

    # Create the blank Textbox field with increased height to input job description
    jobDescription_textbox = ctk.CTkTextbox(root, height=300, width=500)
    jobDescription_textbox.insert("0.0", "Job Description Here...")
    jobDescription_textbox.grid(row=1, column=2, sticky='E')

    # Create a label for the resume
    resume_label = ctk.CTkLabel(root, text="Input the Resume Below:")
    resume_label.grid(row=2, column=2, sticky='NSEW')

    # Create the blank Textbox to input resume
    resume_textbox = ctk.CTkTextbox(root, height=300, width=500)
    resume_textbox.insert("0.0", "Resume Here...")
    resume_textbox.grid(row=3, column=2, sticky='E')

    # Initialize a textbox reference before it is initially made
    results_textbox = None

    # Bind the shortcuts to both textboxes
    for textbox in [jobDescription_textbox, resume_textbox]:
        textbox.bind("<Control-a>", handle_shortcuts)
        textbox.bind("<Control-c>", handle_shortcuts)
        textbox.bind("<Control-v>", handle_shortcuts)

    # Add a button to trigger the action
    submit_button = ctk.CTkButton(root, text="Calculate", fg_color="#1f6aa5",
                                  text_color="white", hover_color="red", command=on_submit)
    submit_button.grid(row=7, column=2, sticky='W')

    # Add a button to trigger the action
    determine_keywords = ctk.CTkButton(root, text="Job Description Keywords", fg_color="#1f6aa5",
                                       text_color="white", hover_color="red", command=job_description_keywords)
    determine_keywords.grid(row=8, column=2, sticky='S', pady=10)

    # Create a button to trigger the file dialog
    file_button = ctk.CTkButton(root, text="Select a File", command=select_file, hover_color="red")
    file_button.grid(row=7, column=2)

    # Label to display the selected file
    label = ctk.CTkLabel(root, text="No file selected")
    label.grid(row=6, column=2)

    # Get the absolute path of the script's directory
    script_dir = Path(__file__).resolve().parent

    # Find 'ResumeAnalyzer' directory by looking for it in the path hierarchy
    while script_dir.name != 'ResumeAnalyzer' and script_dir != script_dir.parent:
        script_dir = script_dir.parent
    
    # Set the directory path to the absolute path of the file location plus the parent directory 'ResumeAnalyzer'
    directory_path = script_dir

    # Create a StringVar to assign a default value for the dropdown menu
    selected_option = ctk.StringVar(value="Select a Resume")  # Default value

    # Dropdown menu with options and filter the files to only search for .pkl files
    resume_choices = [f for f in os.listdir(directory_path)
                      if os.path.isfile(os.path.join(directory_path, f)) and f.endswith('.pkl')]
    dropdown = ctk.CTkOptionMenu(root, variable=selected_option, values=resume_choices,
                                 command=lambda choice: select_resume(choice))
    dropdown.grid(row=7, column=2, sticky='E')

    # Label to display the dropdown
    label_dropdown = ctk.CTkLabel(root, text="Saved Resumes")
    label_dropdown.grid(row=6, column=2, sticky='E')

    # Run the main application loop
    root.mainloop()

if __name__ == "__main__":
    main()