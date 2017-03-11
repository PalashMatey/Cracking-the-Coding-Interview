def urlify(s,n):
    s = s.rstrip().lstrip()
    return s.replace(' ','%20')
    


def main():
    s = 'Mr John Smith      '
    ans = urlify(s,13)
    print ans


if __name__ == '__main__':
    main()



