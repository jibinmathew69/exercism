def is_isogram(string):
    string = string.lower().replace(" ","").replace("-","")
    length = len(string)

    return len(set(string)) == length
