# * queryMapIndex
def getMapKeyIndex(self, nums):
    print(len(nums))
    print(range(len(nums)))
    for i in range(len(nums)):
        if nums[i] == self:
            return i
    i = 0
    for x in nums:
        if self > x:
            i += 1
    return i


print(getMapKeyIndex(5, [1, 23, 45, 6]))
