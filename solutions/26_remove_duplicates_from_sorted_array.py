from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        out_len = 0
        i = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[out_len]:
                out_len += 1
                nums[out_len] = nums[i]
        return out_len + 1


if __name__ == '__main__':
    solution = Solution()

    nums = [1,1,2]
    print(solution.removeDuplicates(nums)) # 2
    print(nums) # [1,2,_]

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums)) # 5, nums = [0,1,2,3,4,_,_,_,_,_]
    print(nums) # [0,1,2,3,4,_,_,_,_,_]

    for nums, expectedNums in [
        ([1,1,2], [1,2]),
        ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4])
    ]:
        k = solution.removeDuplicates(nums)
        assert k == len(expectedNums)
        for i in range(0, k):
            assert nums[i] == expectedNums[i]
