class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=['$', '#']
        for i in range(len(s)):
            arr.append(s[i])
            arr.append('#')
        p=[0]*len(arr)
        mx, pos, ansp=0, 0, 0
        for i in range(1,len(arr)):
            p[i]=min(mx-i, p[2*pos-i])  if mx>i else 1
            while p[i]+i<len(arr) and arr[i+p[i]]==arr[i-p[i]]:
                p[i]+=1
            if p[i]+i>mx:
                mx, pos=p[i]+i, i
            if p[i]>p[ansp]:
                ansp=i
        st=(ansp-p[ansp]+1) // 2
        return s[st:st+p[ansp]-1]
