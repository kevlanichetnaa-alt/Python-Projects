import json
import os
from datetime import datetime

# File definition for persistent account tracking
BANK_FILE = "banking_data.json"

def load_accounts():
    """Loads banking profiles from a JSON storage file. Returns an empty dict on system start."""
    if not os.path.exists(BANK_FILE):
        return {}
    try:
        with open(BANK_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, PermissionError) as error:
        print(f"\n[Warning] Security storage read failure ({error}). Starting with new session.")
        return {}

def save_accounts(accounts):
    """Safely commits account modifications and transactions back to disk storage."""
    try:
        with open(BANK_FILE, 'w') as file:
            json.dump(accounts, file, indent=4)
    except Exception as error:
        print(f"\n[Critical] Failed to record ledger modifications to disk: {error}")

def create_account(accounts):
    """Registers a new bank account profile with a clean structural schema."""
    print("\n--- Create New Bank Account ---")
    account_num = input("Enter a Unique Account Number: ").strip()
    
    if not account_num:
        print("[Abort] Account number identification lines cannot be empty.")
        return
    if account_num in accounts:
        print(f"[Abort] Allocation collision! Account '{account_num}' already exists.")
        return

    name = input("Enter Account Holder Name: ").strip()
    if not name:
        print("[Abort] Holder name parameters cannot be blank.")
        return

    try:
        initial_deposit = float(input("Enter Initial Deposit Amount ($): "))
        if initial_deposit < 0:
            print("[Abort] Initial opening deposits cannot be negative balances.")
            return
    except ValueError:
        print("[Abort] Parsing error. Numeric ledger variables are required.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Store structural schema using nested dictionaries matching system guidelines
    accounts[account_num] = {
        "name": name,
        "balance": initial_deposit,
        "history": [f"[{timestamp}] Account opened with initial deposit: ${initial_deposit:.2f}"]
    }
    
    save_accounts(accounts)
    print(f"\n[Success] Account for '{name}' established successfully with ID: {account_num}")

def deposit_funds(accounts):
    """Increments matching ledger variables and appends tracking summaries."""
    print("\n--- Deposit Transaction Console ---")
    account_num = input("Enter Account Number: ").strip()

    if account_num not in accounts:
        print("[Error] Account registration records missing matching profiles.")
        return

    try:
        amount = float(input("Enter Amount to Deposit ($): "))
        if amount <= 0:
            print("[Abort] Deposit increments must be greater than zero.")
            return
    except ValueError:
        print("[Abort] Format exception. Numeric transaction values required.")
        return

    accounts[account_num]["balance"] += amount
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[account_num]["history"].append(f"[{timestamp}] Deposited: ${amount:.2f}")
    
    save_accounts(accounts)
    print(f"\n[Success] Deposited ${amount:.2f}. Updated Balance: ${accounts[account_num]['balance']:.2f}")

def withdraw_funds(accounts):
    """Validates thresholds and deducts metrics across active target keys safely."""
    print("\n--- Withdrawal Transaction Console ---")
    account_num = input("Enter Account Number: ").strip()

    if account_num not in accounts:
        print("[Error] Target record sequence missing.")
        return

    try:
        amount = float(input("Enter Amount to Withdraw ($): "))
        if amount <= 0:
            print("[Abort] Withdrawal allocations must be greater than zero.")
            return
        if amount > accounts[account_num]["balance"]:
            print(f"[Rejected] Overdraft block. Available balance is only: ${accounts[account_num]['balance']:.2f}")
            return
    except ValueError:
        print("[Abort] Format exception. Numeric transaction parameters required.")
        return

    accounts[account_num]["balance"] -= amount
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[account_num]["history"].append(f"[{timestamp}] Withdrew: ${amount:.2f}")
    
    save_accounts(accounts)
    print(f"\n[Success] Withdrew ${amount:.2f}. Updated Balance: ${accounts[account_num]['balance']:.2f}")

def check_balance(accounts):
    """Retrieves standard metrics without committing alterations."""
    print("\n--- Balance Enquiry Interface ---")
    account_num = input("Enter Account Number: ").strip()

    if account_num in accounts:
        profile = accounts[account_num]
        print(f"\n[Account Profile Matches]")
        print(f"Holder Name:     {profile['name']}")
        print(f"Current Balance: ${profile['balance']:.2f}")
    else:
        print("[Error] Verification index parameter missing.")

def view_transaction_history(accounts):
    """Extracts and formats sequential logging arrays associated with an account."""
    print("\n--- Transaction History Ledger ---")
    account_num = input("Enter Account Number: ").strip()

    if account_num in accounts:
        history_log = accounts[account_num]["history"]
        print(f"\n=== Transaction Log Ledger for ID: {account_num} ===")
        for log_entry in history_log:
            print(log_entry)
        print("==================================================")
    else:
        print("[Error] Record lookup target missing.")

def main():
    """Main workflow runtime hub allocating actions based on choice loops."""
    ledger_db = load_accounts()

    while True:
        print("\n====== BANKING SIMULATION HUB SYSTEM ======")
        print("1. Create New Bank Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Check Account Balance")
        print("5. View Transaction History")
        print("6. Shutdown Banking Interface")
        print("===========================================")
        
        choice = input("Select banking framework operation (1-6): ").strip()

        if choice == '1': create_account(ledger_db)
        elif choice == '2': deposit_funds(ledger_db)
        elif choice == '3': withdraw_funds(ledger_db)
        elif choice == '4': check_balance(ledger_db)
        elif choice == '5': view_transaction_history(ledger_db)
        elif choice == '6':
            print("\nDatabase ledger sessions committed. Core banking grid offline.")
            break
        else:
            print("\n[Invalid] Select from numerical commands bounds (1-6) only.")

if __name__ == "__main__":
    main()
