def verify(isbn):
    isbn = isbn.replace("-","")
    import re
    pattern = re.compile("^\d{9}(?:\d{1})?X?$")
    if not pattern.match(isbn) or len(isbn)<10:
        return False

    isbn = list(isbn)
    j=0
    sum = 0
    for i in range(10,0,-1):
        if isbn[j] == 'X':
            sum+=10*i
            j+=1
            continue
        sum += (int(isbn[j])*i)
        j+=1

    return sum%11==0
