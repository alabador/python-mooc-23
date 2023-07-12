##########################################

### Right aligned ###

# Please write a program which asks 
# the user for a string and then prints it out 
# so that exactly 20 characters are displayed. 
# If the input is shorter than 20 characters, 
# the beginning of the line is filled in with * characters.

string = input("Please type in a string: ")
string_len = len(string)
max_length = 20
final_string = ""
# get string, and its length, take up that amount of space from the 20 '#'
i = 0
while i < max_length - string_len:
    final_string += "*"
    i += 1
final_string += string
print(final_string)

##########################################