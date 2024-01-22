class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        s = s.strip()

        if not s:
            return 0
            
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        num = int(s)
        num*=sign

        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        
        return num 
    
solution =Solution()
s=input()
result=solution.myAtoi(s)