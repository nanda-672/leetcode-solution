class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0
        for i in range(len(s)):
            if i == len(s)-1:
                number += symbols[s[i]]
            elif symbols[s[i]] < symbols[s[i+1]]:
                number -= symbols[s[i]]
            else:
                number += symbols[s[i]]
        return number