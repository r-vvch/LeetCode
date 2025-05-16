from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time_max = max(i[1] for i in intervals)
        times = [0] * (time_max + 1)
        for begin, end in intervals:
            times[begin] += 1
            times[end] -= 1
        
        max_rooms = 0
        rooms_num = 0
        for time in times:
            rooms_num += time
            max_rooms = max(max_rooms, rooms_num)

        return max_rooms

    def minMeetingRoomsNaive(self, intervals: List[List[int]]) -> int:
        time_max = max(i[1] for i in intervals)

        max_rooms = 0
        for i in range(time_max):
            rooms_num = 0
            for j in intervals:
                if j[0] <= i <= j[1]:
                    rooms_num += 1
            max_rooms = max(max_rooms, rooms_num)

        return max_rooms


if __name__ == '__main__':
    solution = Solution()

    intervals = [[0,30],[5,10],[15,20]]
    print(solution.minMeetingRooms(intervals)) # 2

    intervals = [[7,10],[2,4]]
    print(solution.minMeetingRooms(intervals)) # 1
