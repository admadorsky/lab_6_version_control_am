# Alexander Bergendal's decoding program
def decode(string):
    # decoded string is initially empty
    decoded_string = ''
    for i in string:
        # converts each character to an integer. subtracts 3. then adds the string of the character to decoded_string .
        if int(i) in range(3, 10):
            decoded_string += str(int(i) - 3)
        # adds 7 instead of subtracting 3. for characters between 0 and 3.
        else:
            decoded_string += str(int(i) + 7)
    return decoded_string