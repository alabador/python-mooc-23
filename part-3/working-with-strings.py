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


### A Framed Word ###

# A side note: This exercise tripped me up SO MUCH for some reason. 
# This solution is not elegant, can be fixed to be cleaner but it works.
# I can't directly access the index of a string in python?! Strings are immutable?!
# AGHH anyway here's my solution after like an hour geez..


# Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

# Sample output
# Word: testing

# ******************************
# *          testing           *
# ******************************


import math
# take in a word
word = input("Word: ")
#get length of word


#get length of space by subtracting it from 30, then div by 2
space1_len = (30 - len(word)) / 2
space2_len = 0

# checks for even numbers. If odd, will floor the number, then get +1 for second space.
# This is essentially checking for the first half of spaces with lower amount, then other
# half with +1 amount of spaces
if space1_len % 2 == 0:
    space1_len = int(space1_len)
    space2_len = space1_len
elif space1_len % 2 != 0:
    space1_len = int(math.floor(space1_len))
    space2_len = space1_len + 1


# create empty strings
display_string = ""
space1_string = ""
space2_string = ""

display_string += "*"
for x in range(space1_len - 1):
    display_string += " "
display_string += word
for x in range(space2_len - 1):
    display_string += " "
display_string += "*"

# if length of space is odd, convert to int by making it floor
print("*"*30)
print(display_string)
print("*"*30)


################################################################

### Find all Substrings ###

#print out all substrings which are at least three characters long, 
# which begin with the char specified by the user. You can assume the
# input string is at least three chars long.

# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot

word = input("word")
char = input("char")

while True:
    index = word.find(char)
    if len(word) - index > 2 and index >= 0:
        print(word[index:index+3])
        word = word[index+1:]
    else:
        break


####################################################################

### The second occurrence ###

# Find the second occurence of a substring. If there is no second (or first) occurrence,
# the program should print out a message accordingly.

word = input("word")
substring = input("sub")

index = word.find(substring)
second_index = word.find(substring, index + len(substring))

if second_index < 0: 
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {second_index}.")


######################################################################