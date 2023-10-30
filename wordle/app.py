

secret_word = "potato"
guess = ""
attempts = 0
max_attempts = 10

while guess != secret_word and attempts < max_attempts:
    current_attempts = max_attempts - attempts - 1
    guess = input("Enter guess: ")
    attempts += 1
    print("You have " + str(current_attempts) + " left!")

if guess == secret_word:
    print("You have won!")
else:
    print("Out of attempts. The secret word was:", secret_word)
