# Bitcoin Simulation

Bitcoin Simulation is a python program that simulates a cryptocurrency blockchain and gives the user complete control over the processed transactions. The user also has access to parameters such as the number of participants, how much money they have, and has access to view hash codes, private keys and public keys.

#Comprehensive Examination

In regards to the comprehensive examination, I nearly achieved everything I wanted to do with this program. The goal was to make a sort of cryptocurrency that would work. However, I was not able to implement all of the aspects of a cryptocurrency because of my lack of knowledge in the field of cryptography. I was not able to implement the digital signature. This feature makes it so that each person can digitally sign transactions that they put through, but this is actually very complicated to do.

In addition, instead of having a form of cryptocurrency where each participant has their own copy of the blockchain, I made it so that there is only one blockchain. This is because the idea of cryptocurrency does not really make sense in settings with small populations, as one person can easily forge multiple transactions.

The idea of bitcoin is that everyone is protected from hacking because in order for a blockchain to be hacked, someone would have to mine more bitcoins than everyone else combined on the network. This would require a tremendous amount of computing power, however that would be possible in this simulation with low numbers of participants.

#Sources

The sources I used to make this simulation are all part of the attached microsoft word file. In addition, my notes of how bitcoin works are all there, I would primarily recommend reading the three paragraphs with highlighted headers. The rest of the file is mostly notes to myself when I was making this program.

## Installation

In order to use this program, the python IDLE environment must be used. Python can be installed using the following link: https://www.python.org/downloads/
This program can then be opened in the idle, and the code can be launched by going to run --> run module or simply by pressing F5. The commands outlined below can then be used by simply typing them into the IDLE Shell.

## Usage

Phase 1 - Parameters:

# add a participant and an associated amount of money (do not include brackets, only commas). The name must also be unique and can only include numbers and letters.
add [name of participant (no spaces)], [amount of money]

# delete a participant
delete [name of participant]

# print list of participants and amount of money
list

# continue to next phase
continue

Phase 2 - Simulation:

#View the hash of current block to be mined, only works once there is at least one pending transaction
viewcurrenthash

#Random person guesses the current hash
guess

#View a previous block's transactions (the first block has block index 0, and so on)
viewblocktransactions [block index]

#Person X pays Person Y a certain amount of money
This command only works once there are pending transactions
pay [name of participant paying money], [name of participant receiving money], [amount of money]

#Print the pending transactions (transactions that are not yet in a block)
pendingtransactions

#Print the private key of a participant
privatekey [name of participant]

#Print the public key of a participant
publickey [name of participant]