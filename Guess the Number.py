# Guess the Number Game
# by Raphael Gutierrez (https://facebook.com/raphael.gutierrez.17)
# Licensed under MIT (https://github.com/ralphgutz/Guess-The-Number/blob/master/LICENSE)

import time
import random

min = 1
max = 10

print("=" * 36)
print("= WELCOME TO GUESS THE NUMBER GAME =")
print("=" * 36)

start = input("\nStart the game? [Y/N] ")

def guess():
	time.sleep(1)
	print("\nRandom number has been generated.\n")
	time.sleep(1)
	guess_num = int(input(" Your guess number: "))

	rand_num = random.randint(min, max)

	if guess_num == rand_num:
		print("\n  YOU GOT IT!\n")

	elif guess_num == 0 or guess_num >= 11:
		print("\n  Your guess should be 1-10 only!\n")

	elif guess_num > rand_num and guess_num <= 10:
		print("\n  Your guess is high.\n")

	elif guess_num < rand_num and guess_num <= 10:
		print("\n  Your guess is low.\n")

if start == 'Y' or start == 'y':
	while start == 'Y' or start == 'y':
		guess()
		start = input("Start the game again? [Y/N] ")

		if start == 'N' or start == 'n':
			print("Exiting...")

elif start == 'N' or start == 'n':
	print("Exiting...")

else:
	print("Invalid Input!")