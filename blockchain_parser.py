import json

class BlockchainParser:
    def __init__(self, data_directory):
        self.data_directory = data_directory
        self.transactions = self._load_transactions()

    def _load_transactions(self):
        try:
            with open(f"{self.data_directory}/transactions.json", 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Transactions file not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error parsing transactions: {e}")
            return []

    def get_transactions_for_account(self, account_number):
        # Filter transactions for the given account number
        relevant_transactions = [
            tx for tx in self.transactions 
            if tx['sender'] == account_number or tx['receiver'] == account_number
        ]
        return relevant_transactions
