import sys
from blockchain_parser import BlockchainParser
from transaction_analysis import TransactionAnalysis
from account_manager import AccountManager
from error_handler import ErrorHandler

def main():
    # Check for command line arguments for the directory containing DAT files
    data_directory = sys.argv[1] if len(sys.argv) > 1 else '.'

    try:
        # Initialize the blockchain parser
        parser = BlockchainParser(data_directory)

        # Initialize account manager
        account_manager = AccountManager()

        # User input for account number
        account_number = input("Enter a Bitcoin account number: ")
        account_number = account_manager.get_nickname(account_number)

        # Analyze transactions
        transactions = parser.get_transactions_for_account(account_number)
        analysis = TransactionAnalysis(transactions)

        # Display transaction details and account balance
        analysis.display_transactions()
        print(f"Account Balance: {analysis.calculate_balance()} BTC")

    except Exception as e:
        ErrorHandler.handle_error(e)

if __name__ == "__main__":
    main()