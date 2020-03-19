# 1. sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# 2. diff_21
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

# 3. front_back
def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]
  return str[len(str)-1] + mid + str[0]

# 4. front3
def front3(str):
  if len(str) >= 3:
    return str[:3] + str[:3] + str[:3]
  else:
    return str[:len(str)] + str[:len(str)] + str[:len(str)]

# 5. makes10
def makes10(a, b):
  if a == 10 or b == 10 or a + b == 10:
    return True
  else:
    return False

# 6. missing_char
def missing_char(str, n):
  a = str[:n]
  b = str[n+1:]
  return a + b

# 7. monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return ((a_smile and b_smile) or (not a_smile and not b_smile))

# 8. near_hundred
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# 9. not_string
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

# 10. parrot_trouble
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

# 11. pos_neg
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

# 12. sum_double
def sum_double(a, b):
  if (a != b):
    return a + b
  else:
    return (a + b) * 2


