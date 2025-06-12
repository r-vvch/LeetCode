from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output


if __name__ == '__main__':
    solution = Solution()

    nums = [1,2,3,4]
    print(solution.productExceptSelf(nums)) # [24,12,8,6]

    nums = [-1,1,0,-3,3]
    print(solution.productExceptSelf(nums)) # [0,0,9,0,0]
