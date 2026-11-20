import re
from collections import Counter

def analyze_text_metrics(text):
    """Calculates granular counts for characters, words, sentences, digits, and symbols."""
    # Basic structural length parameters
    char_count_with_spaces = len(text)
    char_count_no_spaces = len(text.replace(" ", "").replace("\n", ""))
    
    # Extract structural elements using regular expressions
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    
    # Sentence boundaries split based on period, exclamation, or question marks
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()] # filter out empty gaps
    sentence_count = len(sentences)
    
    # Content type breakdown using regex token lists
    vowels = re.findall(r'[aeiouAEIOU]', text)
    digits = re.findall(r'\d', text)
    # Symbols are anything that is not alphanumeric, a space, or a line break
    symbols = re.findall(r'[^a-zA-Z0-9\s]', text)

    print("\n" + "="*35)
    print("      TEXT QUANTITY METRICS      ")
    print("="*35)
    print(f"[-] Characters (with spaces): {char_count_with_spaces}")
    print(f"[-] Characters (no spaces):   {char_count_no_spaces}")
    print(f"[-] Total Words Extracted:    {word_count}")
    print(f"[-] Total Sentences Parsed:   {sentence_count}")
    print(f"[-] Vowels Found Count:       {len(vowels)}")
    print(f"[-] Numerical Digits Count:   {len(digits)}")
    print(f"[-] Special Symbols Count:    {len(symbols)}")
    print("===================================\n")

    # Display frequency analytics if words exist
    if words:
        word_counts = Counter(words)
        most_common_word, frequency = word_counts.most_common(1)[0]
        print(f">> Most Frequent Word: '{most_common_word}' (Appeared {frequency} times)")
    else:
        print(">> Most Frequent Word: None (No words detected)")

def check_palindrome_status(text):
    """Evaluates if the targeted alphanumeric character sequence reads identical bidirectionally."""
    # Strip down everything except lowercase letters and numbers
    cleaned_string = "".join(re.findall(r'[a-zA-Z0-9]', text)).lower()
    
    if not cleaned_string:
        print("\n[Notice] Input contains no alphanumeric characters to evaluate.")
        return False
        
    # Standard Python string slice inversion manipulation check
    is_palindrome = cleaned_string == cleaned_string[::-1]
    
    print("\n--- Palindrome Verification ---")
    print(f"Cleaned Sequence Evaluated: \"{cleaned_string}\"")
    if is_palindrome:
        print(">> Result: YES, this string sequence is a valid Palindrome! <<")
    else:
        print(">> Result: NO, this string sequence is not a Palindrome. <<")
        
    return is_palindrome

def main():
    """Main terminal coordinator tracking control choices across options loops."""
    while True:
        print("\n====== ADVANCED TEXT ANALYZER HUB ======")
        print("1. Analyze Text (Counts & Word Frequencies)")
        print("2. Check for Palindrome Properties")
        print("3. Execute Complete Analysis Pipeline")
        print("4. Close Analytics Framework")
        print("========================================")
        
        choice = input("Select processing interface task (1-4): ").strip()
        
        if choice in ['1', '2', '3']:
            user_input = input("\nEnter or paste the block of text to analyze:\n> ")
            if not user_input.strip():
                print("[Abort] Processing cancelled. Text text input body cannot be empty.")
                continue
                
            if choice == '1':
                analyze_text_metrics(user_input)
            elif choice == '2':
                check_palindrome_status(user_input)
            elif choice == '3':
                analyze_text_metrics(user_input)
                check_palindrome_status(user_input)
                
        elif choice == '4':
            print("\nShutting down text operations pipeline grid. Terminal offline.")
            break
        else:
            print("\n[Invalid] Select from numerical commands bounds (1-4) only.")

if __name__ == "__main__":
    main()
