from mainFunctions import extract_keywords, match_keywords, detect_keyword_stuffing

def get_job_description():
    print("Paste the job description below (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "": # if nothing on the second line then break
            break
        lines.append(line)
    return " ".join(lines) # return all lines seperated by a space

def get_resume():
    print("Paste your resume below. (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "": # if nothing on the second line then break
            break
        lines.append(line)
    return " ".join(lines) # return all lines seperated by a space

job_keywords = extract_keywords(get_job_description())

resume_text = get_resume()

# match the keywords in the job description with the keywords in the resume
# match_keywords(resume_keywords,job_keywords)

# Detect if there is any possibe keyword stuffing in the resume
print(detect_keyword_stuffing(resume_text, job_keywords))

