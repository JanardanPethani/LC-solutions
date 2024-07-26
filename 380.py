import random


class RandomizedSet:
    def __init__(self):
        self.randomSet = set()
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        self.randomSet.add(val)
        self.len += 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            self.randomSet.remove(val)
            self.len -= 1
            return True
        return False

    def getRandom(self) -> int:
        return random.sample(self.randomSet, 1)[0]


obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.insert(2)
param_3 = obj.remove(2)
param_4 = obj.getRandom()

print(
    param_1,
    param_2,
    param_3,
    param_4,
)
