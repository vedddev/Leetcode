class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        dup=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                dup.add(i)
        if len(dup)>=1:
            return True
        return False
        