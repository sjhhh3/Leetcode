import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myset = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.myset:
            return False
        else:
            self.myset.add(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.myset:
            return False
        else:
            self.myset.remove(val)
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(list(self.myset))

obj = RandomizedSet()
param_1 = obj.insert(2)
param_2 = obj.insert(3)

param_3 = obj.getRandom()

print(param_1)
print(obj.myset)
print(param_3)

