import random

print("Welcome to Guess The Number")
print("\nIn this game you have to guess the right number between 0 and 100")
print("Try to guess as fast as you can\n")
the_number = random.randint(1, 100)
guess = int(input("Your guess: "))
tries = 1
while guess != the_number:
	if guess > the_number:
		print("Less...")
	else:
		print("More...")
	guess = int(input("Your guess: "))
	tries += 1
print("Congratulations, number", the_number, "was the right number. You have tried", tries, "times.")
input("\nPress Enter to exit.")