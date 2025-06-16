from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_cache = {0: -1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]
            remainder %= k
            if remainder not in remainder_cache:
                remainder_cache[remainder] = i
            elif i - remainder_cache[remainder] >=2:
                return True
        return False

    def checkSubarraySumBrute(self, nums: List[int], k: int) -> bool:
        def isGoodSubarray(arr: List[int]) -> bool:
            if len(arr) < 2 or sum(arr) % k != 0:
                return False
            return True

        for left in range(len(nums) - 1):
            for right in range(left + 1, len(nums) + 1):
                if isGoodSubarray(nums[left:right]):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()

    nums = [23,2,4,6,7]
    k = 6
    print(solution.checkSubarraySum(nums, k)) # True

    nums = [23,2,6,4,7]
    k = 6
    print(solution.checkSubarraySum(nums, k)) # True

    nums = [23,2,6,4,7]
    k = 13
    print(solution.checkSubarraySum(nums, k)) # False

    nums = [0,0]
    k = 1
    print(solution.checkSubarraySum(nums, k)) # True
