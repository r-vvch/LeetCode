from collections import Counter, defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_freq = Counter()
        max_length = 0
        start_index = 0
        for end_index, char in enumerate(s):
            char_freq[char] += 1
            while len(char_freq) > 2:
                char_freq[s[start_index]] -= 1
                if char_freq[s[start_index]] == 0:
                    del char_freq[s[start_index]]
                start_index += 1
            max_length = max(max_length, end_index - start_index + 1)
        return max_length

    def lengthOfLongestSubstringTwoDistinctBrute(self, s: str) -> int:
        max_len = 0
        for left in range(len(s)):
            let_dict = defaultdict(int)
            for right in range(left, len(s)):
                let_dict[s[right]] += 1
                if len(let_dict) > 2 or right == len(s) - 1:
                    if right - left + (right == len(s) - 1) > max_len:
                        max_len = right - left + (right == len(s) - 1)
                    break
        return max_len


if __name__ == '__main__':
    solution = Solution()

    s = "eceba"
    print(solution.lengthOfLongestSubstringTwoDistinct(s)) # 3

    s = "ccaabbb"
    print(solution.lengthOfLongestSubstringTwoDistinct(s)) # 5
