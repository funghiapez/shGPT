"""
use this tool to remove the unwanted element from the txt file
like ------page1------
and change it to an array seperated by comma or period
"""
import re
import os

def get_banned_array(banned_file_path):
    with open(banned_file_path, 'r', encoding='utf-8') as f:
        banned_text = f.read()
    return banned_text.split("/")

def preprocess_txt_file(file_path, banned_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    banned_array = get_banned_array(banned_path)
    # Turn the txt file into a file separated by slash
    text = re.sub(r'[，。]', '/', text)
    # Remove characters that are not in Chinese language
    text = re.sub(r'[^\u4e00-\u9fa5/]', '', text)
    for banned_text in banned_array:
        text = re.sub(banned_text, "某某", text)
    
    return text

def save_preprocessed_text(file_path, preprocessed_text):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(preprocessed_text)

# Example usage
file_path = input("Enter file path: ").replace(" ", "")
banned_path = input("Enter banned file path: ").replace(" ", "")
file_name = os.path.basename(file_path)
preprocessed_text = preprocess_txt_file(file_path, banned_path)
parent_dir = os.path.abspath(os.path.join(file_path, os.pardir))
output_path = parent_dir + "/OUTPUT_" + file_name
save_preprocessed_text(output_path, preprocessed_text)