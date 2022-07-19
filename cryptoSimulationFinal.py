import random
import hashlib
import json

class Participant:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        #self.blockchain = []
        self.activeBlock = None
        self.ranNum = random.randint(0,100)
        self.biggerNum = self.ranNum + 1
        self.privateHash = hashlib.sha256(self.ranNum.to_bytes(8, 'big'))
        self.privateKey = self.privateHash.digest()
        self.publicHash = hashlib.sha256(self.biggerNum.to_bytes(8,'big'))
        self.publicKey = self.publicHash.digest()

class Block:
    def __init__(self, previousHash, pendingTransactions, longestChain):
        self.previousHash = previousHash
        self.pendingTransactions = pendingTransactions
        self.index = len(longestChain) + 1
        self.block = {
            'index': self.index,
            'transactions': self.pendingTransactions,
            'previousHash': self.previousHash
            }
    def hash(self):
        #This function was taken online: https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
        string_object = json.dumps(self.block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash=raw_hash.hexdigest()

        return hex_hash

class Genesis:
    def __init__(self, hash, pendingTransactions):
        self.hash = hash
        self.pendingTransactions = pendingTransactions
        self.index = 0
        self.block = {
            'index': self.index,
            'transactions': self.pendingTransactions
            }
    def hash(self):
        return self.hash

parameters = False
participants = []
reward = 500
blockchain = []
transactions = []

while (parameters == False):
    question = input("Add participant / delete participant / view participants / move to next phase:")
    if question[:3] == "add" and question.count(',') == 1:
        participants.append(Participant(question[4:question.find(',')], int(question[question.find(',')+2:])))
        transactions.append(question[4:question.find(',')] + " is paid $" + question[question.find(',')+2:])
    elif question == "list":
        for person in participants:
            print(person.name + " has $" + str(person.money))
    elif question[:6] == "delete":
        for person in participants:
            if person.name == question[7:]:
                participants.remove(person)
    elif question == "continue":
        parameters = True
        print("The number of participants and their initial amounts of money is now complete.\nYou may now begin transactions.")

running = True
#activeBlock = None
genesisData = []
genesisBlock = Genesis('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', transactions)
transactions = []
blockchain.append(genesisBlock)
activeBlock = None
while (running == True):
    question = input("View the current hash / Guess hash / Broadcast hash / View a block's data")
    #print(blockchain)
    if  question[:15] == "viewcurrenthash":
        if len(blockchain) == 1:
            print(activeBlock.hash)
        else:
            print(activeBlock.hash())
    elif question == "guess":
        guesser = random.choice(participants)
        guesser.money += reward
        transactions = []
        blockchain.append(activeBlock)
        print(str(guesser.name) + " guessed the hash " + activeBlock.hash())
    elif question[:3] == "pay" and question.count(',') == 2 and question[4:question.find(',')]:
        names = []
        for person in participants:
            names.append(person.name)
        if question[4:question.find(',')] in names and question[question.find(',')+2:question.rfind(',')] in names:
            for person in participants:
                if question[4:question.find(',')] == person.name:
                    payer = person
                elif question[question.find(',')+2:question.rfind(',')] == person.name:
                    receiver = person
            if int(question[question.rfind(',')+2:]) > payer.money:
                print("This transaction cannot go through")
            else:
                transactions.append(payer.name + " pays " + receiver.name + " $" + question[question.rfind(',')+2:])
                payer.money -= int(question[question.rfind(',')+2:])
                receiver.money += int(question[question.rfind(',')+2:])
                print(payer.name + " pays " + receiver.name + " $" + question[question.rfind(',')+2:])
                if len(blockchain) == 1:                    
                    activeBlock = Block(blockchain[-1].hash, transactions, blockchain)
                else:
                    activeBlock = Block(blockchain[-1].hash(), transactions, blockchain)
    elif question == "pendingtransactions":
        print(transactions)
    elif question[:10] == "privatekey":
        for person in participants:
            if question[11:] == person.name:
                print(person.privateKey)
    elif question[:9] == "publickey":
        for person in participants:
            if question[10:] == person.name:
                print(person.publicKey)
    elif question[:21] == "viewblocktransactions":
        block = blockchain[int(question[22:])]
        print(block.block)
