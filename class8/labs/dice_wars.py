"""
dice_wars.py
===
Break down your problem using a flow chart, pseudocode, etc.  Here's a basic list of what should happen:
1. Print out ASCII art!!!
   ------
 /      /|  ~Dice Warz~
 ------| |
 |     | |
 |     |/
 ------
2. Keep track of scores using a dictionary
3. Loop forever
4. Ask for command
5. If command is roll, roll random dice for computer and player
6. Determine who wins (3 states: computer wins, player wins or tie)
7. For each state add scores appropriately, and print out both rolls and scores
8. If command is quit, then exit the game
9. If the command is not quit or roll, say "I don't know that command"
"""

import random
print """   ------
 /      /|  ~Dice Warz~
 ------| |
 |     | |
 |     |/
 ------"""

scores={"player":0,"computer":0}
 
while True:
		print "roll or quit?"
		command = raw_input(">")
		if command == "roll":
			computer_roll = random.randint(1,6)
			player_roll = random.randint(1,6)
			print "player roll %s, computer roll %s " % (player_roll, computer_roll)
			
			if player_roll > computer_roll:
					print "player won"
					scores['player']+= 1
			elif player_roll < computer_roll:
					print "computer won!"
					scores['computer'] += 1
		elif command == "quit":
				exit()