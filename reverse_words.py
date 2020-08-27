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

def reverse_words(msg):
    # reverse the whole string so the words are in the right place
    reverse_string_in_place(msg, 0, len(msg)-1)
    print(msg)
    # then reverse the words in the string
    left_idx = 0
    right_idx = 0
    while right_idx < len(msg)-1:
        if msg[right_idx] == ' ' or msg[right_idx] == None:
            # found the end of the word, reverse it
            reverse_string_in_place(msg, right_idx-1, left_idx)
            left_idx = right_idx+1
        else:
            right_idx +=1

    return msg


def reverse_string_in_place(msg, left_idx, right_idx):
    for i in range(left_idx ,int(right_idx//2)+1):
        print(i,right_idx - i)
        msg[i], msg[right_idx - i] = msg[right_idx - i],msg[i]
    return msg
    

# Test
message = ['c','a','k','e',' ',
        'p','o','u','n','d',' ',
        's','t','e','a','l']
print(reverse_words(message))
# msg = reverse_string_in_place(message)
print(''.join(msg))