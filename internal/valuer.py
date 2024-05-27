import sqlite3
import pymorphy3

from drhyme.internal.consts import DB_PATH, SCORE_STEP_INCREMENT, SCORE_STEP_DECREMENT


class ManualValuer:
    def __init__(self, db='scores.sqlite'):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            word TEXT,
            orig TEXT,
            score REAL
        )
        ''')
        cursor.close()
        self.conn.commit()

    def insert_or_update_score(self, word, score, orig):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT id FROM scores WHERE word = ?
        ''', (word,))
        result = cursor.fetchone()

        if result:
            cursor.execute('''
            UPDATE scores SET score = ? WHERE word = ?
            ''', (score, word))
        else:
            cursor.execute('''
            INSERT INTO scores (word, score, orig)
            VALUES (?, ?, ?)
            ''', (word, score, orig))

        self.conn.commit()

    def get_score(self, word):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT word, score FROM scores WHERE word = ?
        ''', (word,))
        result = cursor.fetchone()
        return result

    def recount(self, word, orig):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT id, word, orig, score FROM scores WHERE orig = ?
        ''', (orig,))
        result = cursor.fetchall()

        if not result:
            raise Exception("Can't find words in local db")

        for entry in result:
            id_, rhyme, orig, score = entry
            if word == rhyme:
                score += SCORE_STEP_INCREMENT
                score = 1.0 if score > 1.0 else score
            else:
                score -= SCORE_STEP_DECREMENT
                score = 0.0 if score < 0.0 else score

            cursor.execute(
                "UPDATE scores SET score = ? WHERE id = ?",
                (score, id_)
            )
            self.conn.commit()


class Valuer:
    def __init__(self):
        self.morph = pymorphy3.MorphAnalyzer()
        self.manual = ManualValuer(db=DB_PATH)

    def get_score(self, word, orig):
        morph_score = self.morph.parse(word)[0].score

        if self.manual.get_score(word) is None:
            self.manual.insert_or_update_score(word, morph_score, orig)

        return self.manual.get_score(word)[1]
