
def calculate
  calculate_array = []
  puts "To exit program enter 'done'."

  while true
    puts  "Enter the formula to calculate."
    string = gets.chomp.downcase

    if string == 'done'     
      break
    end 

    string = string.split(" ")  

    firstint = string[0].to_f
    operator = string[1].to_sym
    secondint = string[2].to_f

    case operator
    when :+ then result = firstint + secondint
    when :- then result = firstint - secondint
    when :/ then result = firstint / secondint
    when :* then result = firstint * secondint
    else
      puts "invalid input, try again"
    end
    p result
  
  calculate_array << [firstint, operator, secondint, result]

  end
  
    puts "There were #{calculate_array.length} calculations performed:"
    calculate_array.each { |int1, op, int2, calc| puts "#{int1} #{op} #{int2} = #{calc}" }
end

calculate