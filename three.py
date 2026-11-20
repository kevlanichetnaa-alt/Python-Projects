import json
import os

# File definition for persistent library database
LIBRARY_FILE = "library_data.json"

def load_library():
    """Loads library inventory from JSON file. Returns clean records if missing or corrupt."""
    if not os.path.exists(LIBRARY_FILE):
        return {}
    try:
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, PermissionError) as error:
        print(f"\n[Warning] Database read failure ({error}). Starting with a blank library.")
        return {}

def save_library(library):
    """Safely commits library data back to disk storage."""
    try:
        with open(LIBRARY_FILE, 'w') as file:
            json.dump(library, file, indent=4)
        print("\n[System] Database updated successfully.")
    except Exception as error:
        print(f"\n[Error] Failed to save database modifications: {error}")

def add_book(library):
    """Adds a new book or increments copies of an existing title."""
    print("\n--- Add Book to Inventory ---")
    isbn = input("Enter Book ISBN/ID: ").strip()
    if not isbn:
        print("[Abort] ISBN identifier cannot be empty.")
        return

    # If book already exists, offer to increase quantity tracking
    if isbn in library:
        print(f"Book found: '{library[isbn]['title']}'")
        try:
            additional_copies = int(input("Enter number of additional copies to add: "))
            if additional_copies <= 0:
                print("[Abort] Quantity must be greater than zero.")
                return
            library[isbn]['total_copies'] += additional_copies
            library[isbn]['available_copies'] += additional_copies
            print(f"\n[Success] Added {additional_copies} copies.")
            save_library(library)
        except ValueError:
            print("[Abort] Invalid input. Must be an integer.")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    if not title or not author:
        print("[Abort] Title and Author parameters cannot be blank.")
        return

    try:
        total_copies = int(input("Enter Total Copies: "))
        if total_copies <= 0:
            print("[Abort] Initial stock copies must be at least 1.")
            return
    except ValueError:
        print("[Abort] Invalid input. Must enter a whole number.")
        return

    # Store structural schema using nested dictionaries
    library[isbn] = {
        "title": title,
        "author": author,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    save_library(library)

def remove_book(library):
    """Deletes an entire book record permanently from the registry database."""
    print("\n--- Remove Book Profile ---")
    isbn = input("Enter Book ISBN to remove: ").strip()

    if isbn in library:
        # Confirm that no copies are currently checked out before deleting
        if library[isbn]['available_copies'] != library[isbn]['total_copies']:
            print("[Abort] Cannot remove book. Some copies are currently issued out!")
            return
            
        removed_title = library[isbn]['title']
        del library[isbn]
        print(f"\n[Success] '{removed_title}' removed from library catalog.")
        save_library(library)
    else:
        print("[Error] ISBN match target index not found.")

def issue_book(library):
    """Deducts an available copy to issue a book out."""
    print("\n--- Issue Book Transaction ---")
    isbn = input("Enter Book ISBN to issue: ").strip()

    if isbn not in library:
        print("[Error] Book not registered in system catalog.")
        return

    if library[isbn]['available_copies'] > 0:
        library[isbn]['available_copies'] -= 1
        print(f"\n[Success] '{library[isbn]['title']}' has been issued successfully!")
        print(f"Remaining available inventory: {library[isbn]['available_copies']}")
        save_library(library)
    else:
        print("\n[Out of Stock] All copies of this title are currently issued out.")

def return_book(library):
    """Increments the available copy count back upon safe return processing."""
    print("\n--- Return Book Transaction ---")
    isbn = input("Enter Book ISBN to return: ").strip()

    if isbn not in library:
        print("[Error] This item tracking ID does not match our records.")
        return

    if library[isbn]['available_copies'] < library[isbn]['total_copies']:
        library[isbn]['available_copies'] += 1
        print(f"\n[Success] '{library[isbn]['title']}' returned safely.")
        print(f"Updated available inventory: {library[isbn]['available_copies']}")
        save_library(library)
    else:
        print("\n[Anomaly] System records indicate all copies are already present in inventory.")

def track_inventory(library):
    """Displays visual tabular matrix overview outlining book tracking records."""
    if not library:
        print("\n[Notice] Library inventory array system is currently empty.")
        return

    print("\n" + "="*70)
    print(f"{'ISBN':<10} {'TITLE':<22} {'AUTHOR':<18} {'TOTAL':<8} {'AVAILABLE':<10}")
    print("="*70)
    for isbn, info in library.items():
        print(f"{isbn:<10} {info['title'][:20]:<22} {info['author'][:16]:<18} {info['total_copies']:<8} {info['available_copies']:<10}")
    print("="*70)

def main():
    """Main dashboard environment loop managing operation transitions."""
    library_db = load_library()

    while True:
        print("\n====== CORE LIBRARY CONSOLE INTERFACE ======")
        print("1. Add Book / Increase Stock")
        print("2. Remove Book from Catalog")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Track Available Books")
        print("6. Shutdown System")
        print("============================================")
        
        choice = input("Select command line operation (1-6): ").strip()

        if choice == '1': add_book(library_db)
        elif choice == '2': remove_book(library_db)
        elif choice == '3': issue_book(library_db)
        elif choice == '4': return_book(library_db)
        elif choice == '5': track_inventory(library_db)
        elif choice == '6':
            print("\nDatabase session safely closed. Engine offline.")
            break
        else:
            print("\n[Invalid] Select from numerical commands bounds (1-6) only.")

if __name__ == "__main__":
    main()
