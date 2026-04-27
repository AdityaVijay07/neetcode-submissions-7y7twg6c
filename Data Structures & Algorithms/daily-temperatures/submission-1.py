class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result=[]
        for i in range(n):
            count=0
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    count=j-i
                    break
            result.append(count)
        return result