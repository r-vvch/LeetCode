from typing import List

class Solution:
    letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def backtrack(i, comb):
            if i == len(digits):
                output.append(comb[:])
                return

            for letter in self.letter_map[digits[i]]:
                backtrack(i + 1, comb + letter)

        output = []
        backtrack(0, "")

        return output

    def letterCombinationsBrute(self, digits: str) -> List[str]:
        output = []
        if len(digits) > 0:
            for let_1 in self.letter_map[digits[0]]:
                if len(digits) > 1:
                    for let_2 in self.letter_map[digits[1]]:
                        if len(digits) > 2:
                            for let_3 in self.letter_map[digits[2]]:
                                if len(digits) > 3:
                                    for let_4 in self.letter_map[digits[3]]:
                                        output.append(let_1 + let_2 + let_3 + let_4)
                                else:
                                    output.append(let_1 + let_2 + let_3)
                        else:
                            output.append(let_1 + let_2)
                else:
                    output.append(let_1)
        return output


if __name__ == '__main__':
    solution = Solution()

    digits = "23"
    print(solution.letterCombinations(digits)) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    digits = ""
    print(solution.letterCombinations(digits)) # []

    digits = "2"
    print(solution.letterCombinations(digits)) # ["a","b","c"]

    digits = "67"
    print(solution.letterCombinations(digits))

    digits = "456"
    print(solution.letterCombinations(digits))

    digits = "4567"
    print(solution.letterCombinations(digits))
