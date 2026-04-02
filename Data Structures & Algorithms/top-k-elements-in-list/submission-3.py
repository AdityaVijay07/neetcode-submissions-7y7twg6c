class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_map={}

        for i in nums:
            if i not in k_map:
                k_map[i]=1
            else:
                k_map[i]+=1
            
        res=sorted(k_map,key=k_map.get,reverse=True)
        return res[:k]