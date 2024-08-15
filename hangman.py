import random

HANGMAN_PICS = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''',
    '''
     +---+
     |   |
     0   |
    /|\\  |
    / \\  |
         |
    ========='''
]

def get_random_word():
    words = [
        'python', 'javascript', 'hangman', 'coding', 'developer', 'algorithm',
        'function', 'variable', 'syntax', 'compiler', 'interpreter', 'loop',
        'conditional', 'iteration', 'recursion', 'array', 'list', 'dictionary',
        'tuple', 'string', 'integer', 'float', 'boolean', 'class', 'object',
        'inheritance', 'polymorphism', 'encapsulation', 'abstraction', 'module',
        'package', 'library', 'framework', 'debugging', 'testing', 'deployment',
        'version', 'control', 'repository', 'branch', 'commit', 'merge', 'pull',
        'push', 'fork', 'clone', 'issue', 'bug', 'feature', 'release', 'build',
        'continuous', 'integration', 'deployment', 'agile', 'scrum',
        'kanban', 'waterfall', 'sprint', 'backlog', 'retrospective', 'meeting',
        'standup', 'planning', 'review', 'demo', 'user', 'story', 'task',
        'subtask', 'priority', 'severity', 'estimation', 'velocity', 'burn',
        'down', 'chart', 'roadmap', 'milestone', 'deadline', 'goal', 'objective',
        'team', 'collaboration', 'communication', 'feedback', 'cycle',
        'release', 'candidate', 'production', 'environment', 'staging',
        'testing', 'development', 'hotfix'
    ]
    return random.choice(words)

def display_game_state(word, guessed_letters, attempts_left):
    print(HANGMAN_PICS[6 - attempts_left])
    display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
    print(f"Word: {display_word}")
    print(f"Attempts left: {attempts_left}")

def get_user_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            else:
                return guess
        else:
            print("Invalid input. Please enter a single letter.")

def play_hangman():
    word_to_guess = get_random_word()
    guessed_letters = set()
    attempts_left = 6

    while attempts_left > 0:
        display_game_state(word_to_guess, guessed_letters, attempts_left)
        guess = get_user_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not in the word. Attempts left: {attempts_left}")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word '{word_to_guess}' correctly!")
            break
    else:
        print(HANGMAN_PICS[-1])
        print(f"Game over. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    play_hangman()

