class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        m=0
        while l<r:
            dist=r-l
            local=min(heights[l],heights[r])*dist
            m=max(local,m)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return m