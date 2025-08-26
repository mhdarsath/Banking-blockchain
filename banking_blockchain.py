import hashlib
import time

# Define a Block
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions  # banking transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = str(self.index) + str(self.transactions) + str(self.timestamp) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Blockchain Class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, ["Genesis Block"], time.time(), "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        prev_block = self.get_last_block()
        new_block = Block(len(self.chain), transactions, time.time(), prev_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]
            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != prev.hash:
                return False
        return True

# Example Banking Transactions
bank_chain = Blockchain()

# Adding some transactions
bank_chain.add_block({"sender": "Alice", "receiver": "Bob", "amount": 500})
bank_chain.add_block({"sender": "Bob", "receiver": "Charlie", "amount": 200})
bank_chain.add_block({"sender": "Charlie", "receiver": "David", "amount": 150})

# Display the blockchain
for block in bank_chain.chain:
    print(f"Block {block.index}:")
    print(f"Transactions: {block.transactions}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}\n")

# Validate blockchain
print("Is Blockchain Valid?", bank_chain.is_chain_valid())
