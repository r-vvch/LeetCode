from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_wrk = sorted(intervals)
        output_intervals = []
        curr_interval = intervals_wrk[0]
        i = 1
        while i < len(intervals_wrk):
            if intervals_wrk[i][0] <= curr_interval[1]:
                curr_interval[1] = max(curr_interval[1], intervals_wrk[i][1])
            else:
                output_intervals.append(curr_interval)
                curr_interval = intervals_wrk[i]
            i += 1
        output_intervals.append(curr_interval)
        return output_intervals


if __name__ == '__main__':
    solution = Solution()
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(intervals)) # [[1,6],[8,10],[15,18]]

    intervals = [[1,4],[4,5]]
    print(solution.merge(intervals)) # [[1,5]]

    intervals = [[1,4],[0,4]]
    print(solution.merge(intervals)) # [[0,4]]

    intervals = [[1,4],[2,3]]
    print(solution.merge(intervals)) # [[1,4]]
