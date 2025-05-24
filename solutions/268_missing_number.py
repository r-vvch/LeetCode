from typing import List


class Solution:
    # the best
    # O(n), O(1)
    def missingNumberFormula(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    # O(n), O(1)
    def missingNumberSum(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

    # O(n), O(1)
    def missingNumberXOR(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans

    # O(n), O(n)
    def missingNumberSet(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i

    missingNumber = missingNumberFormula


if __name__ == '__main__':
    solution = Solution()

    nums = [3,0,1]
    print(solution.missingNumber(nums)) # 2

    nums = [0,1]
    print(solution.missingNumber(nums)) # 2

    nums = [9,6,4,2,3,5,7,0,1]
    print(solution.missingNumber(nums)) # 8
