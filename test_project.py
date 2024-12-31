from main import handle_shortcuts, on_submit, select_file, select_resume
from saveResumes import save_resume_pickle, load_resume_pickle, save_slot_selection, read_text_file
from mainFunctions import extract_keywords, match_keywords, detect_keyword_stuffing
import pytest
from unittest.mock import patch, MagicMock, mock_open, patch
import os

"""ChatGPT was used extensively to help with testing"""
# Sample file path and return values
file_path = '/home/user/Documents/Resume.txt'
mock_resume_text = 'This is a sample resume text.'

# Test for save_slot_selection function


@patch('resume_analyzer.read_text_file')  # Mock the read_text_file function
@patch('resume_analyzer.os.path.basename')  # Mock os.path.basename
@patch('resume_analyzer.os.path.splitext')  # Mock os.path.splitext
@patch('resume_analyzer.save_resume_pickle')  # Mock save_resume_pickle
@patch('resume_analyzer.load_resume_pickle')  # Mock load_resume_pickle
def test_save_slot_selection(mock_load, mock_save, mock_split, mock_basename, mock_read):
    # Setup mock return values
    # Mock read_text_file to return the resume text
    mock_read.return_value = mock_resume_text
    # Mock os.path.basename to return 'Resume.txt'
    mock_basename.return_value = 'Resume.txt'
    # Mock os.path.splitext to split the filename
    mock_split.return_value = ('Resume', '.txt')
    # Mock load_resume_pickle to return the resume text
    mock_load.return_value = mock_resume_text

    # Call the function with the test file path
    result = save_slot_selection(file_path)

    # Verify that read_text_file was called with the correct file path
    mock_read.assert_called_once_with(file_path)

    # Verify that os.path.basename was called with the correct file path
    mock_basename.assert_called_once_with(file_path)

    # Verify that os.path.splitext was called with the correct filename
    mock_split.assert_called_once_with('Resume.txt')

    # Verify that save_resume_pickle was called with the new file name and resume text
    mock_save.assert_called_once_with('Resume.pkl', mock_resume_text)

    # Verify that load_resume_pickle was called with the new file name
    mock_load.assert_called_once_with('Resume.pkl')

    # Verify that the function returns the expected result
    assert result == mock_resume_text

# Test for save_resume_pickle function


# Mock the open function
@patch('resume_analyzer.open', new_callable=mock_open)
@patch('resume_analyzer.pickle.dump')  # Mock pickle.dump
def test_save_resume_pickle(mock_pickle_dump, mock_open):
    file_path = 'Resume.pkl'
    resume_text = 'This is a sample resume text.'

    # Call the function with the test file path and resume text
    save_resume_pickle(file_path, resume_text)

    # Verify that open was called with the correct file path and mode ('wb' for write-binary)
    mock_open.assert_called_once_with(file_path, 'wb')

    # Verify that pickle.dump was called with the correct arguments (resume text and file handle)
    mock_pickle_dump.assert_called_once_with(resume_text, mock_open())

    # You can also verify that the file is being opened correctly with the correct arguments:
    # This checks that the file write operation has been called
    mock_open().write.assert_called()
