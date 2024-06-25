#!/usr/bin/python
# -*- coding: utf-8 -*-

#import sha256, algorithm used to hash blocks
from hashlib import sha256

#block class, used to create instances of block objects.
class Block():

    #the block's constructor that defines some attributes that will be modified later during the mining process
    def __init__(self, data, previous_hash):

        #these attributes will change later, exept for the genesis block, which will keep these attributes.
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = "GenisisBlockHash" * 4

    #hashing method that returns the sha256 hash of the block and its contents using utf-8 standard
    def hash_block(self):
        hashing_text =  str(self.nonce) + self.previous_hash + self.data
        h = sha256()
        h.update(hashing_text.encode('utf-8'))
        return h.hexdigest()

    #the method used to find a valid hash for a block according to the difficulty which is 4 for this blockchain
    def mine(self, difficulty):

        #this will loop until a hash is found that starts with the difficulty requirement.
        while self.hash[:difficulty] != '0' * difficulty:
            #the nonce is incrimented to then generate a new hash that might be valid.
            self.nonce += 1
            self.hash = self.hash_block()
        print(f"Hash found with nonce of: {self.nonce}")

    #dunder __str__ is used to print the contents of the block for the print_blockchain(self): method of the Blockchain class.
    def __str__(self):
        return f"Hash: {self.hash}\nPrevious Hash: {self.previous_hash}\nData: {self.data}\nNonce: {self.nonce}\n"

#the class used to create an instance of a blockchain.
class Blockchain():

    '''
    constructor for a blockchain.  It defines the actual chain attribute which is a list if all the blocks in
    the order they were created, and gives it its first block, the genesis block. the details of the genesis 
    block do not matter too much and have been given random values. the difficulty of the blockchain is also 
    defined as 4, so valid block hashes must start with 0000.
    '''
    def __init__(self):
        self.chain = [Block("genesis block","NA")]
        self.difficulty = 5

    #function used to add a block to the blockchain. blocks will be given their previous hash, mined for a valid hash
    #and appended to the end of the chain.
    def add_block(self, block):

        #self.chain[-1].hash returns the hash of the newest blockchain, the previous hash of the blockchain being added
        block.previous_hash = self.chain[-1].hash
        block.mine(self.difficulty)
        self.chain.append(block)

    #uses the blocks __str__ of the Block classmethod to print each attribute of each block, giving nice looking
    #insight of the blockchains structure.
    def print_blockchain(self):
        print("\n")
        for block in self.chain:
            print(block)
    
    def create_block(self):
        #prompt for the data that the block should have. (block content)
        block_data = input("\nBlock data: ")
        '''
        Then create a new block with that data and append it to the blockchain. 
        the empty string is there as the block does not yet know its previous hash,
        later decided by self.chain[-1].hash in the add block method.
        '''
        custom_block = Block(block_data, "")
        self.add_block(custom_block)

#The main function that runs first when the script is instantised. requests an action of the user that will execute
#different code depending on the action requested.
def main():

    #create an instance of the blockchain class
    blockchain = Blockchain()

    #This will loop until the user exits the script. 
    while 1 == 1:
        print("\nActions:")
        print("add = Add and mine a block")
        print("print = Print the blockchain")
        print("quit = Quit\n")

        #prompt the user to select an action from the abve actions
        action = input("Select an action: ")

        #a switch is used to perform an action depending on the value of action variable
        match action:
            case 'add':
                blockchain.create_block()
            #case 2, use the print_blockchain method of the blockchain which will then access the __str__ method of the block
            case 'print':
                blockchain.print_blockchain()
            
            #case 3, the script will terminate after printing a nice goodbye message
            case 'quit':
                print("Bye, have a nice day!")
                exit()
            
            # case _: will run if the user does not enter add, print or quit. will print a reminder of how to use the script.
            case _:
                print("Choose a valid action (add, print or quit)")

#this causes the main() function to be ran if the script is executed on the command line. it is the first code that runs.
if __name__ == '__main__':
    main()
