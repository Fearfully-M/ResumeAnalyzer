import pickle
import os

# Save resume to a file


def save_resume_pickle(file_path, resume_text):
    with open(file_path, "wb") as file:
        pickle.dump(resume_text, file)

# Load resume from a file


def load_resume_pickle(file_path):
    with open(file_path, 'rb') as file:
        resume_data = pickle.load(file)
        print("Inside the load resume pickle function")
        print(resume_data)

    # Ensure the data is a string
    # if not isinstance(resume_data, str):
    #     raise ValueError("The content of the .pkl file must be a string.")

    return resume_data

# which save slot the user saves the resume to 1, 2, or 3


def save_slot_selection(file_path):

    # read the file's content
    resume_text = read_text_file(file_path)

    print("Resume text", resume_text)

    # Extract the base name (example 'Resume.txt')
    base_name = os.path.basename(file_path)

    # Extract the file name without the extension (example 'Resume')
    file_name_without_ext = os.path.splitext(base_name)[0]

    # Change the extension to '.pkl'
    new_file_name = f"{file_name_without_ext}.pkl"

    # save the new resume file to the current directory with extension '.pkl'
    save_resume_pickle(new_file_name, resume_text)

    # load the new resume file
    print(resume_text)
    return load_resume_pickle(new_file_name)


def read_text_file(file_path):
    try:
        with open(file_path, "rb") as file:  # Open the file in read mode
            content = file.read()  # Read the file's contents
            return content  # Print the file contents to the console
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except IOError:
        print(
            f"An error occurred while trying to read the file at {file_path}.")

# # Example usage
# file_path = "resume.pkl"
# save_resume_pickle(file_path, "This is a sample resume.")
# print(load_resume_pickle(file_path))  # Output: This is a sample resume.

# used to get lines from text and save to a list
# lines = []
# while True:
#     line = input()
#     if line == "": # if nothing on the second line then break
#         break
#     lines.append(line)
# return " ".join(lines) # return all lines seperated by a space
