from mainFunctions import extract_keywords, match_keywords, detect_keyword_stuffing

# Get job description from the job listing from the user
def get_job_description():
    print("Paste the job description below (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "": # if nothing on the second line then break
            break
        lines.append(line)
    return " ".join(lines) # return all lines seperated by a space

# Ask for the user's resume
def get_resume():
    print("Paste your resume below. (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "": # if nothing on the second line then break
            break
        lines.append(line)
    return " ".join(lines) # return all lines seperated by a space


# Keep asking user for job description until valid input
while True:
    job_keywords = extract_keywords(get_job_description())

    # if the user didn't input a job description
    if not job_keywords:
        print("Invalid Input. Paste the job description below (press Enter twice when done):")
    else:
        break

# Keep asking user for their resume until valid input
while True:
    resume_text = get_resume()

    # if the user didn't input a resume
    if not resume_text:
        print("Invalid Input. Paste the resume below (press Enter twice when done):")
    else:
        break


# match the keywords in the job description with the keywords in the resume
match_keywordsTuple = match_keywords(resume_text,job_keywords)
print(match_keywords(resume_text,job_keywords))

# Detect if there is any possibe keyword stuffing in the resume
print(detect_keyword_stuffing(resume_text, job_keywords))

# if the user has a high amount of keywords
if match_keywordsTuple[1] > 70:
    s = f"""Your resume has a very high percentage of keywords (Keyword to word ratio: {match_keywordsTuple[1]}%). This might suggest keyword stuffing and could be losing context.")
    print("Use keywords more sparingly and with more context - for example:")
    print("Instead of saying: 'Experienced in Python' give context such as: 'Developed a Python-based automation tool that improved efficiency by 30%'")
    print("Most resumes that are considered have a keyword to word ratio of 50-70%"""

elif match_keywordsTuple[1] < 50:
    s = f"""Your resume has a relatively low number of keywords used compared to the job description. (Keyword to word ratio: {match_keywordsTuple[1]}%)
    Make sure you are marketing your skills effectively. For example instead of saying:
    Responsible for developing backend solutions' you might want to rephrase it as 'Developed backend soltuions using Python and Flask to optimize performance'
    The former has fewer keywords and encapsulates the details of what was done whereas the later succintly describes but includes the actual tools used and what the tools used accomplished whilst leaving the reader wanting to know more."""

elif match_keywordsTuple[1] >= 50 or match_keywordsTuple[1] <= 70:
    s = f"""The ratio of words to keywords used in your resume compared to the job description is excellent.
    Keyword to word ratio: {match_keywordsTuple[1]}%"""
    