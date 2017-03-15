def isUnique(s):
    if not s:
        return None
    dictStore = {}
    for char in s:
        dictStore[char] = dictStore.get(char,0) + 1
    for v in dictStore.values():
        if v > 1:
            return False
    return True

def isUniqueNoAdditionalDataStructures(s):
    charList = list(s)
    charList.sort()
    for i in xrange(1,len(charList)):
        if charList[i] == charList[i-1]:
            return False
    return True

def main():
    s = 'Check if this string is unique'
    ans = isUnique(s)
    print ans
    ans2 = isUniqueNoAdditionalDataStructures(s)
    print ans2

if __name__ == '__main__':
    main()
    

        


