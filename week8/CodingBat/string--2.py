# 1. cat_dog
def cat_dog(str):
  return str.count("cat") == str.count("dog")


# 2. count_code
def count_code(str):
  cnt = 0
  for i in range(len(str) - 3):
    if str[i:i + 2] == 'co' and str[i + 3] == 'e':
      cnt += 1
  return cnt


# 3. count_hi
def count_hi(str):
  return str.count("hi")

# 4. double_char
def double_char(str):
  ans = ""
  for i in range(len(str)):
    ans += str[i] + str[i]
  return ans

# 5. end_other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))


# 6. xyz_there
def xyz_there(str):
  str = str.replace('.xyz', '')
  if 'xyz' in str:
    return True
  return False



