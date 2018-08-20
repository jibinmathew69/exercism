import string
alphabets = string.ascii_lowercase
def rotate(text, key):
    # return "".join(map(lambda x:rot(x,key),text))
    key = key%26
    calpha = alphabets[key:]+alphabets[:key]
    trans = str.maketrans(alphabets+alphabets.upper(),calpha+calpha.upper())
    return text.translate(trans)


# def rot(char,key):
    # flag = False
    # if char.isupper():
    #     char = char.lower()
    #     flag = True
    # if char not in alphabets:
    #     return char
    # x = alphabets.index(char)
    # key = (x + key) % 26
    # return alphabets[key] if flag==False else alphabets[key].upper()