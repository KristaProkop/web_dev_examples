# Given a positive integer n, return first n digits of Thue-Morse sequence, as a string:

# thue_morse(1);  "0"
# thue_morse(2);  "01"
# thue_morse(5);  "01101"
# thue_morse(10): "0110100110"
# n will always be a positive integer between 1 and 10000.

def thue_morse(n):
    result = '0'
    while True:
        result = result + result.replace('0', 'X').replace('1', '0').replace('X', '1')
        if len(result) > n:
            break
    return result[0:n]