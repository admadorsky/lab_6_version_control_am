# ANTHONY MADORSKY'S encoder algorithm

from decoder import decode

def encode(password):
    encoded_list = []                                           # initialize an empty list to store shifted values
    for letter in password:
        if (int(letter) < 7):
            encoded_list.append(str(int(letter) + 3))           # store shifted value
        else:
            encoded_list.append(str((int(letter) + 3) - 10))
    encoded_string = "".join(encoded_list)                      # convert list back into a string for output
    return encoded_string

# test_password = "47583645"                                    # testing encode()
# print(encode(test_password))


menu = """
Menu  
------------- 
1. Encode  
2. Decode  
3. Quit 
"""
while True:

    print(menu)
    user_choice = int(input("Please enter an option: "))

    if user_choice == 1:
        input_password = str(input("Please enter your password to encode: "))
        encoded_password = encode(input_password)
        print("Your password has been encoded and stored!")

    elif user_choice == 2:
        print("The encoded password is " + encoded_password + ", and the original password is " + decode(encoded_password))

    elif user_choice == 3:
        quit()