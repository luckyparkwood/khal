secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and out_of_guesses == False:
    if guess_count < guess_limit:
       guess = input("Guess the secret word: ")
       guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses == True:
    print("Sorry! you ran out of guesses!")
else:
    print("Congrats! You guessed the secret word!")