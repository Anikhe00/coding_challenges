# Vowel Case
# Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

# Vowels are "a", "e", "i", "o", and "u" in any case.
# Non-alphabetical characters should remain unchanged.

def vowel_case(s):
    s = s.lower()
    result = ""
    for word in s:
      for char in word:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
          result += char.upper()
        else:
          result += char
    return result