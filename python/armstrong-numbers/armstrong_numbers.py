def is_armstrong(number):
    numb = str(number)
    exp = len(numb)
    num = sum(map(lambda x: int(x)**exp, numb))
    return num == number