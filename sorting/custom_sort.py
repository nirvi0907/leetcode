dictionary = [26]*26
for index,char in enumerate(order):
    dictionary[ord(char)-ord('a')]=index

return ''.join(sorted( list(s), key=lambda x:dictionary[ord(x)-ord('a')]))

        