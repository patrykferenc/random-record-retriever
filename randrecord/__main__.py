from . import word_retriever, album_retriever, presenter


def main():
    """
    Run the randrecord search and display the information to the user.
    """
    words = word_retriever.get_random_words(5)
    print('\nWords obtained fromt the random-words-api:\n')
    presenter.display_words(words)
    recordings = album_retriever.get_random_recordings_from_words(words)
    print('\nRecordings that match the word (artist - album - title):\n')
    presenter.display_recordings(recordings)


if __name__ == "__main__":
    main()
