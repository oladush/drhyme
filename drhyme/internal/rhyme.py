import random
import rusyllab

from drhyme.internal.utils import get_first_vowel
from drhyme.internal.consts import ROOTS, CONSONANTS
from drhyme.internal.simple_rhyme import get_simple_rhyme


REPLACEABLE_ENDS = {
    'ка': {'о': 'онка', 'и': 'инка',  'default': 'анка'},
    'ки': {'default': 'ки'},
    'ры': {'default': 'оры'},
    'ре': {'default': 'ре'},
    'га': {'default': 'ига'},
    'на': {'default': 'ена'},
    'сы': {'default': 'есы'},
    'па': {'default': 'ампа'}
}

POST_RHYME_REPLACE = {
    'йа': 'я', 'йе': 'е', 'йё': 'ё',
    'йи': 'и', 'йо': 'ё', 'йу': 'ю',
    'йэ': 'е', 'йю': 'ю', 'йя': 'я'
}


def get_rhyme(word: str, root=None):
    word = word.lower()
    syllables = rusyllab.split_words([word])

    if not syllables:
        return ''

    if len(syllables) == 1:
        return get_simple_rhyme(word)

    if root:
        syllables[0] = root
    else:
        syllables[0] = random.choice(ROOTS)

    if len(syllables) > 1:
        syllables[1] = ''.join(syllables[1:])
        syllables = syllables[:2]
        if syllables[1] in REPLACEABLE_ENDS:
            first_vowel = get_first_vowel(word)
            replaceable_to_vowel = REPLACEABLE_ENDS[syllables[1]]
            syllables[1] = replaceable_to_vowel[first_vowel] \
                if first_vowel in replaceable_to_vowel \
                else replaceable_to_vowel['default']

        elif syllables[1][0] in CONSONANTS:
            syllables[1] = syllables[1][1:]

    result = ''.join(syllables)

    for rep in POST_RHYME_REPLACE:
        result = result.replace(rep, POST_RHYME_REPLACE[rep])

    return result