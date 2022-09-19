from __future__ import annotations



class FancyQueue:

    def __init__(self, max_size=10, initial_set=None):
        self.max_size = max_size
        self.container = []

        if initial_set is not None:
            self.addAll(initial_set)

    def __str__(self) -> str:
        return str([str(i) for i in self.container])

    def __sizeof__(self) -> int:
        return self.size()

    def __add__(self, other) -> FancyQueue:
        if isinstance(other, FancyQueue):
            return FancyQueue(max_size=self.max_size+other.max_size, initial_set=self.getAll()+other.getAll())

        return self

    def __mul__(self, k) -> FancyQueue:
        if isinstance(k, int):
            self.container = list(map(lambda x: k*x, self.container))
            return self

        return self

    def enqueue(self, element):
        self.container.append(element)

        if(len(self.container) > self.max_size):
            self.container = self.container[1:]

    def dequeue(self):
        if len(self.container) == 0:
            return None

        first = self.container[0]
        self.container = self.container[1:]

        return first

    def peek(self):
        if len(self.container) == 0:
            return Null

        return self.container[0]

    def clear(self):
        self.container = []

    def addAll(self, collection):
        for i in collection:
            self.enqueue(i)

    def rotate(self, k) -> FancyQueue:
        if len(self.container) <= 1:
            return

        k = k % len(self.container)
        self.container = self.container[k:] + self.container[:k]
        return self

    def reverse(self) -> FancyQueue:
        self.container = self.container[::-1]
        return self

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return len(self.container) == 0

    def isFull(self):
        return len(self.container) == self.max_size

    def getAll(self):
        return self.container

    def getOrderedPairs(self):
        return list(zip(list(range(self.size())), self.container))
