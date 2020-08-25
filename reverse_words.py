def reverse_words(message):
    result = ''
    next_word = ''

    for char in message:
        if char != ' ':
            next_word = next_word + char
        else:
            result = char + next_word + result
            next_word = ''
    result = next_word + result

    return result

# Test
message = ['c','a','k','e',' ',
        'p','o','u','n','d',' ',
        's','t','e','a','l']
print(reverse_words(message))