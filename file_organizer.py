import os
import shutil
import logging
from datetime import datetime

# --- Setup Logging ---
logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# --- File Categories ---
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".js", ".html", ".css", ".java"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    # Check if folder exists
    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        logging.error(f"Folder not found: {folder_path}")
        return

    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension and category
        _, ext = os.path.splitext(filename)
        category = get_category(ext)

        # Create category folder if it doesn't exist
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

        # Move the file
        try:
            dest = os.path.join(category_folder, filename)
            shutil.move(file_path, dest)
            print(f"✅ Moved: {filename} → {category}/")
            logging.info(f"Moved: {filename} → {category}/")
            files_moved += 1
        except Exception as e:
            print(f"❌ Error moving {filename}: {e}")
            logging.error(f"Error moving {filename}: {e}")

    print(f"\n🎉 Done! {files_moved} files organized.")
    logging.info(f"Total files organized: {files_moved}")

# --- User Input ---
if __name__ == "__main__":
    print("=== File Organizer Script ===")
    folder = input("Enter the full path of the folder to organize: ").strip()
    organize_folder(folder)