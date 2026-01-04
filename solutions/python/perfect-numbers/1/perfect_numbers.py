def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if (number <= 0):
        raise ValueError("Classification is only possible for positive integers.")

    factor_list = []

    for num in range(1, number):
        if (number % num == 0):
            factor_list.append(num)

    factor_sum = 0

    for factor in factor_list:
        factor_sum += factor

    if factor_sum == number:
        return 'perfect'
    elif factor_sum < number:
        return 'deficient'
    elif factor_sum > number:
        return 'abundant'

