class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
         c x t
        c 1
        r   
        a
        b
        t    1


        recurrance relation: dp[i][j] = 
        '''
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]