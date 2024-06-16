word = "word"

chance = 5

game_over = False

user_letters = []

while not game_over:

    for letter in word:
        if letter.lower() in user_letters:
            print(letter, end=" ")
        else:
            print("_", end="")

    user_guess = input(f" [{chance}]Chances left, Guess the word, letter by letter: ")
    user_letters.append(user_guess.lower())

    if user_guess.lower() not in word.lower():
        chance -= 1
        if chance == 0:
            break

    game_over = True
    for letter in word:
        if letter.lower() not in user_letters:
            game_over = False

if game_over:
    print(f"You won the game, the word was ---> {word} <---")
else:
    print("Game Over, You are hanging in the fan!")
