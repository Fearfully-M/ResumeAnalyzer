import os

directory_path = '/home/fearfully_m/Desktop/ResumeAnalyzer/'

# Filter the files to only search for .pkl files
files = [f for f in os.listdir(directory_path) 
         if os.path.isfile(os.path.join(directory_path, f)) and f.endswith('.pkl')]

