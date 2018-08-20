def prime_factors(natural_number):
    result = []
    for i in range(2, natural_number + 1):
        while natural_number % i == 0 and natural_number != 1:
            natural_number //= i
            result.append(i)
        if natural_number == 1:
            break
    return result