from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            return digits[:-1] + [digits[-1] + 1]
        new_digits = [0] + digits
        new_digits[-1] += 1
        i = len(new_digits) - 1
        while i > 0 and new_digits[i] == 10:
            new_digits[i] = 0
            new_digits[i - 1] += 1
            i -= 1
        if new_digits[0] == 0:
            new_digits = new_digits[1:]
        return new_digits


class SolutionShort:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
        if carry:
            digits = [1] + digits
        return digits


class SolutionOneLiner:
    def plusOne(self, digits: List[int]) -> List[int]:
         return list(map(int,str(int(''.join(map(str, digits))) + 1)))


if __name__ == '__main__':
    solution = SolutionOneLiner()

    digits = [1,2,3]
    print(solution.plusOne(digits)) # [1,2,4]

    digits = [4,3,2,1]
    print(solution.plusOne(digits)) # [4,3,2,2]

    digits = [9]
    print(solution.plusOne(digits)) # [1,0]
