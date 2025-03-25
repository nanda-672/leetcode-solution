class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 1
        count = 0
        char_sample = []
        for char in s:
            if not (char in char_sample):
                count += 1
                if count >= ans:
                    ans = count
                char_sample.append(char)
            else:
                count = 0
                char_sample = []
        return ans
