class Solution(object):
    def getSneakyNumbers(self, nums):
        seen=set()
        duplicates=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                duplicates.add(i)
        return list(duplicates)