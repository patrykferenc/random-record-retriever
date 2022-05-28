# -*- coding: utf-8 -*-

from . import word_retriever, album_retriever

def main():
    """
    Run the randrecord search and display the information to the user.
    """
    words = word_retriever.get_random_words(1)
    print(f"Random words: {words}")
    recordings = album_retriever.get_random_recordings_from_words(words)
    print(f"Random recordings: {recordings}")
    

if __name__ == "__main__":
    main()