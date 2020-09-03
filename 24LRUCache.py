class LRUCache:
    mem = dict()
    memCount = dict()
    capacity = 0
    currentCount = 0

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.memCount:
            self.memCount[key] = self.memCount[key] + 1
        else:
            return -1

        return self.mem.get(key)

    def put(self, key: int, value: int) -> None:
        # if within capacity then add right away
        currentCount = +1

        if currentCount > self.capacity:
            # print('list  before deletion')
            # print(self.memCount)
            # print(self.mem)
            # rm the entry with least memCOunt
            minValue = min(self.memCount.items(), key=lambda x: x[1])
            leastUsedKeys = [i[0] for i in self.memCount.items() if i[1] == minValue[1]]
            leastUsedKey = leastUsedKeys[-1]
            # print('leastUsedKeys', leastUsedKeys)
            # print('leastUsedKey', leastUsedKey)
            del self.memCount[leastUsedKey]
            del self.mem[leastUsedKey]

        self.mem[key] = value
        self.memCount[key] = 0
        return


obj = LRUCache(2)

obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
print(obj.mem)
