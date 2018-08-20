def sieve(limit):
    i = 2
    marked = set()
    prime = []
    while i<=limit:
        if i in marked:
            i += 1
            continue
        prime.append(i)
        marked = marked.union(set(range(i,limit+1,i)))
        i+=1

    return prime