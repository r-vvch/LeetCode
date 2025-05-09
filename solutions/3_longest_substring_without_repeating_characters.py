class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, len(char_set))
        
        return max_len


if __name__ == '__main__':
    solution = Solution()

    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s)) # 3

    s = "bbbbb"
    print(solution.lengthOfLongestSubstring(s)) # 1

    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s)) # 3

    s = " "
    print(solution.lengthOfLongestSubstring(s)) # 1

    s = "dvdf"
    print(solution.lengthOfLongestSubstring(s)) # 3
