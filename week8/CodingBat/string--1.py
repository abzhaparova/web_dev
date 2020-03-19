# 1. combo_string
def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a

# 2. extra_end
def extra_end(str):
  temp = str[-2:]
  return temp + temp + temp

# 3. first_half
def first_half(str):
  return str[:len(str) // 2]


# 4. first_two
def first_two(str):
  if len(str) <= 2:
    return str
  return str[:2]

# 5. hello_name
def hello_name(name):
  return "Hello " + name + "!"

# 6. left2
def left2(str):
  if (len(str) <= 2):
    return str
  a = str[:2]
  b = str[2:]
  return b + a


# 7. make_abba
def make_abba(a, b):
  return a + b + b + a


# 8. make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

# 9. make_tags
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

# 10. non-start
def non_start(a, b):
  return a[1:] + b[1:]

# 11. without_end
def without_end(str):
  return str[1:len(str) - 1]
