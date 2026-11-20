import json
import os
import time

# File definitions for configuration structures
RESULTS_FILE = "quiz_results.txt"

def load_quiz_bank():
    """Returns a hardcoded nested structure definition pool of quiz metadata modules."""
    return [
        {
            "question": "Which programming language was created by Guido van Rossum?",
            "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
            "answer": "B"
        },
        {
            "question": "What data structure operates on a First-In, First-Out (FIFO) pipeline architecture?",
            "options": ["A) Stack", "B) Array", "C) Queue", "D) Tree"],
            "answer": "C"
        },
        {
            "question": "Which of the following is NOT a valid built-in collection data type in Python?",
            "options": ["A) List", "B) Dictionary", "C) Set", "D) ArrayLink"],
            "answer": "D"
        },
        {
            "question": "What is the primary function of the 'json.dumps()' framework module function?",
            "options": ["A) Read JSON files", "B) Convert a Python object into a JSON string", "C) Parse raw text streams", "D) Clear database keys"],
            "answer": "B"
        }
    ]

def record_quiz_run(user_name, score, total_questions, duration):
    """Appends structured historical score outputs onto file tracking blocks cleanly."""
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        percentage = (score / total_questions) * 100
        with open(RESULTS_FILE, 'a') as file:
            file.write(f"[{timestamp}] User: {user_name} | Score: {score}/{total_questions} ({percentage:.1f}%) | Time Spent: {duration:.1f}s\n")
        print("\n[System Database] Running records committed to score metrics sheet.")
    except Exception as error:
        print(f"\n[Error] Failure posting database update logs: {error}")

def execute_quiz_pipeline():
    """Orchestrates loop boundaries tracking input inputs against target correct answers metrics keys."""
    print("\n--- Initializing Quiz Session ---")
    user_name = input("Enter candidate profile user name: ").strip()
    if not user_name:
        print("[Abort] System cannot initialize without an assigned session profile name.")
        return

    questions = load_quiz_bank()
    score = 0
    total = len(questions)
    
    print(f"\nWelcome, {user_name}! The quiz contains {total} questions. Each choice requires typing A, B, C, or D.")
    input("Press [Enter] to start the quiz timer tracking mechanism...")
    
    # Start tracking clock runtime intervals
    start_time = time.time()
    
    for dynamic_index, item in enumerate(questions, 1):
        print(f"\nQuestion {dynamic_index}: {item['question']}")
        for alternative in item['options']:
            print(alternative)
            
        while True:
            selection = input("Your answer choice (A/B/C/D): ").strip().upper()
            if selection in ['A', 'B', 'C', 'D']:
                break
            print("[Warning] Choice out of formatting constraints. Choose options metrics between A and D.")
            
        if selection == item['answer']:
            print("[Correct] Answer confirmed.")
            score += 1
        else:
            print(f"[Incorrect] Wrong validation mapping. The correct key answer option was: {item['answer']}")
            
    end_time = time.time()
    elapsed_duration = end_time - start_time
    final_percentage = (score / total) * 100
    
    print("\n" + "="*45)
    print("             QUIZ PERFORMANCE SUMMARY         ")
    print("="*45)
    print(f"[-] Candidate Name:       {user_name}")
    print(f"[-] Correct Answers:     {score} out of {total}")
    print(f"[-] Final Success Ratio:  {final_percentage:.2f}%")
    print(f"[-] Total Session Time:   {elapsed_duration:.1f} seconds")
    print("=============================================")
    
    # Store history output summaries metrics
    record_quiz_run(user_name, score, total, elapsed_duration)

def display_historical_ledger():
    """Prints history runs tracked locally on disk sheets."""
    print("\n--- Master Historical Quiz Run Dashboard ---")
    if not os.path.exists(RESULTS_FILE):
        print("[Notice] Dashboard empty. Execute quiz instances first to generate storage tracking fields.")
        return

    try:
        with open(RESULTS_FILE, 'r') as file:
            content_lines = file.readlines()
            if not content_lines:
                print("[Notice] Log tracking layers empty.")
                return
            print("\n" + "-"*80)
            for structural_line in content_lines:
                print(structural_line.strip())
            print("-"*80)
    except Exception as error:
        print(f"[Error] Execution read block missing or parsing parameters failed: {error}")

def main():
    """Core terminal router coordinating logic option states updates loop frameworks."""
    while True:
        print("\n====== CONSOLE QUIZ PLATFORM INTERFACE ======")
        print("1. Launch Dynamic Quiz Session")
        print("2. View Leaderboard / Past Run Metrics")
        print("3. Terminate Application Interface")
        print("=============================================")
        
        choice = input("Select application command sequence task (1-3): ").strip()
        
        if choice == '1':
            execute_quiz_pipeline()
        elif choice == '2':
            display_historical_ledger()
        elif choice == '3':
            print("\nShutting down active examination nodes framework. Console grid offline.")
            break
        else:
            print("\n[Invalid] Select from numerical commands bounds (1-3) only.")

if __name__ == "__main__":
    main()
