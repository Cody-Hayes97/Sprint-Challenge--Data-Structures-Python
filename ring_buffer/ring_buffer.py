class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.order = 0

    def append(self, item):
        if self.order >= self.capacity:
            self.order = 0
        self.storage[self.order] = item
        self.order += 1

    def get(self):
        # for var in self.storage:
        #     print(var)
        return self.storage


rb = RingBuffer(3)
rb.append(2)
rb.append(3)


print(rb.get())
