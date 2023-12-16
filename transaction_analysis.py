class TransactionAnalysis:
    def __init__(self, transactions):
        self.transactions = transactions

    
    def display_transactions(self):
        print("Transactions:")
        for tx in self.transactions:
            print(f"ID: {tx['id']}, Sender: {tx['sender']}, Receiver: {tx['receiver']}, Amount: {tx['amount']} BTC, Timestamp: {tx['timestamp']}")

    
    def calculate_balance(self, account_number):
        balance = 0.0
        for tx in self.transactions:
            if tx['receiver'] == account_number:
                balance += tx['amount']
            elif tx['sender'] == account_number:
                balance -= tx['amount']
        return balance
