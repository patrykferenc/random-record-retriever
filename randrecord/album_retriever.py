import musicbrainzngs

musicbrainzngs.set_useragent(
    "Random Record Retriever",
    "0.1.0",
    "https://github.com/patrykferenc/random-record-retriever"
)


def get_random_recordings_from_words(words_list):
    """
    Return a set of entries ('word': 'artist - album - title') of informations about random unique recordings from the given words.
    """
    recordings = {}
    for word in words_list:
        recordings.update(get_random_recordings_from_word(word))
    return recordings


def get_random_recordings_from_word(word):
    """
    Return a set entry ('word': 'artist - album - title') of informations about a random unique recording from the given word.
    """
    recordings = musicbrainzngs.search_recordings(query=word, limit=1)
    recordings_list = recordings['recording-list']
    if len(recordings_list) > 0:
        recording = recordings_list[0]
        artist = recording['artist-credit-phrase']
        album = recording['release-list'][0]['title']
        title = recording['title']
        return {word: f"{artist} - {album} - {title}"}
    else:
        return {word: f"No recordings found for {word}"}
