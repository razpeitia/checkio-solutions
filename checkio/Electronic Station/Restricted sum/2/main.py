def checkio(data):
    if data:
        return data.pop() + checkio(data)
    else:
        return 0

