secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):           #LOOP CONTINUES UNTIL SECRET WORD IS FOUND OR OUT OF GUESSES
    if guess_count < guess_limit:                             #ENSURES GUESS COUNT DOESN'T GO OVER 3
        guess = input("Guess the word: ")
        guess_count += 1
    else:
        out_of_guesses = True                                 #OUT OF GUESSES

if out_of_guesses:
    print("Out of guesses, you LOSE!!!")
else:
    print("You Win!")
