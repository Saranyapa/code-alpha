import random
word_list = ['python', 'hangman', 'challenge', 'programming', 'random', 'function', 'winner', 'loser']

def choose_word():
    return random.choice(word_list)

def play_hangman():
    word_to_guess = choose_word()
    word_length = len(word_to_guess)
    display = ['_' for _ in range(word_length)]
    guessed_letters = []
    attempts_left = 3
    
    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters: {' '.join(display)}")
    
    while attempts_left > 0 and '_' in display:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess not in word_to_guess:
            print(f"Sorry, '{guess}' is not in the word. You lose a life.")
            attempts_left -= 1
            guessed_letters.append(guess)
        else:
            print(f"Good job! '{guess}' is in the word!")
            guessed_letters.append(guess)
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    display[i] = guess
        
        print(f"Word: {' '.join(display)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    if '_' not in display:
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you lost. The word was '{word_to_guess}'.")

if _name_ == "_main_":
    play_hangman()
