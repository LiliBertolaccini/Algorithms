def is_palindrome_recursive(word, low_index, high_index):
    #word_list = ["word", "low_index", "high_index"]

# def check_palindromes(words):
#    lista = []
#    for word in words:
#        check_palindromes = is_palindrome_recursive(word)
#        lista.append(check_palindromes)
#    return list

#word_list = ["amor", "prova", "ola"]
#palindrome_results = check_palindromes(word_list)

#print(palindrome_results)
    if low_index >= high_index:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

def check_palindromes(words):
    list = []
    for word in words:
        check_palindromes = is_palindrome_recursive(word, 0, len(word) - 1)
        list.append(check_palindromes)
    return list

word_list = ["amor", "prova", "ola"]
palindrome_results = check_palindromes(word_list)

print(palindrome_results)
    #"""Faça o código aqui."""
raise NotImplementedError
