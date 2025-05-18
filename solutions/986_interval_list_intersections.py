from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]],
                             secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            fl_start, fl_end = firstList[i]
            sl_start, sl_end = secondList[j]
            if fl_start <= sl_end and sl_start <= fl_end:
                result.append([max(fl_start, sl_start), min(fl_end, sl_end)])
            if fl_end <= sl_end:
                i += 1
            else:
                j += 1
        return result


if __name__ == '__main__':
    solution = Solution()

    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    print(solution.intervalIntersection(firstList, secondList))
    # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

    firstList = [[1,3],[5,9]]
    secondList = []
    print(solution.intervalIntersection(firstList, secondList))
    # []
