class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_length = 0
        length = 0
        for char in s:
            if char == " ":
                length = 0
            else:
                length += 1
            if length != 0:
                last_length = length
        return last_length       