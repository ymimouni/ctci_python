

def count_ways(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        a = 1
        b = 2
        c = 4
        for i in range(3, n):
            d = a + b + c
            a = b
            b = c
            c = d
        return d  # noqa


def test_count_ways():
    assert count_ways(5) == 13
    assert count_ways(0) == 0
    assert count_ways(-5) == 0
