import os
import shutil

def organize_folder(directory_path):
    categories = {
        '.txt': 'Documents',
        '.jpg': 'Pictures',
        '.png': 'Pictures',
        '.docx': 'Documents',
        '.pdf': 'Documents',
        '.mp3': 'Music',
        '.mp4': 'Videos',
        '.mov': 'Videos',
        '.avi': 'Videos',
        '.flv': 'Videos',
        '.zip': 'Archives',
    }

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            ext = os.path.splitext(item)[1]
            if ext.lower() in categories:
                dest_path = os.path.join(directory_path, categories[ext.lower()])
            else:
                dest_path = os.path.join(directory_path, 'Other')

            if not os.path.isdir(dest_path):
                os.makedirs(dest_path, exist_ok=True)
            try:
                shutil.move(item_path, dest_path)
            except shutil.Error as e:
                print(f"Error: {e}")
            except FileExistsError as fe:
                print(f"File already exists: {fe}")


organize_folder(r"C:\Users\Lenovo\Desktop\toSort")
