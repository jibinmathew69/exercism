def slices(series, length):
    start = 0
    end = length
    leng = len(series)
    seq = []

    if end>leng or length <1:
        raise ValueError("invalid")

    while end<=leng:
        seq.append([int(x) for x in list(series[start:end])])
        start += 1
        end += 1



    return seq