#4-6 Christopher Mendoza & Krista Prokopczyk

def encrypt(string)
  index_counter = 0
  until index_counter == string.length
    if string[index_counter] == " " #if character is a space do not change it
        string == " "
    elsif string[index_counter] == "z" #if character is a z, return a
        string[index_counter] = "a"  
    else
        string[index_counter] = string[index_counter].next
    end 
    index_counter += 1
  end
  return string
end

def decrypt(string)
  alpha = "abcdefghijklmnopqrstuvwxyz"
  index_counter = 0
  until index_counter == string.length
    if string[index_counter] == " " #if character is a space do not change it
      string == " "
    else 
      string[index_counter] = alpha[alpha.index(string[index_counter]) - 1 ]
    end
    index_counter += 1
  end
  return string
end

#UI
#ask user which operation they'd like to run
puts "Type 1 to encrypt a password, or 2 to decrypt."
selection = gets.to_i

case 
when selection == 1 #if user picks encrypt, case #1 executes. 
    puts "Enter the password you'd like to encrypt:"
    encrypt_pass = gets.chomp
    encrypt(encrypt_pass)
    puts "The encrypted password is #{encrypt_pass}."
when selection == 2  #if user picks decrypt, case #2 executes.
    puts "Enter the encrypted password you'd like to decrypt:"
    decrypt_pass = gets.chomp
    decrypt(decrypt_pass)
    puts "The decrypted password is #{decrypt_pass}."
else  #if user doesn't pick 1 or 2, an error message is thrown.
    puts "I don't understand."
end

#ORIGINAL CODE BEFORE REVISIONS :
#def encrypt(string)
#  string = string
#  encrypt_string = ""
#  index_counter = 0
#  until index_counter == string.length
#    encrypt_string[index_counter] = string[index_counter].next
#   index_counter += 1
#  end
#  return encrypt_string
#end

#def decrypt(string)
#   alpha = "abcdefghijklmnopqrstuvwxyz"
#   string = string
#   decrypt_string = ""
#   index_counter = 0
#   until index_counter == string.length
#     decrypt_string[index_counter] = alpha[alpha.index(string[index_counter]) - 1 ]
#     index_counter += 1
#   end
#   return decrypt_string
# end

#DRIVER CODE
#encrypt("abc") should return "bcd"
#p encrypt("abc")
#encrypt("zed") should return "afe"
#p encrypt("zed")
#decrypt("bcd") should return "abc"
#p decrypt("bcd")
#decrypt("afe") should return "zed"
#p decrypt("afe")
#nested call should work because it works from the "inside out" of the parenthases.
#p decrypt(encrypt("swordfish"))

# USER INTERFACE BEFORE REVISIONS
# puts "Would you like to encrypt(1) or decrypt(2)"
# selection = gets.to_i
# puts "Please enter the password"
# password = gets.chomp

# if selection == 1
#   encrypted_pass = encrypt(password)
#   puts "The encrypted password is #{encrypted_pass}"
#   elsif selection == 2
#     decrypted_pass = decrypt(password)
#     puts "The decrypted password is #{decrypted_pass}"
#   else
#     puts "I don't understand"
# # end