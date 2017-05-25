# # Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc
# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.



s = "bqukpkalqifcdsqosdzltmf"
substring = ''
iterator = 0
mylist = ['']


for index in range(iterator, len(s)):
    for count in range(iterator, len(s)-1):
        if s[count] <= s[count+1]:
            substring = substring + s[iterator]
            iterator+=1            
        elif s[count] > s[count+1]:
            substring = substring + s[iterator]
            if len(substring) > len(mylist[0]):
                mylist = [substring]
            iterator = count+1
            substring = ''
            break
print("Longest substring in alphabetical order is: "+ mylist[0])