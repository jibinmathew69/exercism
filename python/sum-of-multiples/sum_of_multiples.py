def sum_of_multiples(limit, multiples):
    mult = set()
    for i in multiples:
        mult = mult.union(set(range(i,limit,i)))

    return sum(mult)
