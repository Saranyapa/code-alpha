#add required import data
import os
import shutil

def organize_files(directory):
    # Create a dictionary to map file extensions to directories
    extensions_mapping = {
        'documents': ['.pdf', '.doc', '.docx', '.txt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'audio': ['.mp3', '.wav', '.ogg', '.flac'],
        'archives': ['.zip', '.rar', '.tar', '.gz'],
        'executables': ['.exe', '.msi', '.bat'],
        'code': ['.py', '.java', '.cpp', '.html', '.css', '.js']
        
    }

    # Create directories for each category
    for category in extensions_mapping:
        os.makedirs(os.path.join(directory, category), exist_ok=True)

    # it leads over files in the directory
    for filename in os.listdir(directory):
        if filename != 'organize_files.py':  
            src_path = os.path.join(directory, filename)
            if os.path.isfile(src_path):
                # find  the file extension
                _, extension = os.path.splitext(filename)
                extension = extension.lower()

                
                target_category = None
                for category, extensions in extensions_mapping.items():
                    if extension in extensions:
                        target_category = category
                        break

                
                if target_category:
                    dest_path = os.path.join(directory, target_category, filename)
                    shutil.move(src_path, dest_path)
                    print(f"Moved {filename} to {target_category} directory.")
                else:
                    print(f"Extension {extension} not mapped. File {filename} was not moved.")

if __name__ == "__main__":
    directory = input("Enter the directory path to organize files: ")
    organize_files(directory)
