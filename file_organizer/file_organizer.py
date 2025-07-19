import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".docx", ".doc", ".pdf", ".txt"]
}

def organize_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("❌ The folder path does not exist.")
            return

        files = os.listdir(folder_path)
        if not files:
            print("📁 The folder is empty.")
            return

        for file in files:
            file_path = os.path.join(folder_path, file)

            # Skip if not a file
            if not os.path.isfile(file_path):
                continue

            file_ext = os.path.splitext(file)[1].lower()
            moved = False

            # Check and move file to appropriate category
            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"✅ Moved '{file}' to '{folder_name}/'")
                    moved = True
                    break

            # If no matching extension, move to "Others"
            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"📦 Moved '{file}' to 'Others/'")

        print("\n🎉 File organization completed successfully!")

    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

def main():
    folder_path = input("📂 Enter the full path of the folder to organize: ").strip()
    organize_files(folder_path)

if __name__ == "__main__":
    main()
