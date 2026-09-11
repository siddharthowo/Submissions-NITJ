#Write a Python program to create, access, update and delete lists. Write a program to develop a real life list
basket=[]
while(True):
    print("Welcome to Grocery Store\n1.Add items to basket\n2.Remove items from basket\n3.Update item\n4.Print basket\n5.Exit")
    ch=int(input("Enter your choice:"))
    if (ch==1):
        item=input("Enter item to add to basket:")
        basket.append(item)
    elif (ch==2):
        item=input("Enter item to add to remove from basket:")
        basket.remove(item)
    elif (ch==3):
        item=input("Enter item to update in basket:")
        for idx,i in enumerate(basket):
            if i==item:
                item_up=input("Update item to?:")
                basket[idx]=item_up
    elif(ch==4):
        print("Basket content:")   
        for i in basket:
            print(i)
    elif(ch==5):
        break
    else:
        print("Please enter a valid option")

