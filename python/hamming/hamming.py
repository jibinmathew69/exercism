def distance(strand_a, strand_b):
    length = len(strand_a)
    if length!=len(strand_b):
        raise ValueError('Length doesnt match')
    dist = 0
    for i in range(length):
        if strand_a[i]!=strand_b[i]:
            dist += 1
    return dist