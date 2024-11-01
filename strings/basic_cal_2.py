class Solution:
    def calculate(self, s: str) -> int:

        #using prev, to keep the value of previous number in case we reach * or /
        cur,prev = 0,0
        cur_operation = "+"
        res = 0

        i = 0
        while i < len(s):

            if s[i].isdigit():

                while i < len(s)and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1

                if cur_operation == "+":
                    res += cur
                    prev = cur
                elif cur_operation == "-":
                    res += -cur
                    prev = -cur

                elif cur_operation == "*":
                    #Reverse the last operation since * has priority
                    res -= prev
                    res += prev * cur
                    prev = prev * cur

                elif cur_operation == "/":
                    res -= prev
                    #using int and "/" since "//" with negative number does not truncate to zero
                    res += int(prev / cur)
                    prev = int(prev / cur)
            
                #Set cur to zero again to be ready for the next number
                cur = 0
            #If it is not digit and not an empty space:
            elif s[i] != " ":
                cur_operation = s[i]

            i += 1

        return res


