def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    invertida = word[::-1]

    return word == invertida