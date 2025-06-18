#!/usr/bin/python3
# The range function generates a sequence of numbers from 97 to 123 (inclusive)
# These numbers correspond to the ASCII values of lowercase letters a to z
for i in range(97, 123):
    # The chr function converts an ASCII value to its corresponding character
    # The format function is used to insert the character into the string
    print("{}".format(chr(i)), end="")
