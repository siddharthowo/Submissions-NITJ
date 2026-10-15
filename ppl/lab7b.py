data = set()

while True:
    print("\nSet Menu")
    print("1. Create / Overwrite Set")
    print("2. Display Set")
    print("3. Check Element Existence")
    print("4. Add Elements")
    print("5. Remove an Element")
    print("6. Clear / Delete Set")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")

    if choice == "1":
        items = input("Enter elements separated by spaces: ").split()
        data = set(items)
        print("Set created:", data)

    elif choice == "2":
        if data is None:
            print("Set does not exist.")
        else:
            print("Current Set:", data)

    elif choice == "3":
        if not data:
            print("Set is empty or does not exist.")
            continue
        val = input("Enter element to check: ")
        if val in data:
            print(f"'{val}' is present in the set.")
        else:
            print(f"'{val}' is not in the set.")

    elif choice == "4":
        if data is None:
            data = set()
        items = input("Enter elements to add (separated by spaces): ").split()
        data.update(items)
        print("Updated Set:", data)

    elif choice == "5":
        if not data:
            print("Set is empty or does not exist.")
            continue
        val = input("Enter element to remove: ")
        if val in data:
            data.remove(val)
            print("Updated Set:", data)
        else:
            print("Element not found.")

    elif choice == "6":
        data = None
        print("Set deleted.")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")