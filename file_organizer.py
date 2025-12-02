import os
import shutil
from utils import clear_screen, pause

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"]
}

def organize_files(directory):
    moved = 0
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            ext = os.path.splitext(file)[1].lower()
            category = next((cat for cat, exts in FILE_TYPES.items() if ext in exts), "Others")
            folder = os.path.join(directory, category)
            os.makedirs(folder, exist_ok=True)
            shutil.move(path, os.path.join(folder, file))
            moved += 1
    print(f"Done. Files moved: {moved}")

def file_organizer_menu():
    clear_screen()
    folder = input("Folder path to organize: ").strip()
    if not os.path.exists(folder):
        print("Path not found.")
        pause()
        return
    organize_files(folder)
    pause()
