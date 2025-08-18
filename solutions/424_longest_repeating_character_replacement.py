from collections import defaultdict


class SolutionFastest:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_dict = defaultdict(int)
        max_len = 0
        left = 0
        for right in range(len(s)):
            ch_dict[s[right]] += 1
            max_count = max(ch_dict.values())
            curr_len = right - left + 1
            if curr_len - max_count > k:
                ch_dict[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len


class SolutionFaster:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for left in range(len(s)):
            ch_dict = defaultdict(int)
            max_count = 0
            summ = 0
            for right in range(left, len(s)):
                ch_dict[s[right]] += 1
                summ += 1
                max_count = ch_dict[s[right]] if ch_dict[s[right]] > max_count else max_count
                if len(ch_dict) == 1:
                    continue
                elif summ - max_count > k:
                    right -= 1
                    break
            max_len = max(right - left + 1, max_len)
        return max_len


class SolutionSlow:
    def summCountWihoutTheMostCommon(self, ch_dict: dict) -> int:
        max_count = 0
        summ = 0
        for i in ch_dict:
            summ += ch_dict[i]
            if ch_dict[i] > max_count:
                max_count = ch_dict[i]
        summ -= max_count
        return summ

    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for left in range(len(s)):
            ch_dict = defaultdict(int)
            for right in range(left, len(s)):
                ch_dict[s[right]] += 1
                if len(ch_dict) == 1:
                    continue
                elif self.summCountWihoutTheMostCommon(ch_dict) > k:
                    right -= 1
                    break
            max_len = max(right - left + 1, max_len)
        return max_len


Solution = SolutionFastest


if __name__ == '__main__':
    solution = Solution()

    s = "ABAB"
    k = 2
    print(solution.characterReplacement(s, k)) # 4

    s = "AABABBA"
    k = 1
    print(solution.characterReplacement(s, k)) # 4

    s = "ABAA"
    k = 0
    print(solution.characterReplacement(s, k)) # 2

    s = "ABBB"
    k = 2
    print(solution.characterReplacement(s, k)) # 4

    s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
    k = 4
    print(solution.characterReplacement(s, k)) # 7
