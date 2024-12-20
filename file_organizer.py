import os
import shutil

# Define the folder to organize
folder_path = "C:/Users/YourName/Downloads"

# Define the file type categories
file_types = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
}

# Organize files into folders
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        for category, extensions in file_types.items():
            if file_name.endswith(tuple(extensions)):
                target_folder = os.path.join(folder_path, category)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, target_folder)
                print(f"Moved {file_name} to {category}")
