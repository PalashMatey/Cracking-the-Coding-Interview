import unittest
from collections import Counter
def isPalindromePermutation(s):
    #A string can only be a palindrome permutation if there are exactly even number of charaters in a string
    if not s:
        return 'String is Empty'
    #Simple problem here, have to consider check the frequency of the characters.
    #If the string length is even, all characters must be divisible by 2.
    #If the string length is odd, only one character is odd,rest are even.
    s = s.strip().lower()
    if len(s) <= 2:
        return True
    dictStore = Counter(s)

    if len(s)%2 == 0:
        for k,v in dictStore.items():
            if v % 2 != 0:
                return False
        return True
    else:
        check = []
        for k,v in dictStore.items():
            if v % 2 != 0:
                check.append(k)
        if len(check) > 1:
            return False
        return True 
                
    
class Test(unittest.TestCase):
    data = [('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]
    def test_permutation_palindrome(self):
        for [test_string,expected] in self.data:
            actual = isPalindromePermutation(test_string)
            self.assertEqual(actual,expected)
if __name__ == '__main__':
    unittest.main()

