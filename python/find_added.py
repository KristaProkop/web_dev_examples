# return a string containing the numbers in string 2 which are not in string 1, in ascending order. 

def findAdded(string1, string2):
    return "".join(sorted(i * (string2.count(i)- string1.count(i)) for i in set(string2)))

