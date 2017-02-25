class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        MAX_INT=2147483647
        MIN_INT=-2147483648
        if x>MAX_INT or x<0:
            return False
        else:
            y=str(x)
            reverse=[]
            reverse=list(str(x)[::-1])
            if y[0]=='-':
                reverse.remove('-')
                p=-int(''.join(reverse[:]))
                if p==x:
                    return True
                else:
                    return False
            else: 
                p=int(''.join(reverse[:]))
                if p==x:
                    return True
                else:
                    return False
                  
                  
class Solution:
  def isPalindrome(self, x):
    if x<=0:
      return False if x<=0 else True
    a, b=x, 0
    while a:
      b, a=b*10+a%10, a/10
    return b == x
