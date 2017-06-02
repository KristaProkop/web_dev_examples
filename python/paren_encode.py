# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples:
# "din" => "((("
# "recede" => "()()()"
# "Success" => ")())())"
# "(( @" => "))(("

def duplicate_encode(word):
    return "".join( ')' if word.lower().count(l) > 1 else '(' for l in word.lower() )
    

# def duplicate_encode(word):
#   count = {}
#   #set letter to True if duplicate exists
#   for letter in word.lower():
#     if letter in count:
#       count[letter] = True
#     else:
#       count[letter] = False
      
      
#   # compare each letter to count dict and replace with appropriate char
#   encoded_word = ''
#   for letter in word.lower():
#     if count[letter] == True:
#       encoded_word += ')'
#     else: 
#       encoded_word += '('
#   return encoded_word
 
    
print duplicate_encode('recede')
