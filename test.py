import Blockchain


blockchain = Blockchain.BlockChain()
for i in range(0, 10000):
    blockchain.generateBlock(i)

print(blockchain.chain[777].printBlock())
print("Chain valid? " + str(blockchain.validate()))

blockchain.chain[777].data = "changed!"

print(blockchain.chain[777].printBlock())
print("Chain valid? " + str(blockchain.validate()))
