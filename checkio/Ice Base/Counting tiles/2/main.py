from math import ceil

def checkio(radius):
    def generate_points(n, i, j):
        return (
            (n - i, n - j),
            (n - i - 1, n - j - 1),
            (n - i - 1, n - j),
            (n - i, n - j - 1),
        )

    def is_inside_circle(radius, x, y):
        return (x*x + y*y) <= radius*radius

    def get_results(n, i, j, radius):
        return (is_inside_circle(radius, x, y) for x, y in generate_points(n, i, j))

    def is_solid(n, i, j, radius):
        return all(get_results(n, i, j, radius))

    def is_partial(n, i, j, radius):
        return any(get_results(n, i, j, radius))

    solid_count = 0
    partial_count = 0
    n = int(ceil(radius))
    for i in range(2*n):
        for j in range(2*n):
            if is_solid(n, i, j, radius):
                solid_count += 1
            elif is_partial(n, i, j, radius):
                partial_count += 1

    return [solid_count, partial_count]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"

