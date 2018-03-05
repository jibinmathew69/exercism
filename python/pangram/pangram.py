def is_pangram(sentence):
    import re

    return len(set("".join(re.findall("[a-z]+",sentence.lower())))) == 26