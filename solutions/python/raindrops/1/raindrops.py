def convert(number):
    if ((number % 3) != 0) and ((number % 5) != 0) and ((number % 7) != 0):
        return str(number)

    expletives = ['Pling', 'Plang', 'Plong']

    word = ''    

    if ((number % 3) == 0):
        word += expletives[0]

    if ((number % 5) == 0):
        word += expletives[1]

    if ((number % 7) == 0):
        word += expletives[2]

    return word
