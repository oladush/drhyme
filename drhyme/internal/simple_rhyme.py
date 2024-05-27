import random
from drhyme.internal.utils import get_first_vowel

VOWEL_TO_RHYME = {
    'а': ('дроча', 'конча', 'хуя'), 'е': ('дроче', 'конче', 'хуе'), 'ё': ('дроче', 'конче', 'хуё'),
    'и': ('дрочи', 'кончи', 'хуи'), 'о': ('дрочё', 'кончё', 'хуё'), 'у': ('дрочу', 'кончу', 'хую'),
    'э': ('дроче', 'конче', 'хуе'), 'ю': ('дрочу', 'кончу', 'хую'), 'я': ('дроча', 'конча', 'хуя')
}


def get_simple_rhyme(word: str, root=None) -> str:
    # temp костыль
    if root == 'хуй':
        root = 'ху'
    def get_first_syllable(word: str) -> str:
        res = ""
        read_vowel = False

        for let in word:
            is_vowel = let in VOWEL_TO_RHYME
            if (read_vowel and not is_vowel):
                break
            if is_vowel:
                read_vowel = True
            res += let

        return res

    replace_to_list = VOWEL_TO_RHYME.get(get_first_vowel(word), [''])
    replace_to = ''
    if root:
        for repl in replace_to_list:
            if root in repl:
                replace_to = repl

    if not replace_to:
        replace_to = random.choice(replace_to_list)

    return word.replace(
        get_first_syllable(word),
        replace_to,
        1
    )