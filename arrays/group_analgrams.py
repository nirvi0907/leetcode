class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        eat, ate

        ['ate', 'eat', 'tan']
        ['tan']
        []
        ['', 'a']

        ['a', 'a']

        '''
        def get_sign(w):
            count = [0]*26
            for char in w:
                count[ord(char)-ord('a')]+=1
            pattern = ''
            for val in count:
                pattern+=str(val)+'-'
            return pattern

        sign_map = defaultdict(list)
        for word in strs:
            sign = get_sign(word)
            sign_map[sign].append(word)
        
        return list(sign_map.values())


#second appraoch
        class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            d[tuple(count)].append(s)

        return d.values()