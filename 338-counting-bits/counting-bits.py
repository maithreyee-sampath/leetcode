class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def binCount(num):
            count = 0
            x = str(format(num,'b'))
            for i in range(len(x)):
                if x[i] == '1':
                    count+=1
            return count
        
        ans = [0]*(n+1)
        
        for i in range(1,len(ans)):
            ans[i] = binCount(i)

        return ans