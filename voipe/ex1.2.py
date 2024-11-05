""" 
In the second exercise the idea is to create a small grocery shopping list with the list datastructure. In short, create a program that allows the user to (1) add products to the list, (2) remove items and (3) print the list and quit.

If the user adds something to the list, the program asks "What will be added?: " and saves it as the last item in the list. If the user decides to remove something, the program informs the user about how many items there are on the list (There are [number] items in the list.") and prompts the user for the removed item ("Which item is deleted?: "). If the user selects 0, the first item is removed. When the user quits, the final list is printed for the user "The following items remain in the list:" followed by the remaining items one per line. If the user selects anything outside the options, including when deleting items, the program responds "Incorrect selection.". When the program works correctly it prints out the following:

Example output:
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 1
What will be added?: Milk
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 1
What will be added?: Beer
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 2
There are 2 items in the list.
Which item is deleted?: 1
Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: 3
The following items remain in the list:
Milk

"""


def grocery_list():
    items = []

    while True:
        # Prompt user for an action
        print("would you like to")
        print("(1) Add or")
        print("(2) Remove items or")
        print("(3) Quit?: ", end="")

        try:
            choice = int(input())
        except ValueError:
            print("Incorrect selection")
            continue

        if choice == 1:
            item = input("What will be added?: ")
            items.append(item)

        elif choice == 2:
            if items:
                print(f"There are {len(items)} items in the list.")
                try:
                    index = int(input("Which item is deleted?: "))
                    if 0 <= index < len(items):
                        items.pop(index)
                    else:
                        print("Incorrect selection.")
                except ValueError:
                    print("Incorrect selection.")
            else:
                print("The list is empty.")
        elif choice == 3:
            print("The following items remain in the list:")
            for item in items:
                print(item)
            break
        else:
            print("Incorrect selection.")


grocery_list()
