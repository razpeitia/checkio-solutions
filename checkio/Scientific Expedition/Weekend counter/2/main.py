from datetime import date
from datetime import timedelta


def next_day(some_date, day):
    "day: 0 - monday ... 6 - sunday"
    offset = ((7 + day) - some_date.weekday()) % 7
    return some_date + timedelta(days=offset)

def count_days(from_date, to_date, day):
    new_from_date = next_day(from_date, day)
    if new_from_date > to_date:
        return 0
    else:
        return ((to_date - new_from_date).days / 7 + 1)

def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    sats = count_days(from_date, to_date, 5)
    suns = count_days(from_date, to_date, 6)
    return sats + suns

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"


