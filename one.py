import json
import os

# File name where student data will be saved
DATA_FILE = "students_data.json"

def load_data():
    """Loads student data from the JSON file. Returns an empty dict if file doesn't exist or is corrupt."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, PermissionError) as e:
        print(f"\n[Error] Failed to load data file: {e}. Starting with a blank database.")
        return {}

def save_data(students):
    """Saves the student dictionary back to the JSON file safely."""
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(students, file, indent=4)
        print("\n[Success] Data saved successfully!")
    except PermissionError:
        print("\n[Error] Permission denied. Could not save data.")
    except Exception as e:
        print(f"\n[Error] An unexpected error occurred while saving: {e}")

def calculate_grade(marks):
    """Determines the grade based on marks standard tiers."""
    if marks >= 90: return 'A'
    elif marks >= 80: return 'B'
    elif marks >= 70: return 'C'
    elif marks >= 60: return 'D'
    else: return 'F'

def add_student(students):
    """Adds a new student to the dictionary after data validation."""
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ").strip()
    
    if not student_id:
        print("[Error] Student ID cannot be empty.")
        return
        
    if student_id in students:
        print(f"[Error] Student with ID {student_id} already exists.")
        return

    name = input("Enter Student Name: ").strip()
    if not name:
        print("[Error] Name cannot be empty.")
        return

    try:
        marks = float(input("Enter Marks (0-100): "))
        if not (0 <= marks <= 100):
            print("[Error] Marks must be between 0 and 100.")
            return
    except ValueError:
        print("[Error] Invalid input. Marks must be a number.")
        return

    # Create nested structure & auto-calculate grade
    grade = calculate_grade(marks)
    students[student_id] = {
        "name": name,
        "marks": marks,
        "grade": grade
    }
    print(f"\n[Success] Student '{name}' added successfully!")
    save_data(students)

def update_student(students):
    """Updates details of an existing student."""
    print("\n--- Update Student ---")
    student_id = input("Enter Student ID to update: ").strip()

    if student_id not in students:
        print("[Error] Student ID not found.")
        return

    print(f"Current details: Name: {students[student_id]['name']}, Marks: {students[student_id]['marks']}")
    
    # Optional updates: press enter to skip changing fields
    new_name = input("Enter new name (Leave blank to keep current): ").strip()
    new_marks_str = input("Enter new marks (Leave blank to keep current): ").strip()

    if new_name:
        students[student_id]['name'] = new_name

    if new_marks_str:
        try:
            new_marks = float(new_marks_str)
            if not (0 <= new_marks <= 100):
                print("[Error] Marks must be between 0 and 100. Update aborted.")
                return
            students[student_id]['marks'] = new_marks
            students[student_id]['grade'] = calculate_grade(new_marks)
        except ValueError:
            print("[Error] Invalid marks. Update aborted.")
            return

    print("\n[Success] Student record updated successfully!")
    save_data(students)

def delete_student(students):
    """Removes a student from the record database."""
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ").strip()

    if student_id in students:
        deleted_name = students[student_id]['name']
        del students[student_id]
        print(f"\n[Success] Student '{deleted_name}' removed successfully.")
        save_data(students)
    else:
        print("[Error] Student ID not found.")

def search_student(students):
    """Searches and displays a specific student's details."""
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID to search: ").strip()

    if student_id in students:
        info = students[student_id]
        print("\n--- Student Found ---")
        print(f"ID:     {student_id}")
        print(f"Name:   {info['name']}")
        print(f"Marks:  {info['marks']}")
        print(f"Grade:  {info['grade']}")
    else:
        print("[Error] Student ID not found.")

def display_all_students(students):
    """Prints a clean table overview of all current records."""
    if not students:
        print("\n[Info] No student records available.")
        return

    print("\n" + "="*50)
    print(f"{'ID':<10} {'Name':<20} {'Marks':<10} {'Grade':<5}")
    print("="*50)
    for sid, info in students.items():
        print(f"{sid:<10} {info['name']:<20} {info['marks']:<10.2f} {info['grade']:<5}")
    print("="*50)

def calculate_statistics(students):
    """Computes and prints average, highest, and lowest marks."""
    print("\n--- Performance Statistics ---")
    if not students:
        print("[Info] No student records available to calculate stats.")
        return

    # Extract all marks using list comprehension
    all_marks = [info['marks'] for info in students.values()]
    
    total_marks = sum(all_marks)
    count = len(all_marks)
    average = total_marks / count
    highest = max(all_marks)
    lowest = min(all_marks)

    print(f"Total Students:  {count}")
    print(f"Average Marks:   {average:.2f}")
    print(f"Highest Marks:   {highest:.2f}")
    print(f"Lowest Marks:    {lowest:.2f}")

def main():
    """Main application loop managing console menu workflows."""
    # Initialization and Loading phase
    students_db = load_data()
    
    while True:
        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. View All Students")
        print("6. View Performance Statistics")
        print("7. Exit")
        print("=======================================")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            add_student(students_db)
        elif choice == '2':
            update_student(students_db)
        elif choice == '3':
            delete_student(students_db)
        elif choice == '4':
            search_student(students_db)
        elif choice == '5':
            display_all_students(students_db)
        elif choice == '6':
            calculate_statistics(students_db)
        elif choice == '7':
            print("\nThank you for using the Student Management System. Goodbye!")
            break
        else:
            print("\n[Error] Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
