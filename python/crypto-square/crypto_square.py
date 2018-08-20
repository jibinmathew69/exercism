def encode(plain_text):
    import re
    import math

    regex = re.compile('[^a-z0-9]')

    plain_text = plain_text.lower()
    plain_text = regex.sub("",plain_text)

    length = len(plain_text)

    square = math.sqrt(length)

    if isinstance(square,float):
        c = math.ceil(square)
        if square>(c-0.5):
            r = c
        else:
            r = math.floor(square)
    else:
        c=r=square

    plain_text += " "*((c*r)-length)

    plain_text = list(map(''.join, zip(*[iter(plain_text)] * c)))

    temp = ""
    for i in range(0,c):
        for j in range(0,r):
            temp+=plain_text[j][i]
        if i<c-1:
            temp += " "

    return temp