from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 0
        for num in nums:
            index ^= num
        return index


if __name__ == '__main__':
    solution = Solution()

    nums = [2,2,1]
    print(solution.singleNumber(nums)) # 1

    nums = [4,1,2,1,2]
    print(solution.singleNumber(nums)) # 4

    nums = [1]
    print(solution.singleNumber(nums)) # 1
