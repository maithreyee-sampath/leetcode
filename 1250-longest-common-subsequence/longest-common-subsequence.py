class Solution:
    def f(self,i,j,text1,text2,dp):

            if i<0 or j<0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            elif text1[i] == text2[j]:
                dp[i][j]= 1+self.f(i-1,j-1,text1,text2,dp)
                return dp[i][j]
            
            else:
                dp[i][j]= max(self.f(i-1,j,text1,text2,dp),self.f(i,j-1,text1,text2,dp))
                return dp[i][j]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        index1 = len(text1)
        index2 = len(text2)

        dp = [[-1]*index2 for i in range(index1)]
        return self.f(index1-1,index2-1,text1,text2,dp)
    
