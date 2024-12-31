# Resume Keyword Analyzer

## Overview

The goal of this project was to enhance familiarity with Python and explore a couple of Python libraries through the development of a practical application.

**Resume Keyword Analyzer** is designed to help users optimize their resumes for specific job descriptions. It simplifies the process of identifying keyword matches between a resume and a job description, enabling users to refine their resumes to better align with individual job postings.

---

## Features

- **Keyword Matching:** Calculates the number of keywords in a resume relative to the keywords in a job description.
- **Resume Input Options:**
    - Copy and paste the resume into a text box for immediate analysis.
    - Open a `.txt` file of a resume to automatically save and display it in the resume text box.
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
2. Run the application:
    
    ```bash
    py main.py
    ```
    
3. Once the program launches:
    - Input a job description of your choice into the **Job Description** text box.
    - Use one of the following methods to input your resume:
        - Copy and paste your resume into the **Resume** text box.
        - Open a `.txt` file of your resume using the **Open File** option, which will automatically save and populate your resume in the text box.
    - Click the **Calculate** button to determine the number of matching keywords between the job description and your resume.

---

## Libraries Used

- [**CustomTkinter](https://github.com/TomSchimansky/CustomTkinter):** For creating the user interface.
- [**nltk](https://www.nltk.org/):** For processing text, including determining keywords and stopwords.

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

Let me know if you'd like any adjustments or additions!