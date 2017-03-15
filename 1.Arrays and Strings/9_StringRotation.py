def isSubstring(original,sub):
    return original.find(sub) != -1

    
def stringRotationRecognition(s1,s2):
    if len(s1) == len(s2):
        return isSubstring(s1 + s1,s2)
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
    

