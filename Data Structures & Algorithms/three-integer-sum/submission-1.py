class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[l]+nums[r]+nums[i]
                rev=[]
                if s==0:
                    rev.append(nums[i])
                    rev.append(nums[l])
                    rev.append(nums[r])
                    l += 1
                    r -= 1
                    if rev not in res:
                        res.append(rev)
                elif s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    return 0
        return res