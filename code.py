def calculate_lucky_number(name):
    lucky_number = 0
    
    for char in name:
        if char.isalpha():
            char_value = ord(char.lower()) - ord('a') + 1
            lucky_number += char_value
    
    while lucky_number > 9:
        num_sum = 0
        while lucky_number:
            num_sum += lucky_number % 10
            lucky_number //= 10
        lucky_number = num_sum
    
    return lucky_number

# Prompt the user to enter their name
name = input("Enter your name: ")

# Calculate the lucky number
lucky_number = calculate_lucky_number(name)

# Display the lucky number
print("Your lucky number is:", lucky_number)
