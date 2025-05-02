from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
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
            return ans - 1 
        else:
            return ans


if __name__ == '__main__':
    solution = Solution()
    
    nums = [1,1,0,1]
    # print(solution.longestSubarray(nums)) # 3
    assert solution.longestSubarray(nums) == 3
    # After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

    nums = [0,1,1,1,0,1,1,0,1]
    # print(solution.longestSubarray(nums)) # 5
    assert solution.longestSubarray(nums) == 5
    # Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray 
    # with value of 1's is [1,1,1,1,1].

    nums = [1,1,1]
    # print(solution.longestSubarray(nums)) # 2
    assert solution.longestSubarray(nums) == 2
    # Explanation: You must delete one element.

    nums = [1,1,0,0,1,1,1,0,1]
    # print(solution.longestSubarray(nums)) # 4
    assert solution.longestSubarray(nums) == 4

    nums = [0,0,0]
    # print(solution.longestSubarray(nums)) # 0
    assert solution.longestSubarray(nums) == 0

    nums = [1,1,1]
    # print(solution.longestSubarray(nums)) # 2
    assert solution.longestSubarray(nums) == 2

    nums = [0,0,1,1]
    # print(solution.longestSubarray(nums)) # 2
    assert solution.longestSubarray(nums) == 2

    nums = [1,0,0,1,1,1]
    # print(solution.longestSubarray(nums)) # 3
    assert solution.longestSubarray(nums) == 3

    nums = [1,0,1,1,1,1,1,1,0,1,1,1,1,1]
    # print(solution.longestSubarray(nums)) # 11
    assert solution.longestSubarray(nums) == 11




# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         subarray_start = 0
#         subarray_end = 0
#         zero_count = 0
        
#         max_1s_len = 0
#         max_1s_preceding_zero = 0
#         max_1s_zero_count = 0
#         for i in range(len(nums)):
#             if nums[i] == 0 or i == len(nums) - 1:
#                 current_len = subarray_end - subarray_start
#                 if zero_count <= 1:
#                     if current_len == 0:
#                         subarray_start = i + 1
#                         subarray_end = i + 1
#                         continue
#                     zero_count += 1 * (not nums[i])
#                     subarray_end = i + 1
#                     if zero_count == 2:
#                         if current_len > max_1s_len:
#                             max_1s_len = current_len
#                             max_1s_zero_count = 1
#                             max_1s_preceding_zero = 1 - nums[subarray_start - 1]
#                         subarray_start = i + 1
#                         subarray_end = i + 1
#                         zero_count = 0
#                 else:
#                     if current_len > max_1s_len:
#                         max_1s_len = current_len
#                         max_1s_zero_count = 1
#                         max_1s_preceding_zero = 1 - nums[subarray_start - 1]
#                     subarray_start = i + 1
#                     subarray_end = i + 1
#                     zero_count = 0
#             else:
#                 subarray_end = i + 1
        
#         if subarray_end - subarray_start > max_1s_len:
#             max_1s_len = subarray_end - subarray_start
#             max_1s_zero_count = zero_count
#             max_1s_preceding_zero = 1 - nums[subarray_start - 1]
        
#         if max_1s_len == 0:
#             return 0
#         elif max_1s_len > 0 and max_1s_zero_count == 0 and max_1s_preceding_zero == 1:
#             return max_1s_len
#         elif max_1s_len > 0:
#             if max_1s_zero_count <= 1:
#                 return max_1s_len - 1
