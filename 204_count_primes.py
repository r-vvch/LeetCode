class Solution:
    prime_nums = [2, 3, 5, 7]

    def checkPrime(self, num: int) -> int:
        if num in [0, 1]:
            return False

        for i in self.prime_nums:
            if num == i:
                return True
            if num % i == 0:
                return False

        for i in range(self.prime_nums[-1] + 2, num // 2, 2):
            if num % i == 0:
                return False

        self.prime_nums.append(num)
        return True

    def countPrimesSimple(self, n: int) -> int:
        prime_count = 0
        for i in range(n):
            if self.checkPrime(i):
                prime_count += 1
        return prime_count


    def countPrimesSieve(self, n: int) -> int:
        if n < 2:
            return 0

        candidates = [True] * n
        candidates[0] = candidates[1] = False

        i = 2
        while i * i < n:
            if candidates[i]:
                for j in range(i * i, n, i):
                    candidates[j] = False
            i += 1

        return sum(candidates)


    def countPrimesSieveSlow(self, n: int) -> int:
        candidates = []
        for i in range(2, n):
            candidates.append(i)

        p = 2
        checked_p_num = 0
        while len(candidates) > 0 and p < n:
            mul = 2
            p_x_mul = p * mul
            while p_x_mul <= n:
                if p_x_mul in candidates:
                    candidates.remove(p_x_mul)
                mul += 1
                p_x_mul = p * mul
            checked_p_num += 1
            if checked_p_num < len(candidates):
                p = candidates[checked_p_num]
            else:
                break

        return len(candidates)


    def countPrimes(self, n: int) -> int:
        pass

    countPrimes = countPrimesSieve


if __name__ == '__main__':
    solution = Solution()

    n = 10
    print(solution.countPrimes(n)) # 4

    n = 0
    print(solution.countPrimes(n)) # 0

    n = 1
    print(solution.countPrimes(n)) # 1

    n = 4999
    print(solution.countPrimes(n))

    n = 499979
    print(solution.countPrimes(n))
