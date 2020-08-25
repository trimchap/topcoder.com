def reverse_words_not_in_place(message):
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

def reverse_string_in_place(msg):
    for i in range(int(len(msg)//2)):
        msg[i],msg[-1-i] = msg[-1-i],msg[i]
    return msg
    

# Test
message = ['c','a','k','e',' ',
        'p','o','u','n','d',' ',
        's','t','e','a','l']
# print(reverse_words(message))
msg = reverse_string_in_place(message)
print(''.join(msg))