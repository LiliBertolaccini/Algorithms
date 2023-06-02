def is_anagram(first_string, second_string):

    word_one = str(first_string).lower()
    word_two = str(second_string).lower()
    sort_word_one = merge_sort(word_one)
    sort_word_two = merge_sort(word_two)
    is_equal = sort_word_one == sort_word_two
    if first_string == "" or second_string == "":
        return (sort_word_one, sort_word_two, False)
    return (sort_word_one, sort_word_two, is_equal)


def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    one = merge_sort(string[:mid])
    two = merge_sort(string[mid:])
    return merge(one, two)


def merge(left, right):
    qualquer = list(left + right)
    word = []
    left_index, right_index = 0, 0
    for general_index in range(len(left) + len(right)):
        if left_index >= len(left):
            qualquer[general_index] = right[right_index]
            right_index += 1
            word.append(qualquer[general_index])
        elif right_index >= len(right):
            qualquer[general_index] = left[left_index]
            left_index += 1
            word.append(qualquer[general_index])
        elif left[left_index] < right[right_index]:
            qualquer[general_index] = left[left_index]
            left_index += 1
            word.append(qualquer[general_index])
        else:
            qualquer[general_index] = right[right_index]
            right_index += 1
            word.append(qualquer[general_index])
    return "".join(word)
