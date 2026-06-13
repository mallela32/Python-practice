def is_isogram(string):
    char_map = {}
    for char in string:
      if char == '-' or char == ' ':
          continue
      if char.lower() in char_map:
          return False
      else:
          char_map[char.lower()] = char
    return True
