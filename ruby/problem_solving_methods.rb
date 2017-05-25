# Search array for integer
def search_array(array, integer)
	if array.include?(integer)
		array.index(integer)
	end
end

search_array([42, 89, 23, 1], 1)


# Fibonacci sequence 
def fib(length)
  array = [0]
  
  length.times do |i|
    if i==0
      array[i] = 0
    elsif i==1
      array[i] = 1
    else
      array[i] = array[i-1] + array[i-2]
    end  
  end
  
  p array[0..length]
end

fib(6)

#Accuracy check: return "true" if the last value in array of fib(100) equals 218922995834555169026
if fib(100)[99] == 218922995834555169026
	puts "Checks out!"
else
	puts "Something's not right."
end

#create a method to sort using a sorting algorithm

def mergesort(array)
  def merge(left_sorted, right_sorted)
    res = []
    l = 0
    r = 0

    loop do
      break if r >= right_sorted.length and l >= left_sorted.length

      if r >= right_sorted.length or (l < left_sorted.length and left_sorted[l] < right_sorted[r])
        res << left_sorted[l]
        l += 1
      else
        res << right_sorted[r]
        r += 1
      end
    end

    return res
  end

  def mergesort_iter(array_sliced)
    return array_sliced if array_sliced.length <= 1

    mid = array_sliced.length/2 - 1
    left_sorted = mergesort_iter(array_sliced[0..mid])
    right_sorted = mergesort_iter(array_sliced[mid+1..-1])
    return merge(left_sorted, right_sorted)
  end

  mergesort_iter(array)
end

mergesort([3, 4, 1, 100, 2])