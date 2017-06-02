# implement an difference function, which subtracts one list from another
# It should remove all values from list a, which are present in list b.

# array_diff([1,2],[1]) == [2]
# array_diff([1,2,2,2,3],[2]) == [1,3]
# array_diff([-10, -8, 0, -17, -16, 17, -10, 8, -16, 9, 14, 6, 13, 3, -8, 13, 3, -20, 7, 17],[17, 15, 1, 15, 19, 14, -14, -6, 10, -3]) == [-10, -8, 0, -17, -16, -10, 8, -16, 9, 6, 13, 3, -8, 13, 3, -20, 7]

def array_diff(a, b):
  return [i for i in a if i not in b]