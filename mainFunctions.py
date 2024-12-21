import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# libaries of word data
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

def extract_keywords(job_description):
    """Extracts keywords from a job description and removes 'stop words' that don't add value"""
    stop_words = set(stopwords.words("english")) # Set the language to look for 'stop words' 
    words = word_tokenize(job_description) # tokenize or split words up into individual elements in a list

    # Get only the keywords in the description - according to NLTK
    keywords = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    return keywords


def match_keywords(resume_text, job_keywords):
    """Matches keywords from the resume with the keywords in the job description"""

    # Tokenize words in the resume and set all words to lower
    resume_words = set(word_tokenize(resume_text.lower()))

    # find if there are any matches in the resume with the job keywords and set them to the matches list
    matches = [keyword for keyword in job_keywords if keyword.lower() in resume_words]

    # Return the keywords as well as a value of the percentage of words that matched the keywords
    return matches, round(len(matches) / len(job_keywords) * 100, 2)


def detect_keyword_stuffing(resume_text, job_keywords):
    excessive_repeats = {keyword: resume_text.lower().count(keyword.lower()) for keyword in job_keywords}

    return {keyword: count for keyword, count in excessive_repeats.items() if count > 5} 













# used only for automation later in project
def get_job_description(method="user_input", source=None):
    if method == "user_input":
        return get_job_description_user_input()
    elif method == "api":
        return fetch_job_description_via_api(source)
    elif method == "scraping":
        return scrape_job_description(source)
    else:
        raise ValueError("Invalid method specified.")