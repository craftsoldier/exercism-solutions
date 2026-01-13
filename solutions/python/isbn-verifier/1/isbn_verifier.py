def is_valid(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")
    if len(isbn) != 10:
        return False

    result = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        result += int(isbn[i]) * (10 - i)

    # Handle last character
    if isbn[9].lower() == "x":
        result += 10
    elif isbn[9].isdigit():
        result += int(isbn[9])
    else:
        return False

    return result % 11 == 0
