# 1. close_far
def close_far(a, b, c):
  return (close(a, b) and far(a, b, c)) or (close(a, c) and far(a, c, b))


def close(a, b):
  if abs(a - b) <= 1:
    return True
  return False


def far(a, b, c):
  if abs(a - c) >= 2 and abs(b - c) >= 2:
    return True
  return False


# 2. lone_sum
def lone_sum(a, b, c):
  sum = 0
  if a not in [b, c]:
    sum += a
  if b not in [a, c]:
    sum += b
  if c not in [a, b]:
    sum += c
  return sum


# 3. lucky_sum
def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  else:
    return a + b + c

# 4. make_bricks
def make_bricks(small, big, goal):
  temp = 0
  if goal >= 5 * big:
    temp = goal - (5 * big)
  else:
    temp = goal % 5
  return small >= temp


# 5. make_chocolate
def make_chocolate(small, big, goal):
  temp = 0
  if goal >= 5 * big:
    temp = goal - 5 * big
  else:
    temp = goal % 5
  if temp <= small:
    return temp
  else:
    return -1

# 6. no_teen_sum
def no_teen_sum(a, b, c):
  return check(a) + check(b) + check(c)

def check(a):
  if a not in [13, 14, 17, 18, 19]:
    return a
  else:
    return 0

# 7. round_sum
def round_sum(a, b, c):
  return check(a) + check(b) + check(c)


def check(a):
  if a % 10 < 5:
    return a - (a % 10)
  else:
    return a + (10 - a % 10)

