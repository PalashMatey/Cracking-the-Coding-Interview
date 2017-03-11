import unittest
from collections import Counter
def checkPermutation(s1,s2):
    dictStore1, dictStore2 = map(Counter,(s1,s2))
    return dictStore1 == dictStore2

class Test(unittest.TestCase):
    dataTrue = [['abcd','dabc'] , ['1234','4321'], ['aaaa','aaaa'], ['a2bc3','23abc']]
    dataFalse = [['asdf','gfds'],['teyr','xvcb']]
    
    def test_cp(self):
        for test_case in self.dataTrue:
            actual = checkPermutation(test_case[0],test_case[1])
            self.assertTrue(actual)

        for test_case in self.dataFalse:
            actual = checkPermutation(test_case[0],test_case[1])
            self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()


