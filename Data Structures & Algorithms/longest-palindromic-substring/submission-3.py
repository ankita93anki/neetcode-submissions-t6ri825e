class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[False]*n for _ in range(n)]

        #Initialize start position and max_length
        start, max_length = 0,1

        #Base case: one character length
        for i in range(n):
            dp[i][i] = True
        
        #Base case: two character length
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
            if dp[i][i+1]:
                start, max_length = i,2

        #DP Case
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start, max_length = i, length
        return s[start:start+max_length]

        

        