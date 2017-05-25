
# Method to create a list
# input: string of items separated by spaces (example: 'carrots apples cereal pizza')
# steps: 
  # [fill in any steps here]
  # set default quantity
  # print the list to the console [can you use one of your other methods here?]
# output: [what data type goes here, array or hash?]

# Method to add an item to a list
# input: item name and optional quantity
# steps: pass in item name and quantity. quantity defaults to 1. Add to array.
# output:return array

# Method to remove an item from the list
# input: item name and optional quantity
# steps: quantity defaults to 1. pass in item name and quantity, find item in array, delete
# output: puts item removed. return array.

# Method to update the quantity of an item
# input: item name 
# steps: find item in array, p current quantity. ask for new quantity, replace quantity
# output:

# Method to print a list and make it look pretty
# input: call method
# steps: use each to iterate through array and print
# output: print array 

#---------------------------------------------------------------
def create_list(items_array)
  list = {}
  items_array.map { |item| list[item] = 1  }
  return list
end

def add_item(list, item, quantity = 1)
  list[item] = quantity
  return list
end

def change_quantity(list, item, quantity)
  list[item] = quantity
  return list
end

def delete_item(list,item)
  list.delete(item)
  return list
end

def print(list)
  puts 'SHOPPING LIST'
  puts '--------------------------'
  list.each { |item, quantity| puts "#{quantity}  #{item}" } 
    puts '--------------------------'
end
#---------------------------------------------------------------

# Create a new list
list = create_list([])
list = create_list(['Almond Milk', 'Eggs', 'Bread']) 
#I  could not figure out how to get my program to work with 2-word items like 'Almond Milk' if I used a string here!

# Add the following items to your list
# Lemonade, qty: 2, Tomatoes, qty: 3, Onions, qty: 1, Ice Cream, qty: 4
add_item(list, 'Lemonade', 2)
add_item(list,'Tomatoes', 3)
add_item(list, 'Onion', 1)
add_item(list,'Ice Cream', 4)

#Remove the Lemonade from your list
delete_item(list,'Lemonade')

#Update the Ice Cream quantity to 1
change_quantity(list,'Ice Cream', 1)
change_quantity(list,'Almond Milk', 2)

#Print out your list (Is this readable and nice looking)?
print(list)