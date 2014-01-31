#Your code here
#You can import some modules or create additional functions
from collections import Counter

def checkio(data):
    c = Counter(data)
    return [i for i in data if c[i] > 1]

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#or remove elements from original list (but it's bad practice for many real cases)
#Loop over original list


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
