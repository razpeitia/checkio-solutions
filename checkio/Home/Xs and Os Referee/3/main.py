def checkio(game_result):
    x = set(['X'])
    o = set(['O'])
    
    def win(portion):
        if portion == x:
            return "X"
        elif portion == o:
            return "O"
    
    for row in game_result:
        row = set(row)
        result = win(row)
        if result is not None:
            return result
    
    for column in zip(*game_result):
        column = set(column)
        result = win(column)
        if result is not None:
            return result
    
    diagonal = set([game_result[i][i] for i in range(3)])
    inv_diagonal = set([game_result[i][2-i] for i in range(3)])
    
    result = win(diagonal)
    if result is not None:
        return result
        
    result = win(inv_diagonal)
    if result is not None:
        return result
        
    return "D"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"


