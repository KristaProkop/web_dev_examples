# Given an array of integers, find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.
# For example:
# given the array {1,2,3,4,3,2,1} return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
# given the array {1,100,50,-51,1,1} return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

arr = [1,2,3,4,5,6]
#arr = [1,2,3,4,3,2,1]

def find_even_index(arr):
  for i, x in enumerate(arr):
    left_sum, right_sum = sum(arr[0:i]), sum(arr[i+1:])
    if left_sum == right_sum:
      return i
  return -1


# def find_even_index(arr):
#   return [ (i, x)  for i, x in enumerate(arr) if (sum(arr[0:i]) == sum(arr[i+1:])) ] 

  
print find_even_index(arr)