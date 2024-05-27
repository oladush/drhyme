from unittest import TestCase
from drhyme import get_rhyme, get_simple_rhyme

class SimpleTestCase(TestCase):
    def test_droch(self):
        test_data = {
            'молоко': 'дрочоко',
            'лампа': 'дрочампа',
            'сметана': 'дрочана',
            'чимита': 'дрочита',
            'гачимучи': 'дрочимучи',
            'лалка': 'дрочанка'

        }

        for word, expected_rhyme in test_data.items():
            self.assertEqual(expected_rhyme, get_rhyme(word, 'дроч'))

    def test_simple_hui(self):
        test_data = {
            'молоко': 'хуёлоко',
            'лампа': 'хуямпа',
            'сметана': 'хуетана',
            'чимита': 'хуимита',
            'гачимучи': 'хуячимучи',
            'лалка': 'хуялка'
        }

        for word, expected_rhyme in test_data.items():
            self.assertEqual(expected_rhyme, get_simple_rhyme(word, 'хуй'),)

    def test_hui(self):
        test_data = {
            'молоко': 'хуёко',
            'лампа': 'хуямпа',
            'сметана': 'хуяна',
            'чимита': 'хуита',
            'гачимучи': 'хуимучи',
            'лалка': 'хуянка'
        }

        for word, expected_rhyme in test_data.items():
            self.assertEqual(expected_rhyme, get_rhyme(word, 'хуй'),)