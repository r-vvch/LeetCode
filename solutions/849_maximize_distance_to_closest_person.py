from typing import List


class Solution:
    def maxDistToClosest(self, seats):
        left_zeros = -1
        right_zeros = -1
        max_zeros = -1
        zeros = 0
        for seat in seats:
            if seat == 0:
                zeros += 1
            else:
                if left_zeros == -1:
                    left_zeros = zeros
                else:
                    max_zeros = max(max_zeros, zeros)
                zeros = 0
        right_zeros = zeros
        return max(left_zeros, right_zeros, (max_zeros + 1) // 2)

    def maxDistToClosestLong(self, seats: List[int]) -> int:
        i = 0

        # max length of continuous zeros on the left
        left_zeros = 0
        while i < len(seats) and seats[i] == 0:
            left_zeros += 1
            i += 1
        max_zeros = left_zeros
        i += 1

        # max length of continuous zeros in the middle
        while i < len(seats):
            if seats[i] == 0:
                i_zero_start = i
                i = i_zero_start + 1
                while i < len(seats) and seats[i] == 0:
                    i += 1
                max_zeros = max(max_zeros, i - i_zero_start)
            else:
                i += 1

        # max length of continuous zeros on the right
        right_zeros = 0
        if seats[-1] == 0:
            right_zeros = i - i_zero_start

        if max_zeros in [left_zeros, right_zeros]:
            return max_zeros
        else:
            middle_zeros = (max_zeros + 1) // 2
            return max(left_zeros, right_zeros, middle_zeros)


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
