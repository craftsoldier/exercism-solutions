import string

def is_pangram(sentence):
    sentence_lower = sentence.lower()
    for letter in string.ascii_lowercase:
        if letter not in sentence_lower:
            return False
    return True


