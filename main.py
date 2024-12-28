from mainFunctions import extract_keywords, match_keywords, detect_keyword_stuffing
import customtkinter as ctk

# Set up the appearance (optional)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main window
root = ctk.CTk()
root.geometry("750x1080")
root.title("Resume Keyword Analyzer")

# Create a label for the job description
job_label = ctk.CTkLabel(root, text="Input the Job Description Below:")
job_label.pack(pady=10)

# Create the blank Textbox field with increased height to input job description
jobDescription_textbox = ctk.CTkTextbox(root, height=300, width=500)
jobDescription_textbox.insert("0.0", "Job Description Here...")
jobDescription_textbox.pack(pady=10, padx=20)

# Create a label for the resume
resume_label = ctk.CTkLabel(root, text="Input the Resume Below:")
resume_label.pack(pady=10)

# Create the blank Textbox to input resume
resume_textbox = ctk.CTkTextbox(root, height=300, width=500)
resume_textbox.insert("0.0", "Resume Here...")
resume_textbox.pack(pady=10, padx=20)


# Initialize a textbox reference before it is initially made
results_textbox = None

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
        new_results_textbox = ctk.CTkTextbox(root, height=200, width=300)
        new_results_textbox.insert("0.0", error_message)
        new_results_textbox.pack(pady=10, padx=20)
        results_textbox = new_results_textbox

    # calculate the resume keywords
    else:
        # extract keywords from job description
        job_keywords = extract_keywords(job_description)

        # match the keywords in the job description with the keywords in the resume
        matched_keywords = match_keywords(resume_text,job_keywords)
        keyword_percentage = matched_keywords[1]
        matched_keywords = matched_keywords[0]
        
        #print(match_keywords(resume_text,job_keywords))

        # Detect if there is any possibe keyword stuffing in the resume
        print(detect_keyword_stuffing(resume_text, job_keywords))
        
        # If there are no keywords between the resume and the job description
        if not matched_keywords:
            matched_keywords = "There are no matched keywords."

        else:
            keywords = (', ').join(set(matched_keywords))
            matched_keywords = "The matched keywords are: \n" + keywords + " The keyword percentage match is: " + str(keyword_percentage) + "%"

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
            new_results_textbox = ctk.CTkTextbox(root, height=200, width=300)
            new_results_textbox.insert("0.0", matched_keywords + "/n" + f"The following words might be overused in your resume. {stuffed_keywords}. Make sure to check to see if enough context is given for these keywords.")
            new_results_textbox.pack(pady=10, padx=20)
            results_textbox = new_results_textbox
        
        else:
            # Dynamically create a new textbox
            new_results_textbox = ctk.CTkTextbox(root, height=200, width=300)
            new_results_textbox.insert("0.0", matched_keywords + "/n")
            new_results_textbox.pack(pady=10, padx=20)
            results_textbox = new_results_textbox



# Add a button to trigger the action
submit_button = ctk.CTkButton(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Run the main application loop
root.mainloop()
