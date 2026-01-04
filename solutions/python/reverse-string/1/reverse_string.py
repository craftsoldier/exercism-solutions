def reverse(text):
    length = len(text) 

    reverse_text = ''

    for i in range(1, length + 1):
        reverse_text += text[-i]
        
    return reverse_text
