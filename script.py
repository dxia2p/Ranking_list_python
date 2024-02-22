def MainMenu(): # a function to print the main menu, also gets the user's input
    print("*** MAIN MENU ***")
    print("* 1: Print List")
    print("* 2: Add Item To End")
    print("* 3: Remove Last Item")
    print("* 4: Insert At Position")
    print("* 5: Remove At Position")
    print("* 6: Move To Position")
    print("* 7: Edit Item")
    print("* 8: Exit")
    return int(input("* Enter Option #: "))

rankingList = ["Pizza", "Pasta"] # list to hold the rankings

def printList(): # function to print list, this is used for every menu option
    print("RANK LIST")
    for i in rankingList:
        print(i)


inp = MainMenu()
while inp != 8: # keep getting the user's input until the input 8
    match inp:
        case 1:
            if len(rankingList) == 0:
                print("RANK LIST")
                print("No Items in the Rank List")
            else:
                printList()
        case 2:
            print("ADD ITEM TO END")
            item = input("Enter item: ")
            rankingList.append(item) # add the item to the end
            printList()
        case 3:
            print("REMOVE LAST ITEM")
            print(f"{rankingList[-1]} removed from end of list")
            del rankingList[-1] # delete the last item using index -1
            printList()
        case 4:
            print("INSERT ITEM")
            pos = int(input("Insert position: "))
            item = input("Item to insert: ")
            rankingList.insert(pos, item) # using the insert function to insert an item
            printList()
        case 5:
            print("REMOVE AT POSITION")
            pos = int(input("Position to remove: "))
            print(f"{rankingList[pos]} removed from position {pos}")
            del rankingList[pos] # deleting the item at the specified position
            printList()
        case 6:
            print("MOVE TO POSITION")
            fromIndex = int(input("Move Item from: "))
            toIndex = int(input("Move Item to: "))
            rankingList.insert(toIndex, rankingList.pop(fromIndex)) # remove the element that we want, then move it to the correct place
            printList()
        case 7:
            print("EDIT ITEM")
            pos = int(input("Enter position: "))
            replaceWith = input("Replace with: ")
            rankingList[pos] = replaceWith # simply change the value of the array element
            printList()
    inp = MainMenu() # display the main menu again