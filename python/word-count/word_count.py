def word_count(phrase):
    words = phrase.split()
    # worddict = {}
    # for word in words:
    #     if word not in worddict:
    #         worddict[word] = 1
    #     else:
    #         worddict[word] += 1
    # return worddict
    from collections import Counter
    return Counter(words)