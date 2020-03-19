# 1. common_end
def common_end(a, b):
  if a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]:
    return True
  else:
    return False

# 2. first_last6
def first_last6(nums):
   if nums[0] == 6 or nums[len(nums) - 1] == 6:
     return True
   else:
    return False

# 3. has23
def has23(nums):
  for i in range(len(nums)):
    if nums[i] == 2 or nums[i] == 3:
      return True
  return False


# 4. make_ends
def make_ends(nums):
  return [nums[0], nums[len(nums) - 1]]


# 5. make_pi
def make_pi():
  return [3, 1, 4]


# 6. max_end3
def max_end3(nums):
  temp = nums[0]
  if nums[0] < nums[len(nums) - 1]:
    temp = nums[len(nums) - 1]
  return [temp, temp, temp]

# 7. middle_way
def middle_way(a, b):
  return [a[1], b[1]]

# 8. reverse3
def reverse3(nums):
  nums = nums[::-1]
  return nums

# 9. rotate_left3
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

# 10. same_first_last
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums) - 1]:
    return True
  else:
    return False

# 11. sum2
def sum2(nums):
  sum = 0
  end = min(len(nums), 2)
  for i in range(end):
    sum += nums[i]
  return sum

# 12. sum3
def sum3(nums):
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
  return sum


