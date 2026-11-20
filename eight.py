import os
import shutil

def organize_directory(target_path):
    """Scan and organize all files in the target folder by their extension types."""
    # Define file type extension maps using intuitive grouping pools
    extension_map = {
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Programs": [".exe", ".msi", ".sh", ".bat"]
    }

    if not os.path.isdir(target_path):
        print(f"[Error] The designated directory path '{target_path}' does not exist.")
        return

    print(f"\n--- Scanning Path: {target_path} ---")
    
    # Iterate through all items directly under the target directory path
    try:
        items = os.listdir(target_path)
    except PermissionError:
        print("[Critical] Permission denied to access this directory layer.")
        return

    file_count = 0
    
    for item in items:
        item_path = os.path.join(target_path, item)
        
        # Process files only; skip folders to prevent circular nesting loops
        if os.path.isfile(item_path):
            filename, extension = os.path.splitext(item.lower())
            
            # Identify target category folder matching extension mappings
            destination_category = "Others"
            for category, extensions in extension_map.items():
                if extension in extensions:
                    destination_category = category
                    break
            
            # Construct full category folder pathway location
            category_dir = os.path.join(target_path, destination_category)
            
            # Ensure folder framework path layers exist securely
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)
                print(f"[System] Created new structural allocation folder: {destination_category}")

            # Define initial source to destination tracking limits parameters
            new_destination_path = os.path.join(category_dir, item)
            
            # Auto-rename sequence algorithm block if file identity collision happens
            if os.path.exists(new_destination_path):
                counter = 1
                while os.path.exists(new_destination_path):
                    # Injects counter smoothly before extension standard bounds
                    raw_filename, ext = os.path.splitext(item)
                    renamed_filename = f"{raw_filename}_{counter}{ext}"
                    new_destination_path = os.path.join(category_dir, renamed_filename)
                    counter += 1
                print(f"[Auto-Rename] Collision resolved. Renaming '{item}' -> '{os.path.basename(new_destination_path)}'")

            try:
                # Perform execution moves parameters
                shutil.move(item_path, new_destination_path)
                file_count += 1
            except (IOError, PermissionError) as error:
                print(f"[Skip File Error] Could not relocate item '{item}': {error}")

    print(f"[Complete] Successfully organized {file_count} file entries.")

def prune_empty_folders(target_path):
    """Recursively parses folder trees inside directory targets, destroying empty pathways."""
    print("\n--- Scanning for Empty Folders Grid ---")
    deleted_folders_count = 0

    # Walk directories bottom-up architecture to ensure sub-folders clear out before parents
    for current_root, folders, files in os.walk(target_path, topdown=False):
        for single_folder in folders:
            folder_path = os.path.join(current_root, single_folder)
            
            try:
                # Check absolute list capacity items
                if not os.listdir(folder_path):
                    os.rmdir(folder_path)
                    print(f"[Pruned Empty Category Folder]: {folder_path}")
                    deleted_folders_count += 1
            except PermissionError:
                # Catch localized tracking read constraint locks gracefully
                continue
            except OSError as error:
                print(f"[System Note] Could not evaluate removal on directory '{single_folder}': {error}")

    print(f"[Pruning Complete] Eliminated {deleted_folders_count} empty directory paths.")

def main():
    """Main administrative execution workflow coordinator management terminal wrapper loop."""
    while True:
        print("\n====== AUTOMATED FILE SYSTEM ORGANIZER ======")
        print("1. Run Complete Optimization Profile (Organize & Prune)")
        print("2. Organize Files by Extension Categories Only")
        print("3. Prune / Delete Empty Folders Only")
        print("4. Close Maintenance Utility Engine")
        print("=============================================")
        
        choice = input("Select processing interface index command (1-4): ").strip()
        
        if choice in ['1', '2', '3']:
            target_directory = input("\nEnter full path of the folder to clean up:\n> ").strip()
            
            # Handle trivial context expansions safely
            if not target_directory:
                print("[Abort] Input folder target execution path line string lines cannot be empty.")
                continue

            if choice == '1':
                organize_directory(target_directory)
                prune_empty_folders(target_directory)
            elif choice == '2':
                organize_directory(target_directory)
            elif choice == '3':
                prune_empty_folders(target_directory)
                
        elif choice == '4':
            print("\nExiting file manager operations console. Maintenance suite offline.")
            break
        else:
            print("\n[Invalid Selection] Enter numbers within choice option bounds (1-4) only.")

if __name__ == "__main__":
    main()
