employeesentered = 0   #set starting var for entries loop

puts "How many employees do you have to enter today?"
entries = gets.chomp.to_i

until employeesentered == entries  #employeesentered var increases by 1 until it matches the number of entries per user input
	puts "What is your name?"
	name = gets.chomp.downcase
	
	puts "how old are you?"
	age = gets.chomp.to_i

	puts "What year were you born?"
	year = gets.chomp.to_i

	puts "Our company cafeteria serves garlic bread. Should we order some for you? y/n"
	likesgarlic = gets.chomp.downcase

	puts "Would you like to enroll in the company’s health insurance? y/n"
	wantsinsurance = gets.chomp.downcase

	allergies = ""  #sets allergies var to avoid skipping this question after one entry answers "done"
	until allergies == "done"
		puts "Type in your allergies one by one. Type 'done' when finished."
		allergies = gets.chomp.downcase
		if allergies == "sunshine"
			break #exits allergies question and moves on to condition test
		end
	end

ageyearmatch = Time.new.year - age == year #calculates age accuracy and sets boolean for test
decision = nil

if ageyearmatch && (likesgarlic == "y" || wantsinsurance == "y")
    decision = "Probably not a vampire"
end

if allergies == "sunshine" || !ageyearmatch && (likesgarlic == "n" || wantsinsurance == "n")
	decision = "Probably a vampire"
end

if !ageyearmatch && likesgarlic == "n" && wantsinsurance == "n"
	decision = "Almost certainly a vampire"
end

if name == "drake cula" || name == "tu fang"
	decision = "Definitely a vampire"
end

if decision.nil?
	decision = "Results inconclusive"
end
	
puts decision
employeesentered = employeesentered + 1
end
puts "Actually, never mind! What do these questions have to do with anything? Let's all be friends." 


