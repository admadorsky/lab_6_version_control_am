# ANTHONY MADORSKY'S encoder algorithm

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