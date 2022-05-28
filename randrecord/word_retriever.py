import requests
import json

WORD_API_LINK = 'https://random-words-api.vercel.app/word'
WORD_FIELD = 'word'

def get_random_words(number_of_words=10):
    """
    Return a set of random unique words from the random-words-api.
    """
    words = set()

    while len(words) < number_of_words:
        respones = requests.get(WORD_API_LINK)
        if respones.status_code == 200:
            word_json = json.loads(respones.text)[0]
            word = word_json[WORD_FIELD]
            words.add(word)
        else:
            print(f"Error: {respones.status_code}")
            break

    return words
