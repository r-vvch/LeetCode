from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        result = []
        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result


if __name__ == '__main__':
    solution = Solution()

    s = "ababcbacadefegdehijhklij"
    print(solution.partitionLabels(s)) # [9,7,8]

    s = "eccbbbbdec"
    print(solution.partitionLabels(s)) # [10]
