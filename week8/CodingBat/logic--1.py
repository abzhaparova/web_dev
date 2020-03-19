# 1. alarm_clock
def alarm_clock(day, vacation):
  if not vacation and day != 0 and day != 6:
    return '7:00'
  elif (not vacation and (day == 6 or day == 0)) or (vacation and day != 0 and day != 6):
    return '10:00'
  else:
    return 'off'

# 2. caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed = speed - 5
  if (speed <= 60):
    return 0
  elif speed >= 61 and speed <= 80:
    return 1
  else:
    return 2

# 3. cigar_party
def cigar_party(cigars, is_weekend):
  return (is_weekend and cigars >= 40) or (cigars >= 40 and cigars <= 60)

# 4. date_fashion
def date_fashion(you, date):
  if (you >= 8 and date > 2) or (date >= 8 and you > 2):
    return 2
  elif you <= 2 or date <= 2:
    return 0
  else:
    return 1

# 5. in1to10
def in1to10(n, outside_mode):
  if n >= 1 and n <= 10 and not outside_mode:
    return True
  elif outside_mode and (n <= 1 or n >= 10):
    return True
  else:
    return False

# 6. love6
def love6(a, b):
  if a == 6 or b == 6:
    return True
  elif a + b == 6 or abs(a - b) == 6:
    return True
  else:
    return False

# 7. near_ten
def near_ten(num):
  return num % 10 <= 2 or num % 10 >= 8

# 8. sorta_sum
def sorta_sum(a, b):
  if a + b >= 10 and a + b < 20:
    return 20
  else:
    return a + b

# 9. squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer and temp >= 60 and temp <= 100:
    return True
  elif not is_summer and temp >= 60 and temp <= 90:
    return True
  else:
    return False

