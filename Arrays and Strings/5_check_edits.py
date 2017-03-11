import unittest
def checkEdits(original,edited):
    count = 0
    if original == edited:
        return True
    

    if len(original) != len(edited):
        count += abs(len(original)- len(edited))
    for char in edited:
        if (original+edited).count(char) % 2 == 1:
            count += 1
    
    if count == 0 or count == 1:
        return True
    else:
        return False

class Test(unittest.TestCase):
    data = [('pale','ple',True),('pales','pale',True),('pale','bale',True),('pale','bake',False)]

    def test_check_edits(self):
        for [original,edited,expected] in self.data:
            actual = checkEdits(original,edited)
            self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()