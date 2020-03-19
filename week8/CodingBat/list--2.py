# 1. big_diff
def big_diff(nums):
  return max(nums) - min(nums)

# 2. centered_average
def centered_average(nums):
  nums.remove(min(nums))
  nums.remove(max(nums))
  return sum(nums) // len(nums)

# 3. count_events
def count_evens(nums):
  cnt = 0
  for i in range(len(nums)):
    if (nums[i] % 2 == 0):
      cnt += 1
  return cnt

# 4. has22
def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False


# 5. sum13
def sum13(nums):
  cnt = 0
  i = 0
  while i < len(nums):
    if nums[i] == 13:
      i += 1
    else:
      cnt += nums[i]
    i += 1
  return cnt


# 6. sum67
def sum67(nums):
  cnt = 0
  ok = False
  for i in range(len(nums)):
    if nums[i] == 6:
      ok = True
      continue
    if nums[i] == 7 and ok == True:
      ok = False
      continue
    if ok == False:
      cnt += nums[i]
  return cnt

