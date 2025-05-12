class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
    ["MyQueue", "push", "push", "peek", "pop", "empty"]
