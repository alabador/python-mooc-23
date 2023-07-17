# Creating a Spruce Tree 

# Description: Create a tree with equal spacing on each side, given an argument for its height.

def spruce(height):
    # deal with height of tree
    # deal with spaces
    # find max width, subtract from there
    print("a spruce!")
    
    for i in range(height):
        create_space(height, i, True)
        print("*" * (i+1), end="")
        print("*" * i, end="")
        create_space(height, i, False)
    
    # Stump of spruce tree
    create_space(height, 0, True)
    print("*", end="")
    create_space(height, 0, False)

    
def create_space(height, index, concat):
    if concat == True:
        print(" " * (height - 1 - index), end="")
    else:
        print(" " * (height - 1 - index))

#######################################################

