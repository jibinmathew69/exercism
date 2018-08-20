import string
alphabets = string.ascii_lowercase


def encode(plain_text):
    import re
    calpha = alphabets[::-1]
    trans = str.maketrans(alphabets + alphabets.upper(), calpha + calpha)
    cipher = re.sub(r'[\W_]+', '', plain_text).translate(trans)
    return " ".join(list((cipher[0 + i:5 + i] for i in range(0, len(cipher), 5))))


def decode(ciphered_text):
    calpha = alphabets[::-1]
    trans = str.maketrans(calpha + calpha.upper(), alphabets + alphabets.upper())
    return ciphered_text.replace(" ","").translate(trans)
