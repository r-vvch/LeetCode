from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set_len_before = len(nums_set)
            nums_set.add(num)
            if len(nums_set) == nums_set_len_before:
                return num


class SolutionO1:
    def repeatedNTimes(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
            if i + 2 < len(nums):
                if nums[i] == nums[i + 2]:
                    return nums[i]
        return nums[0]


if __name__ == '__main__':
    solution = SolutionO1()

    nums = [1,2,3,3]
    print(solution.repeatedNTimes(nums)) # 3

    nums = [2,1,2,5,3,2]
    print(solution.repeatedNTimes(nums)) # 2

    nums = [5,1,5,2,5,3,5,4]
    print(solution.repeatedNTimes(nums)) # 5
