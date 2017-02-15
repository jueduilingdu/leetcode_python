class Solution:
    # @return an integer
    def reverse(self, x):
        a = 0
        b = x if x > 0 else -x
        while b:
            a, b = a * 10 + b % 10, b / 10 
        return a if x > 0 else -a
      (overflow if int 32 bits)

      
      
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        revx=int(str(abs(x))[::-1])
        if revx>math.pow(2,31):
            return 0
        else:
            return revx*cmp(x,0)
