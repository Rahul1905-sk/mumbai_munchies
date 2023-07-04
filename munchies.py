

menu=[]


def Add_snack():
    name = input("Enter snack name: ")
    Id = int(input("Enter snack id: "))
    price = int(input("Enter Price: "))

    obj = {
        "Name": name,
        "ID":Id,
        "Price": price
    }


    for i in menu: 
        if(i["ID"] == Id):
            print("Id is already exist!!")
            return 

    menu.append(obj)
    print("Item added successfully")




def Remove_snack():
    Id = input("Enter snack id: ")

    for i in menu:
        if i["ID"] == Id:
            menu.remove(i)
            print("Item removed Successfully!!")
            return 
    
    print("Item not found!! ")
    return


    

def Update_snack():
    Id = input("Enter snack id: ")
    New_price = int(input("Enter snack new price: "))
    for i in menu:
        if i["ID"] == Id:
            i["Price"] = New_price
            print("Item Updated Successfully!!")
            return
            # break;
    
    print("Item not found!! ")
    return



def Record_sale():
    print(menu)


while True :
    print("welcome to mumbai munchies!!")
    print("Please Choose one of the following options: ")
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Snack Availability")
    print("4. Record Sales")
    print("5. Exit")
    print()
    print()


    choice = int(input("Enter your input: "))

    if choice == 1:
        Add_snack()
    
    elif choice == 2:
        Remove_snack()
    
    elif choice == 3:
        Update_snack()

    elif choice == 4:
        Record_sale()

    elif choice == 5:
        print("You have quit successfully !!")
        break
    else:
        print("Invalid input try again")
        continue
 