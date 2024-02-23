import unittest


def power_set(s):
    subsets = [frozenset()]
    for e in s:
        additions = set()
        for subset in subsets:
            additions.add(subset.union(e))
        subsets.extend(additions)
    return subsets


class Test(unittest.TestCase):
    def test_power_set(self):
        s = {'a', 'b', 'c', 'd'}
        ps = power_set(s)
        self.assertEqual(len(ps), 16)
        subsets = [set(), {'a'}, {'b'}, {'c'}, {'d'},
                   {'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {'b', 'c'}, {'b', 'd'}, {'c', 'd'},
                   {'a', 'b', 'c'}, {'a', 'b', 'd'}, {'a', 'c', 'd'}, {'b', 'c', 'd'}, s]
        self.assertEqual(set(ps), set([frozenset(s) for s in subsets]))


if __name__ == "__main__":
    unittest.main()
