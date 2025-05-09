from bisect import bisect_left


class HitCounter:
    def __init__(self):
        self.timestamps = []

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        hits_300s = 0
        for ts in self.timestamps:
            if ts > timestamp - 300:
                hits_300s += 1
        return hits_300s

    def getHitsFast(self, timestamp: int) -> int:
        return len(self.ts) - bisect_left(self.ts, timestamp - 300 + 1)


if __name__ == '__main__':
    hitCounter = HitCounter()

    hitCounter.hit(1)       # hit at timestamp 1.
    hitCounter.hit(2)       # hit at timestamp 2.
    hitCounter.hit(3)       # hit at timestamp 3.
    print(hitCounter.getHits(4))   # get hits at timestamp 4, return 3.
    # 3
    hitCounter.hit(300)     # hit at timestamp 300.
    print(hitCounter.getHits(300)) # get hits at timestamp 300, return 4.
    # 4
    print(hitCounter.getHits(301)) # get hits at timestamp 301, return 3.
    # 3
