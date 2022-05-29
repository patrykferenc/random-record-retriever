
def display_recordings(recordings):
    """
    Display the recordings to the user ordered by the word.
    """
    for word in sorted(recordings):
        print(f"{word}: {recordings[word]}")


def display_words(words):
    """
    Display the words to the user in alphabetical order.
    """
    for word in sorted(words):
        print(word)
