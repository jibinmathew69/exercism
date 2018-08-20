def largest_product(series, size):
    length = len(series)
    if size>length or size<0:
        raise ValueError("invalid size")

    import numpy

    max = -1
    for i in range(length-size+1):
        temp = [int(x) for x in series[i:i + size]]
        prod = numpy.prod(temp)
        if max < prod:
            max = prod

    return max