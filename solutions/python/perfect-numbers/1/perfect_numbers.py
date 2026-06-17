def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 :
        raise ValueError('Classification is only possible for positive integers.')
    sum = 0
    for i in range(number):
        i += 1
        if number % i == 0 and i != number:
            sum += i
    if sum == number :
        return 'perfect'
    elif sum > number:
        return 'abundant'
    else:
        return 'deficient'
