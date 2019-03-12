class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.kth = k
        self.arr = nums
        self.len = len(nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.arr.append(val)
        return sorted(self.arr)[-3]


obj = KthLargest(3,[4,5,8,2])
obj.add(3)
obj.add(5)
obj.add(10)
print(obj.add(9))