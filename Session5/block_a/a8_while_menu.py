# A8* — While menu
# 1 = add name, 2 = show list, 0 = quit

names = []

while True:
    print("press 1 to add the name.")
    print("press 2 to show the list.")
    print("press 0 to quit the program.")
    choice = input("Enter the choice: ")
    if choice == "0":
        break
    elif choice == "1":
        names.append(input("Enter your name: "))
    elif choice == "2":
        if not names:
            print("The list is empty")
        else:
            for i, name in enumerate(names, start = 1):
                print(f"{i}. {name}")
    else:
        print("Unknown Choice")