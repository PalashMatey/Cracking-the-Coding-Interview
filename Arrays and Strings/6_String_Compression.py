import unittest
from collections import Counter,OrderedDict
def stringCompression(s):
    
    if not s:
        return 'Empty String'
    
    s = s + '#'
    temp = []
    count = 1
    for i in xrange(1,len(s)): 
        if s[i] == s[i-1]:
            count += 1
        else:
            temp.extend(s[i-1])
            temp.extend(str(count))
            count = 1
    if len(''.join(temp)) > len(s):
        return s[:-1]

    return ''.join(temp) 

class Test(unittest.TestCase):
    data = [('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')]
    
    def test_check_compression(self):
        for [test_string,expected] in self.data:
            actual = stringCompression(test_string)
            self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()



