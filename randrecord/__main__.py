import sys
from . import word_retriever, album_retriever, presenter

MIN_NUMBER_OF_WORDS = 5
MAX_NUMBER_OF_WORDS = 20


def main():
    """
    Run the randrecord search and display the information to the user.
    """
    number_of_words = get_number_from_cli_argument()
    find_and_display_recordings(number_of_words)


def find_and_display_recordings(number=MIN_NUMBER_OF_WORDS):
    words = word_retriever.get_random_words(number)
    print('\nWords obtained fromt the random-words-api:\n')
    presenter.display_words(words)
    recordings = album_retriever.get_random_recordings_from_words(words)
    print('\nRecordings that match the word (artist - album - title):\n')
    presenter.display_recordings(recordings)


def get_number_from_cli_argument():
    """
    Return the number of words to be retrieved from the CLI argument.
    Make sure the number is between MIN_NUMBER_OF_WORDS and MAX_NUMBER_OF_WORDS.
    Exit otherwise.
    """
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        if number >= MIN_NUMBER_OF_WORDS and number <= MAX_NUMBER_OF_WORDS:
            return number
    print(
        f'Error: number of words must be between {MIN_NUMBER_OF_WORDS} and {MAX_NUMBER_OF_WORDS}')
    sys.exit(1)


if __name__ == "__main__":
    main()
