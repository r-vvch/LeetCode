from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        return []

    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    solution = Solution()

    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums, target)) # [0,1]
    assert solution.twoSum(nums, target) == [0, 1]

    nums = [3,2,4]
    target = 6
    print(solution.twoSum(nums, target)) # [1,2]
    assert solution.twoSum(nums, target) == [1, 2]

    nums = [3,3]
    target = 6
    print(solution.twoSum(nums, target)) # [0,1]
    assert solution.twoSum(nums, target) == [0, 1]

    nums = [2,5,5,11]
    target = 10
    print(solution.twoSum(nums, target)) # [1,2]
    assert solution.twoSum(nums, target) == [1, 2]
