from string import ascii_lowercase
def translate(text):
    words = text.split()
    return " ".join([process(word) for word in words])

def process(word):
    first = word[0]
    vowels = set("aeiou")
    if first in vowels or word.startswith("yt") or word.startswith("xr"):
        return "{0}ay".format(word)
    vowels.add('y')
    consonants = set(ascii_lowercase).difference(vowels)
    if first in consonants:
        cluster = first
        for letter in word[1:]:
            if letter in consonants:
                cluster += letter
            else:
                if cluster[-1] == "q" and letter == "u":
                    cluster += letter
                break
        return "{0}{1}ay".format(word[len(cluster):], cluster)
    return "{0}{1}ay".format(word[1:], word[0])
