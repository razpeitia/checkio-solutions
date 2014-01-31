def checkio(input_data):
    'Return password of given cipher map'
    mapc, data = input_data

    def f(mapa, data):
        ans = []
        for i in range(4):
            for j in range(4):
                if mapa[i][j] == 'X':
                    ans.append(data[i][j])
        return ''.join(ans)

    def rotate(mapa):
        mapd = [[None] * 4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                mapd[i][j] = mapa[4 - j - 1][i]
        mapd = [''.join(i) for i in mapd]
        return mapd

    ans = []
    for i in range(4):
        ans.append(f(mapc, data))
        mapc = rotate(mapc)
    return ''.join(ans)


if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
    print('All ok')
