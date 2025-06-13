def two_sum(nums,target):
   seen{}
  for i, num in enumerate(nums):
      complement = target - num
   print(f"index:{i},number:{num}")
    compement={complement},seen:{seen}")
   if complement in seen:
     return [seen[complement],i]
      seen[num]=1
   return[]