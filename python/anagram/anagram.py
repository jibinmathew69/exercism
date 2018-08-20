from collections import Counter
def detect_anagrams(word, candidates):
    word = Counter(first_lower(word))
    return list(filter(lambda x:word == Counter(first_lower(x)),candidates))

def first_lower(s):
   return s[0].lower()+s[1:] if len(s) != 0 else s