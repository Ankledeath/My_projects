import random
import animals
import stages

word_list = animals.animals_list

chosen_word = random.choice(word_list)

# Create blanks
display = []
for letter in chosen_word:
    display.append("_")

print(display)
print(stages.all_stages[0])
# Testing code
print(f"Solution is {chosen_word}")

attempt = 0
lives = 0
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter\n>").lower()
    count = 0
    guess_true = False

    # Check guessed letter
    for i in chosen_word:
        if i == guess:
            display[count] = guess
            guess_true = True
            count += 1
        else:
            count += 1

    if not guess_true:
        lives += 1

    print(display)
    print(stages.all_stages[int(lives)])

    if lives >= 6:
        print("You loose...")
        exit()

    # Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win!")



