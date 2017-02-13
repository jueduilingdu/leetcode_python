class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    totlen=len(A)+len(B)
    if (1 & totlen):
      return self.findK(A, B, (totlen+1)/2)
    else:
      return (self.findK(A, B, totlen/2)+self.findK(A, B, totlen/2+1))/2.0
    
  def findK(self, A, B, K):
    la, lb, pa, pb=len(A), len(B), min(K/2,len(A)), K-min(K/2, len(A))
    if (la>lb):
      return self.findK(B,A,K)
    if (la==0):
      return B[K-1]
    if (K==1):
      return min(A[0],B[0])
    if A[pa-1]<B[pb-1]:
      return self.findK(A[pa:],B,K-pa)
    elif A[pa-1]>B[pb-1]:
      return self.findK(A,B[pb:],K-pb)
    else:
      return A[pa-1]
