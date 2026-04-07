class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        rev=[]
        nums=sorted(nums)
        for i in nums:
            if i not in rev:
                rev.append(i)
        
        count=1
        longest=1
        for j in range(len(rev)-1):
            if rev[j]==rev[j+1]-1:
                count=count+1
            else:
                longest=max(count,longest)
                count=1
        return max(longest,count) 