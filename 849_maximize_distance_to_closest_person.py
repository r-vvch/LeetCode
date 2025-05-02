from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0

        # max length of continuous zeros on the left
        left_zeros_len = 0
        while i < len(seats) and seats[i] == 0:
            left_zeros_len += 1
            i += 1
        max_zeros_len = left_zeros_len
        i += 1

        # max length of continuous zeros in the middle
        while i < len(seats):
            if seats[i] == 0:
                i_zero_start = i
                i = i_zero_start + 1
                while i < len(seats) and seats[i] == 0:
                    i += 1
                if i - i_zero_start > max_zeros_len:
                    max_zeros_len = i - i_zero_start
            else:
                i += 1
        
        # max length of continuous zeros on the right
        right_zeros_len = 0
        if seats[-1] == 0:
            right_zeros_len = i - i_zero_start
        
        if max_zeros_len in [left_zeros_len, right_zeros_len]:
            return max_zeros_len
        else:
            middle_zeros = 0
            if max_zeros_len % 2 == 0:
                middle_zeros = max_zeros_len // 2
            else:
                middle_zeros = max_zeros_len // 2 + 1
            return max(left_zeros_len, right_zeros_len, middle_zeros)


if __name__ == '__main__':
    solution = Solution()

    seats = [1,0,0,0,1,0,1]
    print(solution.maxDistToClosest(seats)) # 2

    seats = [1,0,0,0]
    print(solution.maxDistToClosest(seats)) # 3

    seats = [0,1]
    print(solution.maxDistToClosest(seats)) # 1

    seats = [1,0,0,1]
    print(solution.maxDistToClosest(seats)) # 1

    seats = [1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0]
    print(solution.maxDistToClosest(seats)) # 5
