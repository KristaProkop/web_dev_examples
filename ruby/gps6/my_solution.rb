# Virus Predictor
# I worked on this challenge [by myself, with: Krista Prokopczyk, Chris Mendoza ].
# We spent [2] hours on this challenge.
# EXPLANATION OF require_relative
# When you run my_solution.rb, look at this file called #"state data" which is located relative to the current file.

# Require_relative 'state_data' runs the data through ruby
#interpreter first
#

require_relative 'STATE_DATA'

class VirusPredictor

#initialize the instance (creates a new object)
#require 3 arguments
#variables are accessible in the class

  def initialize(state_of_origin, population_density, population)
    @state = state_of_origin
    @population = population
    @population_density = population_density
  end

#virus effects calls predicted_deaths and speed_of_spread
#resulting in printed statements from predicted_deaths and speed_of_spread
#Release 8: removed the print statements from the other methods to  predicted_deaths and speed_of spread to make those methods only responsible for calculations and virus effects only responsible for printing.
  def virus_effects
    print "#{@state} will lose #{predicted_deaths} people in this outbreak and will spread across the state in #{speed_of_spread} months.\n\n"
  end

  private
#predicted_deaths takes 3 arguments from State_data file
#calculates the number of deaths based on population and density (and rounds to nearest integer)
#and then prints

  def predicted_deaths
  # predicted deaths is solely based on population density
    if @population_density >= 200
      number_of_deaths = (@population * 0.4).floor
    elsif @population_density >= 150
      number_of_deaths = (@population * 0.3).floor
    elsif @population_density >= 100
      number_of_deaths = (@population * 0.2).floor
    elsif @population_density >= 50
      number_of_deaths = (@population * 0.1).floor
    else
      number_of_deaths = (@population * 0.05).floor
    end
  end


#speed_of_spread takes 2 arguments from state_data file
#calculates the speed of the virus spreading based on population density
#and then puts
  def speed_of_spread #in months
  # We are still perfecting our formula here. The speed is also affected
  # by additional factors we haven't added into this functionality.

    if @population_density >= 200
      months = 0.5
    elsif @population_density >= 150
      months = 1
    elsif @population_density >= 100
      months = 1.5
    elsif @population_density >= 50
      months = 2
    else
      months = 2.5
    end

  end
end
#=======================================================================

# DRIVER CODE
 # initialize VirusPredictor for each state
# Don't forget STATE_DATA needs to be in caps to signify constant

STATE_DATA.each do | state_name, statistics |
  newstate = VirusPredictor.new(state_name, statistics[:population_density],statistics[:population])
  newstate.virus_effects
end

##Reflection Section
# What are the differences between the two different hash syntaxes shown in the state_data file?
# One hash has the key pointing (=>) to a value that is a nested hash. The nested hash contains key-value pairs with the key followed by a colon to point to the value.

# What does require_relative do? How is it different from require?
#require_relative pulls in data from a named file located relative to the my_solution file. I have read quite a bit about "require" and still don't quite understand the difference. Something to do with load paths, libraries and gems!

# What are some ways to iterate through a hash? 
#You can iterate over the keys, values or both at the same time.

# When refactoring virus_effects, what stood out to you about the variables, if anything?
#the variable names were unclear in speed_of_spread and it was difficult to understand what the formulas were doing.

# What concept did you most solidify in this challenge?
#iterating over hashes
