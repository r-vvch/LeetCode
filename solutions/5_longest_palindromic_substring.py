class Solution:
    def longestPalindromeCenter(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str

    def longestPalindromeBrute(self, s: str) -> str:
        pal_out = ''
        for i in range(len(s)):
            for pal_end in range(i + 1, len(s) + 1):
                if s[i:pal_end] == s[i:pal_end][::-1] and pal_end - i > len(pal_out):
                    pal_out = s[i:pal_end]
        return pal_out

    def longestPalindromeManacher(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len = 1
        max_str = s[0]

        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0

        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while (i - dp[i]-1 >= 0 and
                   i + dp[i] + 1 < len(s) and
                   s[i - dp[i] - 1] == s[i + dp[i] + 1]):
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i - dp[i]:i + dp[i] + 1].replace('#', '')

        return max_str

    longestPalindrome = longestPalindromeCenter


if __name__ == '__main__':
    solution = Solution()

    s = "babad"
    print(solution.longestPalindrome(s)) # "bab"

    s = "cbbd"
    print(solution.longestPalindrome(s)) # "bb"

    s = "a"
    print(solution.longestPalindrome(s)) # "a"
