'''
       tim-o(n)
       space-o(26)
        '''

        s_counter = Counter(s)
        order_set = set(order)
        res = ''
        for index, char in enumerate(order):
            if char in s_counter:
                res+=(char)*s_counter[char]
        # print(res)
        for index,char in enumerate(s):
            if char not in order_set:
                res+=char
        return res
        # s='abzc'
        '''
        another solution is to have a 26 size array, and note the index for each char present in order
        (this is our own dictionary)
        becuase as question has asked we want to sort the s string based on order
        initially rank for each char in dic is 26, then we are storing the indexes in order as rank for each char in dic

        then all we are doing is sort s string based on this dictionary
        '''
        # dictionary = [26]*26
        # for idx, char in enumerate(order):
        #     dictionary[ord(char)-ord('a')] = idx
        # return ''.join(sorted(s, key = lambda x:dictionary[ord(x)-ord('a')]))

        