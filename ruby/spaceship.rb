class Spaceship

attr_reader :max_speed, :location  #I made location readable for driver code testing
attr_accessor :name

def initialize(name, max_speed)
	puts 'Initializing Spaceship instance...'
	@name = name
	@max_speed = max_speed
	@shield = true
	@inventory = {}
	@location = nil
	@num_array = []
end

#TRACTOR BEAM
#This method works when I run it on its own outside of a class, but 
#in the class it is only summing the first letter of the string. 
#I didn't notice until the very end and did not have time to debug
#^^^^DISREGARD, I figured it out I think!

#disable shield
#convert item to array
#iterate through array characters to 
#add integer values to num_array
#when done, sum the values in the array and assign to word_sum
#if word_sum is less than 500, then
#add the item to inventory
#enable shield (will return true automatically)
#else return false

def tractor_beam(item)
	disable_shield
	
	array = item.split('')
	array.map do |char|
		@num_array << char.ord
	end
	word_sum = @num_array.inject{ |sum,x| sum + x }

	if word_sum < 500
		key = item	
		@inventory[key] = word_sum
		p "#{item.capitalize} has been added to inventory"

		enable_shield
	else
		return false
	end
end

def cargo_weight
	sum = 0
	@inventory.each do |key, value| 
		sum = sum += value
	end
	p "The total cargo weight is #{sum}."
end

def disable_shield
	puts "Shield has been disabled"
	@shield = false
end

def enable_shield
	puts "Shield has been enabled"
	@shield = true
end

def warp_to(location)
	puts "Traveling at #{@max_speed} to #{location}."
	@location = location
end


def pickup(item, location)
	warp_to(location)
	tractor_beam(item)
end

def print_inventory
	puts "-----------------"
	puts "INVENTORY LIST"
	puts "-----------------"
	@inventory.each do |item, weight|
  	puts "#{item.capitalize}, #{weight} lbs"  	
	end
	puts "-----------------"
end

end

#driver code
new_ship = Spaceship.new("Enterprise", "200,000")
p new_ship.name
new_ship.name=("bob")
p new_ship.name
p new_ship.max_speed
p new_ship.enable_shield
new_ship.warp_to("Chicago")
new_ship.tractor_beam("cow")
new_ship.tractor_beam("a")
new_ship.pickup("beads", "Vegas")
p new_ship.location
new_ship.print_inventory
new_ship.cargo_weight