class RecentCounter:

    def __init__(self):
        self.requests = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.start] < t - 3000:
            self.start += 1
        return len(self.requests) - self.start


class RecentCounterMy:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)

        num_calls = 0
        i = 0
        while i < len(self.requests):
            if self.requests[i] >= t - 3000:
                num_calls += 1
            else:
                self.requests.pop(i)
                i -= 1
            i += 1

        return num_calls


if __name__ == '__main__':
    recent_counter = RecentCounter()

    print(recent_counter.ping(1))     # requests = [1], range is [-2999,1], return 1
    print(recent_counter.ping(100))   # requests = [1, 100], range is [-2900,100], return 2
    print(recent_counter.ping(3001))  # requests = [1, 100, 3001], range is [1,3001], return 3
    print(recent_counter.ping(3002))  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3
