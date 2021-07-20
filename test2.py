import Blockchain


blockchain = Blockchain.BlockChain()
for i in range(0, 10000):
    blockchain.generateBlock(i)

print(blockchain.chain[8000].printBlock())
print("Chain valid? " + str(blockchain.validate()))

blockchain.chain[8000].data = "changed!"

print(blockchain.chain[8000].printBlock())

print("Before changing other blocks:")
print("Chain valid? " + str(blockchain.validate()))

prev_hash = blockchain.chain[7999].hash

for i in range(8000, 10001):
    blockchain.chain[i].previousHash = prev_hash
    blockchain.chain[i].hash = blockchain.chain[i].calculateHash()
    prev_hash = blockchain.chain[i].hash

print("\nAfter changing other blocks:")
print("Chain valid? " + str(blockchain.validate()))
