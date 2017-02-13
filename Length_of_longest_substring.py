class Solution(boject):
  def lengthofLongestSubstring(self, s):
    """
    :type s:str
    :rtype: int
    """
    dict, ans, p1, p2= {}, 0, 0, 0
    while p2<len(s):
      p = dict.get(s[p2],None)
      if p==None:
        dict[s[p2]]=p2
        p2+=1
        ans=max(ans,p2-p1)
       else:
        while p1<=p:
          dict.pop(s[p1])
          p1+=1
        p1=p+1
    return ans
    
