import unittest

def number_needed(a, b):
    word_length = len(a + b)
    a1 = duplicateCount(a)
    b1 = duplicateCount(b)
    duplicate = 0

    for s in a1:
        if s in b1:
             t = (a1[s] * 2) if a1[s] == b1[s] else (min(a1[s], b1[s]) * 2)

             duplicate += (a1[s] * 2) if a1[s] == b1[s] else (min(a1[s], b1[s]) * 2)

    return (word_length - duplicate) if duplicate else word_length

def duplicateCount(arr):
    arr = sorted(arr)
    dup = {}
    for ch in arr:
        if ch in dup:
            dup[ch] += 1
        else:
            dup[ch] = 1

    return dup

#a = input().strip()
#b = input().strip()

#print(number_needed(a, b))


class MyTest(unittest.TestCase):
    def test1(self):
        a="cde"
        b="abc"
        self.assertEqual(number_needed(a, b), 4)
    def test2(self):
        a="bicycle"
        b="motorcycle"
        self.assertEqual(number_needed(a, b), 7)


if __name__ == '__main__':
    unittest.main()
