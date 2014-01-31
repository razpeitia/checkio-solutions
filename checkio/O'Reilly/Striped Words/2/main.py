# Solution for problem
# http://www.checkio.org/mission/striped-words/solve/
import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    words = [word.strip() for word in re.split(r'\s|,|\.|\?', text)]
    def is_valid(word):
        if not word.isalpha() or len(word) <= 1:
            return False
        return (
        all((char.upper() in VOWELS) for char in word[::2]) \
        and \
        all((char.upper() in CONSONANTS) for char in word[1::2]) \
        ) \
        or (\
        all((char.upper() in CONSONANTS) for char in word[::2]) \
        and \
        all((char.upper() in VOWELS) for char in word[1::2]) \
        )
    ans = sum(is_valid(word) for word in words)

    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

