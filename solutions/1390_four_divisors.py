from math import sqrt
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result_sum = 0
        for num in nums:
            divisors = [1, num]
            for iter_num in range(2, int(sqrt(num)) + 1):
                if len(divisors) > 4:
                    break
                if num % iter_num == 0:
                    divisors.append(iter_num)
                    if num // iter_num != iter_num:
                        divisors.append(num // iter_num)
            if len(divisors) == 4:
                result_sum += sum(divisors)
        return result_sum


if __name__ == '__main__':
    solution = Solution()

    nums = [21,4,7]
    print(solution.sumFourDivisors(nums)) # 32

    nums = [21,21]
    print(solution.sumFourDivisors(nums)) # 64

    nums = [1,2,3,4,5]
    print(solution.sumFourDivisors(nums)) # 0

    nums = [1,2,3,4,5,6,7,8,9,10]
    print(solution.sumFourDivisors(nums)) # 45
