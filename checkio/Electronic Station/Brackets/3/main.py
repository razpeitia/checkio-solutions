def checkio(data):
    stack = []
    lookup = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    for token in data:
        if token in "{[(":
            stack.append(token)
        elif token in "}])":
            if stack and lookup[token] == stack[-1]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"

