import random


HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]

class Hangman():
    """
    The hangman game class with his methods
    """

    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self.word_to_guess))

    def find_indexes(self, letter):
        """
        Method that takes a letter and returns a list with his indexes in
        the word to guess
        :param letter: String, Letter to find his indexes
        """
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]

    def is_invalid_letter(self, input_):
        """
        Method to validate if an user input is not just a letter (it means the
        input is a number or a text with more than 1 char)
        :param input_: String, user input to be validated
        """
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game_status(self):
        """
        Method to print the word to guess blankspaces with the remaining
        attempts and the guessed letters
        """
        # We append withespaces both sides to make the game look prettier
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
        """
        Method to update the game progress with the guessed letters
        :param letter: String, Letter to be added to the game progress
        :param indexes: List, found occurrences (as indexes) of the given
                        letter in the word
        """
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\nPlease type a letter: ')
        return user_input

    def play(self):
        """
        Method to play the game, it prompts the user for a letter and plays
        the game until the user guesses the word or lose his attempts
        """
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('¡The input is not a letter!')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_progress:
                print('You already have guessed that letter')
                continue

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_progress.count('_') == 0:
                    print('\n¡Yay! You win!')
                    print('The word is: {0}'.format(self.word_to_guess))
                    quit()
            else:
                self.failed_attempts += 1
        print("\n¡OMG! You lost!")

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()