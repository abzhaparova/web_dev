# 1. array_count9
def array_count9(nums):
  cnt = 0
  for num in nums:
    if num == 9:
      cnt = cnt + 1
  return cnt

# 2. array_front9
def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  for i in range(end):
    if nums[i] == 9:
      return True
  return False


# 3. array123
def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
      return True
  return False


# 4. front_times
def front_times(str, n):
  a = 3
  if a > len(str):
    a = len(str)
  front = str[:a]
  ans = ""
  for i in range(n):
    ans += front
  return ans


# 5. last2
def last2(str):
  if len(str) < 2:
    return 0
  last = str[len(str) - 2:]
  cnt = 0
  for i in range(len(str) - 2):
    if str[i:i + 2] == last:
      cnt += 1
  return cnt


# 6. string_bits
def string_bits(str):
  ans = ""
  for i in range(len(str)):
    if i % 2 == 0:
      ans += str[i]
  return ans


# 7. string_match
def string_match(a, b):
  cnt = 0
  temp = len(a)
  if (len(b) < temp):
    temp = len(b)
  for i in range(temp - 1):
    if a[i:i + 2] == b[i:i + 2]:
      cnt += 1
  return cnt

# 8. string_splosim
def string_splosion(str):
  ans = ""
  for i in range(len(str)):
    ans = ans + str[:i + 1]
  return ans


# 9. string_times
def string_times(str, n):
  ans = ""
  for i in range(n):
    ans += str
  return ans
