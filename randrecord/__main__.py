# -*- coding: utf-8 -*-

from . import word_retriever

def main():
    """
    Run the randrecord search and display the information to the user.
    """
    print(word_retriever.get_random_words(5))
    

if __name__ == "__main__":
    main()