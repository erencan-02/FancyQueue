
class FancyQueue:

    def __init__(self, max_size=10, initial_set=None):
        self.max_size = max_size
        self.container = []

        if initial_set is not None:
            self.addAll(initial_set)

    def __str__(self):
        return str([str(i) for i in self.container])

    def __sizeof__(self):
        return self.size()

    def __add__(self, other):
        if isinstance(other, FancyQueue):
            return ErenQueue(max_size=self.max_size+other.max_size, initial_set=self.getAll()+other.getAll())

        return self

    def __mul__(self, k):
        return list(map(lambda x: k*x, self.container))

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

    def rotate(self, k):
        if len(self.container) <= 1:
            return

        k = k % len(self.container)
        self.container = self.container[k:] + self.container[:k]

    def reverse(self):
        self.container = self.container[::-1]
        return self.container

    def size(self):
        return len(self.container)

    def isEmpty(self):
        return len(self.container) == 0

    def isFull(self):
        return len(self.container) == self.max_size

    def getAll(self):
        return self.container



