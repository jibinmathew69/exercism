def abbreviate(words):
    import re
    words = re.findall(r"[\w']+", words)
    return "".join([x[0].upper() for x in words])
