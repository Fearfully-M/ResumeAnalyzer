# Resume Keyword Analyzer
    #### Video Demo:  https://www.youtube.com/watch?v=KU7oCgp5U6k
    #### Description: A Python application that determines the ratio of keywords from a job description compared to a user's resume text file

## Overview

The goal of this project was to enhance familiarity with Python and explore a couple of Python libraries through the development of a practical application.

**Resume Keyword Analyzer** is designed to help users optimize their resumes for specific job descriptions. It simplifies the process of identifying keyword matches between a resume and a job description, enabling users to refine their resumes to better align with individual job postings.

---

## Features

- **Keyword Matching:** Calculates the number of keywords in a resume relative to the keywords in a job description.
- **Keyword Finder:** Quickly and simply show ONLY the keywords in a job description.
- **Resume Input Options:**
    - Copy and paste the resume into a text box for immediate analysis of keybwords.
    - Open a `.txt` file of a resume to automatically save and display it in the resume text box. (requires a reload to display the resume)
- **Resume Saving:** Saves resumes for reuse without needing to re-enter them manually.
- **Keyboard Shortcuts:** Quickly copy and paste job descriptions with built-in shortcuts.

---

## Installation

1. Clone the repository:
    
    ```bash
    git clone https://github.com/Fearfully-M/ResumeAnalyzer.git
    
    ```
    
2. Install the required dependencies:
    
    ```bash
    pip install -r requirements.txt
    
    ```

---

## Usage

1. Navigate to the project's main directory in your terminal. 

**The parent directory's name must remain as '*ResumeAnalyzer*' for the application to function.**

2. Run the application:
    
    ```bash
    python3 main.py
    ```
    
3. Once the program launches:
    - Input a job description of your choice into the **Job Description** text box.
    - Use one of the following methods to input your resume:
        - Copy and paste your resume into the **Resume** text box.
        - Open a `.txt` file of your resume using the **Select a File** option, which will automatically save and populate your resume in the text box upon reload.
         - Click the **Select a Resume** dropdown menu to load a resume that was uploaded via the **Select a File** option.
    - Click the **Calculate** button to determine the number of matching keywords between the job description and your resume.
    - Click the **Job Description Keywords** button to determine what the keywords are in a job description

---

## Libraries Used

- [**CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** For creating the user interface.
- [**nltk](https://www.nltk.org/):** For processing text, including determining keywords and stopwords.
- [**pickle](https://www.nltk.org/):** For saving and allowing the use of already uploaded resumes in a .txt file format

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are welcome and appreciated!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions, feedback, or collaboration opportunities, feel free to reach out at [https://github.com/Fearfully-M].

---

Feel free to let me know if you'd like any adjustments or have any suggestions - there are no plans to actively maintain this project. 

## Appreciation

A special thanks to the CS50 team for teaching this class and providing the opportunity to learn from world-class leaders regardless of location, financial situation, or status. It really cannot be stated enough how much of an opportunity this is and how this is potentially life changing to thousands of people. Thank you so much.