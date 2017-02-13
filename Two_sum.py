Class Solutin(object):
  def twoSum(self, nums, target):
    dict={}
    for i in range(len(nums)):
      if dict.get(target-nums[i],None)==None:
        dict[nums[i]]=i
      else:
        return (dict[target-nums[i]],i)
