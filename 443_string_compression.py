from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        output_len = 0
        i = 0

        while i < len(chars):
            j = i
            count = 0
            while j < len(chars) and chars[j] == chars[i]:
                count += 1
                j += 1

            output_len += 1
            if count != 1:
                for k in str(count):
                    chars[output_len] = k
                    output_len += 1
        
            if output_len < j:
                for l in range(output_len, j):
                    chars.pop(output_len)
                
            i = output_len

        return output_len


if __name__ == '__main__':
    solution = Solution()

    chars = ["a","a","b","b","c","c","c"]
    print(solution.compress(chars), chars)
    # Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    # Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

    chars = ["a"]
    print(solution.compress(chars), chars)
    # Output: Return 1, and the first character of the input array should be: ["a"]
    # Explanation: The only group is "a", which remains uncompressed since it's a single character.
    
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(solution.compress(chars), chars)
    # Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    # Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 