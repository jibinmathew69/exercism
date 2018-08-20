def square_of_sum(count):
    return int(((count*(count+1))/2)**2)


def sum_of_squares(count):
    return int(round(((count**3)/3)+((count**2)/2)+((count)/6)))


def difference(count):
    return square_of_sum(count)-sum_of_squares(count)
