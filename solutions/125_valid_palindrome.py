class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = ''.join(filter(str.isalnum, s.lower()))
        if formatted_s == formatted_s[::-1]:
            return True
        else:
            return False

    def isPalindromeLowLevel(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start <= end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True


if __name__ == '__main__':
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    # true
    # Explanation: "amanaplanacanalpanama" is a palindrome.
    assert solution.isPalindrome(s) == True
    assert solution.isPalindromeLowLevel(s) == True

    s = "race a car"
    # false
    # "raceacar" is not a palindrome.
    assert solution.isPalindrome(s) == False
    assert solution.isPalindromeLowLevel(s) == False

    s = " "
    # true
    # Explanation: s is an empty string "" after removing non-alphanumeric characters.
    assert solution.isPalindrome(s) == True
    assert solution.isPalindromeLowLevel(s) == True

    s = "0P"
    # false
    assert solution.isPalindrome(s) == False
    assert solution.isPalindromeLowLevel(s) == False

    # print(solution.isPalindromeLowLevel(s))
