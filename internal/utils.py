from drhyme.internal.consts import VOWELS


def get_first_vowel(word: str) -> str:
    for let in word:
        if let in VOWELS:
            return let


def get_max_score(data: dict):
    max_score = 0
    selected = ''

    for word, score in data.items():
        if score > max_score:
            max_score = score
            selected = word

    return selected, max_score
