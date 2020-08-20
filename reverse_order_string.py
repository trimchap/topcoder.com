def reverse_string(string):

    length = len(string)
    for i in range(int(length/2)):
        tmp = string[i]
        string[i] = string[-1-i]
        string[-1-i] = tmp
    return string


# TEST REVERSE STRING
# string = ['h','e','l','l','o']
string = ['h','e','l','l','o','w','o','r','l','d']
string = reverse_string(string)
print(string)

        

