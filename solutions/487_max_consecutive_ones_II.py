from typing import List


class Solution:
    def findMaxConsecutiveOnesFast(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        for x in nums:
            zeros += x ^ 1
            if zeros > 1:
                zeros -= nums[left] ^ 1
                left += 1
        return len(nums) - left

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l_nums = len(nums)

        left = 0
        zeros = 0
        ans = 0

        for right in range(l_nums):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        if ans == l_nums:
            return ans
        else:
            return ans + 1


if __name__ == '__main__':
    solution = Solution()

    nums = [1,0,1,1,0]
    print(solution.findMaxConsecutiveOnes(nums)) # 4

    nums = [1,0,1,1,0,1]
    print(solution.findMaxConsecutiveOnes(nums)) # 4
