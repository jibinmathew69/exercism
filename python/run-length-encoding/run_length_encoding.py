def decode(string):
    str1 = ""
    length = len(string)
    curnum = ""
    for i in range(length):
        if string[i].isnumeric():
            curnum+=string[i]
            continue
        if not string[i].isnumeric() and i-1 >-1 and string[i-1].isnumeric():
            str1 += (string[i]*int(curnum))
            curnum = ""
        else:
            str1 += string[i]
    return str1


def encode(string):
    import itertools
    groups = [(len(list(n)),c) for c, n in itertools.groupby(string)]
    return ''.join(str(n) + c if n > 1 else c for n, c in groups)

