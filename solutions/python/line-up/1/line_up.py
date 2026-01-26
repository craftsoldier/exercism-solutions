def line_up(name, number):
    call_one = ", you are the "
    call_two = " customer we serve today. Thank you!"

    remainder = number % 10
    prefix = "th"

    if remainder == 1:
        prefix = "st"
    elif remainder == 2:
        prefix = "nd"
    elif remainder == 3:
        prefix = "rd"
    
    remainder = number % 100
    
    if remainder in [11, 12, 13]:
        prefix = "th"

    call_out = name + call_one + str(number) + prefix + call_two
    return call_out
