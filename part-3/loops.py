### Flip the Pairs ###

num = int(input("num"))
num_list = []

for x in range(1, num+1, 2):
    if x+1 <= num:
        print(x + 1)
        print(x)
    else:
        print(x)

###################################################
