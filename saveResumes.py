import pickle
import os

# Save resume to a file
def save_resume_pickle(file_path, resume_text):
    with open(file_path, "wb") as file:
        pickle.dump(resume_text, file)

# Load resume from a file
def load_resume_pickle(file_path):
    try:
        with open(file_path, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

# Example usage
file_path = "resume.pkl"
save_resume_pickle(file_path, "This is a sample resume.")
print(load_resume_pickle(file_path))  # Output: This is a sample resume.

# which save slot the user saves the resume to 1, 2, or 3
def save_slot_selection(file_path):
    
    resume_text = read_text_file(file_path)
    save_resume_pickle(file_path, resume_text)

    #print("This is the loaded resume", loaded_resume)
    return load_resume_pickle(file_path)


def read_text_file(file_path):
    try:
        with open(file_path, "rb") as file:  # Open the file in read mode
            content = file.read()  # Read the file's contents
            return content  # Print the file contents to the console
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except IOError:
        print(f"An error occurred while trying to read the file at {file_path}.")

    # lines = []
    # while True:
    #     line = input()
    #     if line == "": # if nothing on the second line then break
    #         break
    #     lines.append(line)
    # return " ".join(lines) # return all lines seperated by a space