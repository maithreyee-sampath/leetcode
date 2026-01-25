class Solution:
    # def f(self,i,j,text1,text2,dp):

    #         if i<0 or j<0:
    #             return 0

    #         if dp[i][j] != -1:
    #             return dp[i][j]

    #         elif text1[i] == text2[j]:
    #             dp[i][j]= 1+self.f(i-1,j-1,text1,text2,dp)
    #             return dp[i][j]
            
    #         else:
    #             dp[i][j]= max(self.f(i-1,j,text1,text2,dp),self.f(i,j-1,text1,text2,dp))
    #             return dp[i][j]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        index1 = len(text1)
        index2 = len(text2)

        dp = [[-1]*(index2+1) for i in range(index1+1)]

        def f(i,j,text1,text2,dp):

            if dp[i][j] != -1:
                return dp[i][j]
            if i==0 or j==0:
                return 0

            elif text1[i-1] == text2[j-1]:
                dp[i][j]= 1 +f (i-1,j-1,text1,text2,dp)
                return dp[i][j]
            
            else:
                dp[i][j]= max(f(i-1,j,text1,text2,dp),f(i,j-1,text1,text2,dp))
                return dp[i][j]
        
        
        
        return f(index1,index2,text1,text2,dp)
    
