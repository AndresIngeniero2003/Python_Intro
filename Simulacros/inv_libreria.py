#Simulation exam: Library inventory management

#Variables globales
list_Inventory = [
    {"title": "el hombre mas rico de babilonia", "price": 20000.0, "quantity": 10},
    {"title": "el monje que vendio su ferrari", "price": 15000.0, "quantity": 9},       
    {"title": "padre rico padre pobre", "price": 30000.0, "quantity": 12},
    {"title": "piense y hagase rico", "price": 25000.0, "quantity": 15},
    {"title": "sangre de campeon", "price": 10000.0, "quantity": 3}
]               #list of dictionaries with keys(title, price, quantity)

#Functions
def menu():    
    bool_Init = True
    while bool_Init:
        str_option = (input("""
                        **********<Main menu>**********
                        
                        1. Add products
                        2. Consul products
                        3. Update products
                        4. Delete products
                        5. Inventory total
                        6. Exit
                        option -->  """))
        if str_option.isdecimal(): 
            int_option = int(str_option)
            if 1 <= int_option <= 6:
                match int_option:
                    case 1:
                        print("\nLet's add a new book!\n")
                        str_name = input("Enter the title of the book:  ").lower().strip()
                        while True:
                            str_price = input("Enter the book price:  ")
                            if str_price.isdecimal():
                                flt_price = float(str_price)
                                if flt_price >= 0:
                                    break 
                                else:
                                    print("The price can not be negative")
                            else:
                                print("You can enter only numbers\n")
                        while True:
                            str_quantity = input("Enter the product quantity:  ")
                            if str_quantity.isdecimal():
                                int_quantity = int(str_quantity)
                                if int_quantity >= 0:
                                    break 
                                else:
                                    print("The quantity cannot be negative\n")
                            else:
                                print("You can enter only numbers\n")                                    
                        add_book(str_name, flt_price, int_quantity)
                    case 2:
                        print("\nLet's consult a book\n")
                        str_name = input("Enter the book name:  ").lower().strip()
                        consult_book(str_name)                           
                    case 3:
                        print("\nLet's update the price of a book\n")
                        str_name = input("Enter the title of the book:  ").lower().strip()
                        while True:
                            str_price = input("Enter the book price:  ")
                            if str_price.isdecimal():
                                flt_price = float(str_price)
                                if flt_price >= 0:
                                    break 
                                else:
                                    print("The price can not be negative")
                            else:
                                print("You can enter only numbers\n")                        
                        update_book(str_name, flt_price)
                    case 4:
                        print("\nLet's delete a book\n")
                        str_name = input("Enter the title of the book:  ").lower().strip()
                        delete_book(str_name)
                    case 5:
                        print("\nLet's calculate the total inventory\n")
                        inventory_total()
                    case 6:
                        print("\nClosing software..........\n")
                        bool_Init = False
            else:
                print("\nYou are outside the range 1-6")
        else: 
            print("\nYou cannot enter letters, remember only numbers\n")
        
def add_book(str_name, flt_price, int_quantity):
    thisBook = False
    for book in list_Inventory:
        if str_name == book["title"]:
            thisBook = True
            break
    if thisBook == False:
        libro={"title":str_name, "price": flt_price, "quantity": int_quantity}
        
        list_Inventory.append(libro)
    else:
        print("book is already in inventory\n")
        
    number = 1
    print(f"\nLibros en el inventario:\n")
    for title in list_Inventory:
        print(f"#{number} {title["title"]}")
        number += 1
    
def consult_book(str_name):
    thisBook = False
    for book in list_Inventory:
        if str_name == book["title"]:
            print(f"\nName: {str_name} \nPrice: {book["price"]} \nQuantity: {book["quantity"]} \n") 
            thisBook = True
            break
    if thisBook == False:
        print("book is not in inventory\n")
    
def update_book(str_name, flt_price):
        thisBook = False
        for book in list_Inventory:
            if str_name == book["title"]:
                
                book["price"] = flt_price
                print("was succefully updated", book)
                thisBook = True
                break
        if thisBook == False:
            print("Does not exist")
            
def delete_book(str_name):
    thisBook = False
    index = -1
    for i,book in enumerate(list_Inventory):
        if str_name == book["title"]:
            index =  i
            thisBook = True
            break
    if thisBook == False:
        print("book is not in inventory\n")
    else:
        del list_Inventory[index]
    
def inventory_total():
    total_inv = 0
    for book in list_Inventory:
        flt_price = book["price"]
        int_quantity = book["quantity"]
        total_inv = total_inv + flt_price*int_quantity
    print(f"The total book inventory is: {total_inv}")


#Program start
print("Starting inventory software..........\n")
print("Software started correctly.\n")
menu()