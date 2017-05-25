# Given two numbers in an array, if the numbers have the same number of digits, return the first one in the array.

def find_longest(arr):
    return sorted(arr, key=lambda x: len(str(x)), reverse=True)[0]