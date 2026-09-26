class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dum=[]
        for i in nums:
            if i in dum:
                return True
            else:
                dum.append(i)
        return False