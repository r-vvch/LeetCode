class Solution:
    def addNumbers(self, num1: str, num2: str, numext: str) -> tuple[str, str]:
        summ = int(num1) + int(num2) + int(numext)
        if summ < 10:
            return '0', str(summ)
        else:
            return str(summ)[0], str(summ)[1]

    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            return self.addStrings(num2, num1)

        num2 = '0' * (len(num1) - len(num2)) + num2

        result = ['0'] * (len(num1) + 1)

        for i in range(1, len(num1) + 1):
            temp = self.addNumbers(num1[-i], num2[-i], result[-i])
            result[-i - 1], result[-i] = temp

        if result[0] == '0':
            result = result[1:]

        return ''.join(result)


class SolutionFast:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            digit1 = 0
            if i >= 0:
                digit1 = ord(num1[i]) - ord('0')

            digit2 = 0
            if j >= 0:
                digit2 = ord(num2[j]) - ord('0')

            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(chr(total % 10 + ord('0')))

            i -= 1
            j -= 1

        return ''.join(result[::-1])


if __name__ == '__main__':
    solution = Solution()

    num1 = "11"
    num2 = "123"
    print(solution.addStrings(num1, num2)) # "134"

    num1 = "456"
    num2 = "77"
    print(solution.addStrings(num1, num2)) # "533"

    num1 = "0"
    num2 = "0"
    print(solution.addStrings(num1, num2)) # "0"

    num1 = "0"
    num2 = "9"
    print(solution.addStrings(num1, num2)) # "0"
