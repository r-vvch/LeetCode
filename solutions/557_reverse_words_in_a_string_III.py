class Solution:
    def reverseWordsBest(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)

    def reverseWordsFaster(self, s: str) -> str:
        output = ''
        left = 0
        right = 0

        while left < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1

            right_it = right - 1
            while right_it >= left:
                output += s[right_it]
                right_it -= 1

            if right < len(s) and s[right] == ' ':
                output += ' '
                right += 1

            left = right

        return output

    def reverseWordsSimple(self, s: str) -> str:
        output = ''
        temp_wrd = ''
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != ' ':
                temp_wrd += s[i]
                i += 1
            output += temp_wrd[::-1]
            temp_wrd = ''
            output += ' '
            i += 1
        return output[:-1]

    reverseWords = reverseWordsBest


if __name__ == '__main__':
    solution = Solution()

    s = "Let's take LeetCode contest"
    print(solution.reverseWords(s)) # "s'teL ekat edoCteeL tsetnoc"
    assert solution.reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"

    s = "Mr Ding"
    print(solution.reverseWords(s)) # "rM gniD"
    assert solution.reverseWords(s) == "rM gniD"
