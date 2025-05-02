from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        
        output = []
        range_start = nums[0]
        range_end = nums[0]
        for i in nums[1:]:
            if i == range_end + 1:
                range_end = i
            else:
                if range_start == range_end:
                    output.append(str(range_start))
                else:
                    output.append(f'{range_start}->{range_end}')
                range_start = i
                range_end = i
        
        # working with the last element
        if range_start == range_end:
            output.append(str(range_start))
        else:
            output.append(f'{range_start}->{range_end}')
        
        return output


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    # ["0->2","4->5","7"]

    # nums = [0, 2, 3, 4, 6, 8, 9]
    # ["0","2->4","6","8->9"]

    solution = Solution()

    print(solution.summaryRanges(nums))
