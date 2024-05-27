"""
      ／l、           drhyme - simple lib for find rhyme
    （ﾟ､ ｡ ７         author: zxolad
      l  ~ヽ         version: 0.0.1
      じしf_,)ノ
"""


from drhyme.internal.valuer import Valuer
from drhyme.internal.consts import ROOTS
from drhyme.internal.rhyme import get_rhyme
from drhyme.internal.utils import get_max_score
from drhyme.internal.simple_rhyme import get_simple_rhyme


VALUER = Valuer()


def get_rhymes_score(word: str) -> dict:
    '''
    :param word: word to find rhyme
    :return: dict with rhymes:scores
    '''
    rhymes = set()
    for root in ROOTS:
        rhymes.add(get_rhyme(word, root))
        rhymes.add(get_simple_rhyme(word, root))

    res = {}
    for rhyme in rhymes:
        res[rhyme] = VALUER.get_score(rhyme, orig=word)

    return res


def get_best_rhyme(word: str) -> str:
    '''
    :param word: word to find rhyme
    :return: rhyme with the best score
    '''
    rhymes_scores = get_rhymes_score(word)
    rhyme, _ = get_max_score(rhymes_scores)
    return rhyme


def rhymes_recount(selected_rhyme: str, orig: str):
    '''
    :param selected_rhyme: word to increment score
    :param orig: original word
    '''
    VALUER.manual.recount(selected_rhyme, orig)
