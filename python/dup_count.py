# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.

# Example

# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabbcdeB" -> 2 # 'a' and 'b'
# "indivisibility" -> 1 # 'i'
# "Indivisibilities" -> 2 # 'i' and 's'
# "aa11" -> 2 # 'a' and '1'

def duplicate_count(text):
  text = text.lower()
  dictionary = dict.fromkeys(text, 0)
  for char in text: 
    dictionary[char] += 1
  return len([val for key, val in dictionary.iteritems() if val > 1])


def duplicate_count(text):
  text = text.lower()
  return len( [c for c in set(text) if text.count(c)>1] )
     
    