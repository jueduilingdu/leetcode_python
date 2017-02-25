class Solution(object):
    def isMatch(self, s, p):
        """
        :递归算法
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0:
            return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i=-1;
            length=len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]):
                    return True
                i+=1
            return False
          
 class Solution:
    # @return a boolean
    # DP算法：http://blog.csdn.net/fzzying3/article/details/42057935；http://blog.csdn.net/u014265088/article/details/52574639
    def isMatch(self, s, p):
        s, p = ' ' + s, ' ' + p
        dp = [[False] * (len(p)) for i in range(len(s))]
        dp[0][0] = True
        ind = 2
        while ind < len(p) and p[ind] == '*':
            dp[0][ind], ind = True, ind + 2
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if (s[i] == p[j] or p[j] == '.') and dp[i-1][j-1]:
                    dp[i][j] = True
                if p[j] == '*' and (dp[i][j-2] or ((p[j-1] == '.' or p[j-1] == s[i]) and (dp[i-1][j-2] or dp[i-1][j]))):
                    dp[i][j] = True
        return dp[len(s) - 1][len(p) - 1]
