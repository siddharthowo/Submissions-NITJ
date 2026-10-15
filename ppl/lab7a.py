data = ()

while True:
    print("\nTuple Menu")
    print("1. Create / Overwrite Tuple")
    print("2. Display Tuple")
    print("3. Access Element by Index")
    print("4. Update an Element")
    print("5. Delete an Element")
    print("6. Delete Entire Tuple")
    print("7. Exit")
    
    choice = input("Enter choice (1-7): ")

    if choice == "1":
        items = input("Enter elements separated by spaces: ").split()
        data = tuple(items)
        print("Tuple created:", data)

    elif choice == "2":
        if data is None:
            print("Tuple does not exist.")
        else:
            print("Current Tuple:", data)

    elif choice == "3":
        if not data:
            print("Tuple is empty or does not exist.")
            continue
        try:
            index = int(input(f"Enter index (0 to {len(data) - 1}): "))
            print(f"Element at index {index}:", data[index])
        except (ValueError, IndexError):
            print("Invalid index.")

    elif choice == "4":
        if not data:
            print("Tuple is empty or does not exist.")
            continue
        try:
            index = int(input(f"Enter index to replace (0 to {len(data) - 1}): "))
            new_val = input("Enter new value: ")
            
            temp = list(data)
            temp[index] = new_val
            data = tuple(temp)
            print("Updated Tuple:", data)
        except (ValueError, IndexError):
            print("Invalid index.")

    elif choice == "5":
        if not data:
            print("Tuple is empty or does not exist.")
            continue
        val = input("Enter element to remove: ")
        if val in data:
            temp = list(data)
            temp.remove(val)
            data = tuple(temp)
            print("Updated Tuple:", data)
        else:
            print("Element not found.")

    elif choice == "6":
        data = None
        print("Tuple deleted.")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")