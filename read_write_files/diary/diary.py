# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    selection = input('Function: ')

    if selection == "1":
        new_entry = input('Diary entry: ')
        with open('diary.txt', 'a') as diary:
            diary.write(f"{new_entry}\n")
        print('Diary saved')

    elif selection == "2":
        with open('diary.txt') as diary:
            for entry in diary:
                entry = entry.replace("\n", "")
                print(entry)

    elif selection == "0":
        break
print("Bye now!")