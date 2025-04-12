from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums
    
    def moveZeroesMy(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_init_len = len(nums)
        i = 0
        pop_counter = 0
        while i + pop_counter < nums_init_len:
            if nums[i] == 0:
                nums.pop(i)
                pop_counter += 1
                i -= 1
            i += 1
        nums.extend([0] * (pop_counter))

    def moveZeroesMyFast(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros_i = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_i.append(i)
        for i in range(1, len(zeros_i)):
            zeros_i[i] = zeros_i[i] - i
        for i in zeros_i:
            nums.pop(i)
        nums.extend([0] * len(zeros_i))


if __name__ == '__main__':
    solution = Solution()

    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)
    # assert nums == [1, 3, 12, 0, 0]

    nums = [0]
    solution.moveZeroes(nums)
    print(nums)
    # assert nums == [0]

    nums = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    solution.moveZeroes(nums)
    print(nums)
    # assert nums == [1,1,1,0,0,0,0,0,0]

