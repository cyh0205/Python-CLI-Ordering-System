def main():
    print("""
-------------------------------------------
----ONLINE FOOD ORDER MANAGEMENT SYSTEM----
-WELCOME TO SPIDERMAN ONLINE FOOD SERVICES-
-------------------------------------------
    """)
    mainMenu()                                         # call main menu function


def mainMenu():
    print("""
-----------------Main Page-----------------
Choose your option (1-4)
1.View as Guest
2.Login as Customer
3.Login as Admin
4.Exit
    """)
    redirectUser(userInput())                          # get input from user
    mainMenu()                                         # call main menu function


def redirectUser(x):
    if x == "1":
        guest()                                        # call guest function

    elif x == "2":
        login_pg()                                     # call login page function

    elif (x == "3"):
        admin()                                        # call admin function

    elif (x == "4"):
        print("""Exiting program.
Come again next time!""")
        quit()                                    # call main menu function

    else:
        print("Try again!")
    mainMenu()                                         # call main menu function


def guest():
    print("""
---------------Food Category---------------
Special
Rice
Noodle
Ala Carte
Dessert
-------------------------------------------

-----------------CUSTOMER------------------
Please enter one of the options provided.
1.View menu
2.Register as Customer
3.Back to main page
4.Exit

    """)
    redirectGuest(userInput())                        # get input from user


def redirectGuest(x):
    if x == "1":
        viewMenu()                                    # call view menu function
    elif x == "2":
        print("""
--Customer Registration-- 
        """)
        new_username()                                # call new username function
    elif x == "3":
        print("Going back to main page.")
        mainMenu()                                    # call main menu function
    elif x == "4":
        print("""Exiting program.
Come again next time!""")
        quit()                                        # quit the program
    else:
        print("Try again!")
        guest()                                       # call guest function


def viewMenu():
    print("""
-------------------------------------------
-------------------Menu--------------------
-------------------------------------------""")
    menu_special()                                     # call menu special function
    print("")
    menu_rice()                                        # call menu rice function
    print("")
    menu_noodle()                                      # call menu noodle function
    print("")
    menu_ala_carte()                                   # call menu ala carte function
    print("")
    menu_dessert()                                     # call menu dessert function
    print("")
    choices = input("""
Insert '1' to go back to the previous page.
Enter a number: """)
    if choices == "1":
        guest()                                        # call guest function
    else:
        print("Try again!")
        viewMenu()                                     # call view menu function


def menu_special():
    print("""
-------------------------------------------
---------------Special Menu----------------
-------------------------------------------
Item                                      Price""")
    x = open("menuSpecialList.txt", "r")                   # open list and read
    for line in x:                                     # separate data in txt file
        data = line.split(";")
        itemCode = data[0]
        itemInfo = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemInfo)
        price_location = 40 - length_in_digit
        print(itemCode + "-" + itemInfo + " " * price_location + "RM", itemPrice)
    x.close()                                          # close txt file


def menu_rice():
    print("""
-------------------------------------------
----------------Rice Menu------------------
-------------------------------------------
Item                                      Price""")
    x = open("menuRiceList.txt", "r")                   # open list and read
    for line in x:                                  # separate data in txt file
        data = line.split(";")
        itemCode = data[0]
        itemInfo = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemInfo)
        price_location = 40 - length_in_digit
        print(itemCode + "-" + itemInfo + " " * price_location + "RM", itemPrice)
    x.close()                                          # close txt file


def menu_noodle():
    print("""
-------------------------------------------
---------------Noodle Menu-----------------
-------------------------------------------
Item                                      Price""")
    x = open("menuNoodleList.txt", "r")                   # open list and read
    for line in x:                                    # separate data in txt file
        data = line.split(";")
        itemCode = data[0]
        itemInfo = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemInfo)
        price_location = 40 - length_in_digit
        print(itemCode + "-" + itemInfo + " " * price_location + "RM", itemPrice)
    x.close()                                          # close txt file


def menu_ala_carte():
    print("""
-------------------------------------------
--------------Ala Carte Menu---------------
-------------------------------------------
Item                                      Price""")
    x = open("menuAlaCarteList.txt", "r")               # open list and read
    for line in x:                                      # separate data in txt file
        data = line.split(";")
        itemCode = data[0]
        itemInfo = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemInfo)
        price_location = 40 - length_in_digit
        print(itemCode + "-" + itemInfo + " " * price_location + "RM", itemPrice)
    x.close()                                          # close txt file


def menu_dessert():
    print("""
-------------------------------------------
---------------Dessert Menu----------------
-------------------------------------------
Item                                      Price""")
    x = open("menuDessertList.txt", "r")                   # open list and read
    for line in x:                                     # separate data in txt file
        data = line.split(";")
        itemCode = data[0]
        itemInfo = data[1]
        itemPrice = data[2]
        length_in_digit = len(itemCode + itemInfo)
        price_location = 40 - length_in_digit
        print(itemCode + "-" + itemInfo + " " * price_location + "RM", itemPrice)
    x.close()                                          # close txt file


def new_username():
    tempUsernameList = []                                           # create empty list
    customerUsernameList = open("customerUsernameList.txt", "r")        # open list and read
    for line in customerUsernameList.readlines():                   # separate data in txt file
        data = line.split(";")
        username = data[0]
        tempUsernameList.append(username)
    customerUsernameList.close()                                    # close txt file

    customerUsername = input("Enter a username: ")
    if customerUsername in tempUsernameList:                        # to check whether the username is taken or not
        print("This username was taken, please enter another username! ")
        new_username()                                              # call new username function
    else:
        customerUsernameList = open("customerUsernameList.txt", "a")    # add data into customerUsernameList
        x = open("customerUsername&PasswordList.txt", "a")              # add data into customerUsername$PasswordList
        customerUsernameList.write(customerUsername + ";" + "\n")   # add data into customerUsernameList and separate it
        x.write(customerUsername + ";")
        customerUsernameList.close()                                # close txt file
        x.close()                                                   # close txt file
        new_password()                                              # call new password function


def new_password():
    customerPassword = input("Enter a password(at least 4 characters): ")            # get input from user
    if len(customerPassword) >= 4:
        customerPasswordList = open("customerPasswordList.txt", "a")                     # add data into customerPasswordList
        customerUsernameAndPasswordList = open("customerUsername&PasswordList.txt", "a") # add data into customerUsername$PasswordList
        customerPasswordList.write(customerPassword + ";" + "\n")                    # add data into customerPasswordList and separate it
        customerUsernameAndPasswordList.write(customerPassword + ";" + "\n")         # add data into customerUsername$PasswordList and separate it
        customerPasswordList.close()                                                 # close txt file
        customerUsernameAndPasswordList.close()                                      # close txt file
        print("""
Registered successfully!
Directing you to the Login Page.
        """)
    else:
        print("Password is too short, please try again! ")
        new_password()                                                               # call new password function


def login_pg():
    login_choice = input("""
Choose your option (1-3)
1.Sign up as new customer.
2.Login to existing account.
3.Return to previous page.
Enter a number: """)
    if login_choice == "1":
        new_username()                                                               # call new username function
    elif login_choice == "2":
        existUsername = input("Enter your username: ")                               # get input from user
        existPassword = input("Enter your password: ")                               # get input from user

        tempUsernameList = []                                                        # create empty list
        tempPasswordList = []                                                        # create empty list
        x = open("customerUsername&PasswordList.txt", "r")                               # open txt file and read
        for line in x.readlines():                                                   # separate data in txt file
            data = line.split(";")
            username = data[0]
            password = data[1]
            tempUsernameList.append(username)                                        # add data into temp list
            tempPasswordList.append(password)                                        # add data into temp list
        x.close()                                                                    # close txt file

        if existPassword in tempPasswordList:                                        # check if data exist or not
            if (existUsername in tempUsernameList and tempUsernameList.index(existUsername) == tempPasswordList.index(
                    existPassword)):
                print("Login Successfully!")
                print(f"Welcome {existUsername.upper()}!")
                customer_View()                                                      # call customer view function
            else:
                print("Invalid username or password, please try again! ")
                login_pg()                                                           # call login page function
        else:
            print("Invalid username or password, please try again! ")
            login_pg()                                                               # call login page function
    elif login_choice == "3":
        mainMenu()                                                                   # call main menu function
    else:
        print("Please try again! ")
        login_pg()


def customer_View():
    print("""-------------------------------------------


-----------------CUSTOMER------------------
Please choose one of the options provided. (1-5)
1.View food category
2.View all food item
3.Select food item & add to cart
4.Proceed to payment
5.Exit

    """)
    redirectcustomer_view(userInput())                     # get input form user


def redirectcustomer_view(x):
    if x == "1":
        viewFoodCategory()                                 # call viewFoodCategory function

    elif x == "2":
        viewAllFoodItem()                                  # call viewAllFoodItem function

    elif x == "3":
        customerFoodCartMenu()                             # call customerFoodCartMenu function

    elif x == "4":
        proceedToPayment()                                 # call proceedToPayment function

    elif x == "5":
        mainMenu()                                         # call mainMenu function
    else:
        print("Try again!")


def viewFoodCategory():
    print("""
---------------Food Category---------------
Special
Rice
Noodle
Ala Carte
Dessert

Insert "1" to go back to previous page. 
""")
    redirectviewfoodCustomer(userInput())                # get input from user
    customer_View()                                      # call customer view function


def redirectviewfoodCustomer(x):
    if x == "1":
        customer_View()                                  # call customer view function
    else:
        print("Try again! ")
        viewFoodCategory()                               # call view food category function


def viewAllFoodItem():
    print("""
-------------------------------------------
-------------------Menu--------------------
-------------------------------------------""")
    menu_special()                                     # call menu special function
    print("")
    menu_rice()                                        # call menu rice function
    print("")
    menu_noodle()                                      # call menu noodle function
    print("")
    menu_ala_carte()                                   # call menu ala carte function
    print("")
    menu_dessert()                                     # call menu dessert function
    print("")

    Customer = input("""Insert '1' to go back to the previous page.        
Enter a number: """)                                                 # get input form user
    if Customer == "1":
        customer_View()                                # call customer view function

    else:
        print(
            "Try again!")
        viewAllFoodItem()                              # call view all food item function


def customerFoodCartMenu():
    print("""
-------------------------------------------
-----------------Item Cart-----------------
-------------------------------------------

Item                                      Price
""")
    customerFoodCartList = open("customerFoodCartList.txt", "r")            # open list and read
    totalPrice = 0                                                      # set total price to 0
    for item in customerFoodCartList.readlines():                       # separate data in txt file
        data = item.split(";")
        itemCode = data[0]
        itemInfo = data[1]
        itemPrice = float(data[2])
        totalPrice += itemPrice                                        # add up all itemPrice become totalPrice
        lengthInDigit = len(itemCode + itemInfo)                       # arrange data
        price_location = 40 - lengthInDigit
        print(itemCode + "-" + itemInfo + " " * price_location, "{:.2f}".format(itemPrice))
    print("\n", " " * 34, "===============")
    print(" " * 35, "Total: RM", "{:.2f}".format(totalPrice))
    print(" " * 35, "===============")
    itemCartChoice = input("""
Please enter one of the option provided (1-5):
1. Return to Menu
2. Take Order
3. Remove Order
4. Proceed to Payment
5. Return to previous page
Enter a number: """)                                                   # get input from user
    if itemCartChoice == "1":
        viewCustMenu()                                                 # call view cust menu function
    elif itemCartChoice == "2":
        takeOrder()                                                    # call take order function
    elif itemCartChoice == "3":
        remove_item = input("""
Please enter the item code that you want to remove (Eg. A123): """)    # get input form user
        customerFoodCart = open("customerFoodCartList.txt", "r")           # open text file and read
        temp_list = []                                                 # create empty list
        temp_remove_list = []                                          # create empty list
        for item in customerFoodCart.readlines():                      # separate data in txt file
            data = item.split(";")
            itemCode = data[0]
            if itemCode == remove_item:                                # to check if data is similar or not
                if remove_item not in temp_remove_list:
                    temp_remove_list.append(itemCode)
                else:
                    temp_list.append(item)
            if not itemCode == remove_item:                           # remove data
                temp_list.append(item)
        customerFoodCart.close()                                      # close txt file
        customerFoodCart = open("customerFoodCartList.txt", "w")          # open txt file and write
        for item in temp_list:
            customerFoodCart.write(item)
        customerFoodCart.close()                                      # close txt file
        customerFoodCartMenu()                                        # call customerFoodCartList function
    elif itemCartChoice == "4":
        proceedToPayment()                                            # call proceedToPayment function
    elif itemCartChoice =='5':
        customer_View()                                               # call customerView function
    else:
        print("Invalid code, please try again!")
        customerFoodCartMenu()                                       # call customerFoodCartMenu function


def viewCustMenu():
    print("""
    -------------------------------------------
    -------------------Menu--------------------
    -------------------------------------------""")
    menu_special()                                                   # call menu special function
    print("")
    menu_rice()                                                      # call menu rice function
    print("")
    menu_noodle()                                                    # call menu noodle function
    print("")
    menu_ala_carte()                                                 # call menu ala carte function
    print("")
    menu_dessert()                                                   # call menu dessert function
    print("")
    choices = input("""                                              
Insert '1' to go back to the previous page.
Enter a number: """)                                                 # get input form user
    if choices == "1":
        customerFoodCartMenu()                                       # call customerFoodCartMenu function
    else:
        print("Try again!")
        viewMenu()                                                   # call view menu function


def takeOrder():
    menuOnly()                                                       # call menu only function
    while True:
        orderCode = input("""
-------------------------------------------
-------------------Order-------------------
-------------------------------------------
Enter the item code that you want to add to your cart.
(Enter "L" to leave) (Enter "V" to view item cart)
Enter an input: """)                                                # get input from user
        if orderCode[0] == "A":                                     # open txt file if input is A
            menuSpecialList = open("menuSpecialList.txt", "r")
            for item in menuSpecialList.readlines():                # separate data in txt file
                data = item.split(";")
                itemCode = data[0]
                itemInfo = data[1]
                itemPrice = data[2]
                if itemCode == orderCode:
                    print(f"""
Item added to cart: {itemCode}- {itemInfo} """)
                    customerFoodCart = open("customerFoodCartList.txt", "a")
                    customerFoodCart.write(itemCode + "; " + itemInfo + "; " + itemPrice + ";\n")
                    customerFoodCart.close()                       # close txt file
                    break
            else:
                print("Invalid item code, please try again!")

        elif orderCode[0] == "B":                                     # open txt file if input is B
            menuRiceList = open("menuRiceList.txt", "r")
            for item in menuRiceList.readlines():                     # separate data in txt file
                data = item.split(";")
                itemCode = data[0]
                itemInfo = data[1]
                itemPrice = data[2]
                if itemCode == orderCode:
                    print(f"""
Item added to cart: {itemCode}- {itemInfo} """)
                    customerFoodCart = open("customerFoodCartList.txt", "a")
                    customerFoodCart.write(itemCode + "; " + itemInfo + "; " + itemPrice + ";\n")
                    customerFoodCart.close()                       # close txt file
                    break
            else:
                print("Invalid item code, please try again!")

        elif orderCode[0] == "C":                                     # open txt file if input is C
            menuNoodleList = open("menuNoodleList.txt", "r")
            for item in menuNoodleList.readlines():                   # separate data in txt file
                data = item.split(";")
                itemCode = data[0]
                itemInfo = data[1]
                itemPrice = data[2]
                if itemCode == orderCode:
                    print(f"""
Item added to cart: {itemCode}- {itemInfo} """)
                    customerFoodCart = open("customerFoodCartList.txt", "a")
                    customerFoodCart.write(itemCode + "; " + itemInfo + "; " + itemPrice + ";\n")
                    customerFoodCart.close()                       # close txt file
                    break
            else:
                print("Invalid item code! Please try again.")

        elif orderCode[0] == "D":                                     # open txt file if input is D
            menuAlaCarteList = open("menuAlaCarteList.txt", "r")
            for item in menuAlaCarteList.readlines():                 # separate data in txt file
                data = item.split(";")
                itemCode = data[0]
                itemInfo = data[1]
                itemPrice = data[2]
                if itemCode == orderCode:
                    print(f"""
Item added to cart: {itemCode}- {itemInfo} """)
                    customerFoodCart = open("customerFoodCartList.txt", "a")
                    customerFoodCart.write(itemCode + "; " + itemInfo + "; " + itemPrice + ";\n")
                    customerFoodCart.close()                       # close txt file
                    break
            else:
                print("Invalid item code! Please try again.")

        elif orderCode[0] == "E":                                     # open txt file if input is E
            menuDessertList = open("menuDessertList.txt", "r")
            for item in menuDessertList.readlines():                  # separate data in txt file
                data = item.split(";")
                itemCode = data[0]
                itemInfo = data[1]
                itemPrice = data[2]
                if itemCode == orderCode:
                    print(f"""
Item added to cart: {itemCode}- {itemInfo} """)
                    customerFoodCart = open("customerFoodCartList.txt", "a")
                    customerFoodCart.write(itemCode + "; " + itemInfo + "; " + itemPrice + ";\n")
                    customerFoodCart.close()                       # close txt file
                    break
            else:
                print("Invalid item code, please try again!")

        elif orderCode == "L":
            print("""
Leaving ordering page, returning to main page.""")
            mainMenu()                                              # call main menu function

        elif orderCode == "V":
            customerFoodCartMenu()                                  # call customerFoodCartMenu function

        else:
            print("Invalid code, please try again!")
            takeOrder()                                             # call takeOrder function


def menuOnly():
    print("""
-------------------------------------------
-------------------Menu--------------------
-------------------------------------------""")
    menu_special()                                                  # call menu special function
    print("")
    menu_rice()                                                     # call menu rice function
    print("")
    menu_noodle()                                                   # call menu noodle function
    print("")
    menu_ala_carte()                                                # call menu ala carte function
    print("")
    menu_dessert()                                                  # call menu dessert function
    print("")


def proceedToPayment():
    print("""
-------------------------------------------
-----------------Payment-------------------
-------------------------------------------

Item                                      Price
""")
    customerFoodCartList = open("customerFoodCartList.txt", "r")       # open txt file and read
    totalPrice = 0
    for item in customerFoodCartList.readlines():                  # separate data in txt file
        data = item.split(";")
        itemCode = data[0]
        itemInfo = data[1]
        itemPrice = float(data[2])
        totalPrice += itemPrice
        lengthInDigit = len(itemCode + itemInfo)                   # arrange data
        price_location = 40 - lengthInDigit
        print(itemCode + "-" + itemInfo + " " * price_location, "{:.2f}".format(itemPrice))
    print("\n", " " * 34, "===============")
    print(" " * 35, "Total: RM", "{:.2f}".format(totalPrice))
    print(" " * 35, "===============")
    customerPaymentConfirmation = input("""
Please enter one of the option provided (1-2):
1. Continue with payment
2. Return to previous page
Enter a number: """)
    if customerPaymentConfirmation == "1":
        CustomerName = input("Enter your name: ")
        confirmation = input("""
Are you sure you want to proceed to payment?
1.Yes
2.No
Enter a number: """)
    elif customerPaymentConfirmation == "2":
        customerFoodCartMenu()                                    # call customerFoodCartMenu Function
    else:
        print("Try again!")

    if confirmation == "1":
        customerFoodCartList = open("customerFoodCartList.txt", "r+")     # open txt file and read, placing the pointer at the beginning of the file
        customerOrderHistory = open("customerOrderHistory.txt", "a")      # open txt file in append mode
        adminOrderReceived = open("adminOrderReceived.txt", "a")          # open txt file in append mode
        for item in customerFoodCartList.readlines():                 # read data in txt file
            customerOrderHistory.write(CustomerName + "; ")           # write name then separate with ";" in txt file
            customerOrderHistory.write(item)                          # write item after ";"
            adminOrderReceived.write(CustomerName + "; ")             # write name then separate with ";" in txt file
            adminOrderReceived.write(item)                            # write item after ";"
        customerFoodCartList.truncate(0)                              # clear data in txt file
        customerFoodCartList.close()                                  # close txt file
        customerOrderHistory.write("\n")                              # write blank row in txt file
        customerOrderHistory.close()                                  # close txt file
        adminOrderReceived.close()                                    # close txt file
        payment()                                                     # call payment function
    elif confirmation == "2":
        proceedToPayment()                                            # call proceedToPayment function
    else:
        print("Try again!")
        proceedToPayment()                                            # call proceedToPayment function


def payment():
    paymentDone = input("""
-------------------------------------------
------------Payment Successful-------------
-------------------------------------------
Preparing your order....
Your order will be ready in 5 minutes.

Please enter one of the option provided (1-2):
1.Back to Menu
2.Logout
Enter a number: """)
    if paymentDone == "1":
        customerFoodCartMenu()                                        # call customerFoodCartMenu function
    elif paymentDone == "2":
        print("""Logging out...
You have been logged out.
        """)
        mainMenu()                                                    # call mainMenu function
    else:
        print("Try again!")
        payment()                                                     # call payment function


def admin(): # admin functions interface
    admin_choice = input("""                            
---------------Admin Login-----------------
Choose your option (1-2)
1. Sign up as new admin.
2. Login to existing account.
3. Back to main page.

Enter a number:""")                                         # accept input from user
    if admin_choice == "1":
        new_AdminUser()                                     # call functions that add new username of new admin
    elif admin_choice == "2":
        exist_adminUsername = input("Enter your username:") # accept input from user
        exist_adminPassword = input("Enter your password:") # accept input from user

        tempAdminUsernameList = []                          # create an empty list for new admin's username
        tempAdminPasswordList = []                          # create an empty list for new admin's password
        x = open("adminUsername&PasswordList.txt", "r")         # open text file and read
        for line in x.readlines():                          # separate data in text file with ";"
            data = line.split(";")
            username = data[0]
            password = data[1]
            tempAdminUsernameList.append(username)          # add data into text file
            tempAdminPasswordList.append(password)          # add data into text file
        x.close()                                           # close text file

        if exist_adminPassword in tempAdminPasswordList:    # to validate if the input from user match with data in text file
            if (exist_adminUsername in tempAdminUsernameList and tempAdminUsernameList.index(
                    exist_adminUsername) == tempAdminPasswordList.index(exist_adminPassword)):
                print("Login Successfully!")
                print(f"Welcome {exist_adminUsername.upper()}!")
                admin_page()                                # call functions that direct user to admin page
            else:
                print("Invalid username or password, please try again! ")
                admin()                                     # call functions that redirect user to admin login page
        else:
            print("Invalid username or password, please try again! ")
            admin()                                         # call functions that redirect user to admin login page
    elif admin_choice == "3":
        mainMenu()                                          # call functions that redirect user to main menu
    else:
        print("Please try again!")
        admin()                                             # call functions that redirect user to admin login page


def new_AdminUser():                                        # functions to add username of new admins
    tempAdminUsernameList = []                              # create an empty list for new admin's username
    adminUsernameList = open("adminUsernameList.txt", "r")      # open text file
    for aline in adminUsernameList.readlines():             # separate data with ";"
        data = aline.split(";")
        username = data[0]
        tempAdminUsernameList.append(username)              # add data in to list
    adminUsernameList.close()                               # clost text file

    adminUsername = input("Enter a username: ")
    if adminUsername in tempAdminUsernameList:              # username validation
        print("This username as been taken, please choose a new one.")
        new_AdminUser()                                     # redirect user to add username
    else:
        adminUsernameList = open("adminUsernameList.txt", "a")  # open text file
        x = open("adminUsername&PasswordList.txt", "a")
        adminUsernameList.write(adminUsername + ";" + "\n") # write in the text file
        x.write(adminUsername + ";")
        adminUsernameList.close()
        x.close()                                           # close text file
        new_AdminPas()                                      # call functions that accept input from user as new passwords


def new_AdminPas():                                         # functions to store new admin passwords
    adminPassword = input("Enter a password(at least 4 characters with numbers, upper & lower case): ")
    if len(adminPassword) < 4:                              # password validation
        print("Password is too short, please try again!""\n")
        new_AdminPas()                                      # redirect user to enter new passwords
    if not any(char.isupper() for char in adminPassword):   # check password for upper case
        print("Password must include at least one upper case, please try again!""\n")
        new_AdminPas()
    if not any(char.islower() for char in adminPassword):   # check password for lower case
        print("Password must include at least one lower case, please try again!""\n")
        new_AdminPas()
    if not any(char.isdigit() for char in adminPassword):   # check password for numerical character
        print("Password must include at least one numerical character, please try again!""\n")
        new_AdminPas()
    else:
        adminPasswordList = open("adminPasswordList.txt", "a")  # open text file
        adminUsernameAndPasswordList = open("adminUsername&PasswordList.txt", "a")  # open text file
        adminPasswordList.write(adminPassword + ";" + "\n")                     # write in text file
        adminUsernameAndPasswordList.write(adminPassword + ";" + "\n")          # write in text file
        adminPasswordList.close()                                               # close text file
        adminUsernameAndPasswordList.close()                                    # close text file
        print("""
    Registered successfully!
    Directing you to the Login Page.
            """)
    admin()                                                                     # redirect user back to admin interface


def admin_page():                           # admin interface design
    print("""
------------------Admin--------------------

Choose your option (1-5)
1.Modify Food Item
2.Display Food Records
3.Display Order & Payment History
4.Search order or Payment
5.Logout
""")

    redirectAdmin(userInput()) # call functions that accept input from admin to choose food category to add into the menu


def redirectAdmin(x):
    if x == "1":
        modifyFoodItem()                                            # call modifyFoodItem function
    elif x == "2":
        displayFoodRecords()                                        # call displayFoodRecords function
    elif x == "3":
        displayRecords()
    elif x == "4":
        searchOrderOrPayment()                                      # call searchOrderOrPayment function
    elif x == "5":
        mainMenu()                                                  # call mainMenu function
    else:
        print("Try again!")
        admin_page()                                                # call admin_page function


def modifyFoodItem():
    print("""
-------------Modify Food Item--------------
1.Add food item
2.Remove food item
3.Return to previous page
    """)

    redirectmodify(userInput())                                     # get input from user


def redirectmodify(x):
    if x == "1":
        addFoodItem()                                               # call addFoodItem function
    elif x == "2":
        removeFoodItem()                                            # call removeFoodItem function
    else:
        admin_page()                                                # call admin_page function


def addFoodItem():
    print("""
---------------Add Food Item---------------
Add Food Item Into:
1.Menu Special
2.Menu Rice
3.Menu Noodle
4.Menu Ala Carte
5.Menu Dessert
    """)

    redirectadd(userInput())                                       # get input from user


def redirectadd(x):
    if x == "1":
        addMenuSpecial()                                           # call addMenuSpecial function
    elif x == "2":
        addMenuRice()                                              # call addMenuRice function
    elif x == "3":
        addMenuNoodle()                                            # call addMenuNoodle function
    elif x == "4":
        addMenuAlaCarte()                                          # call addMenuAlaCarte function
    elif x == "5":
        addMenuDessert()                                           # call addMenuDessert function
    else:
        print("Try again!")
        addFoodItem()


def addMenuSpecial():
    print("""
---------------Add Food Item---------------
-----------Existing Menu Special-----------
    """)
    menu_special()                                                  # call menu_special function
    newItemCode = input("Enter an item code(Eg.A001): ")            # get input from user
    itemCodeList = open("itemCodeList.txt", "r")                    # open txt file and read

    tempSpecialCode = []                                            # create temp list

    for code in itemCodeList.readlines():                           # separate data in txt file
        data = code.split(";")
        specialCode = data[0]
    tempSpecialCode.append(specialCode)                             # add data into txt file

    if (newItemCode not in tempSpecialCode and len(newItemCode) == 4):
        itemCodeList.close()                                        # close txt file
        itemCodeList = open("itemCodeList.txt", "a")                    # open txt file and add data
        menuSpecialList = open("menuSpecialList.txt", "a")              # open txt file and add data

        itemCodeList.write(newItemCode + ";" + "\n")
        itemInfo = input("Enter the item info: ")                   # get input form user
        itemPrice = input("Enter the price of the item: ")          # get input form user

        menuSpecialList.write(newItemCode + ";" + itemInfo + ";" + itemPrice + ";" + "\n")
        print("Successfully Added Food Item!")
        menuSpecialList.close()                                     # close txt file
        menu_special()                                              # call menu_special function
    else:
        print("Invalid code, please try again! ")
        addMenuSpecial()                                            # call addMenuSpecial function
    modifyFoodItem()                                                # call modifyFoodItem function


def addMenuRice():
    print("""
    ---------------Add Food Item---------------
    -----------Existing Menu Special-----------
        """)
    menu_rice()                                                     # call menu_rice function
    newItemCode = input("Enter an item code(Eg.A001): ")            # get input from user
    itemCodeList = open("itemCodeList.txt", "r")                        # open txt file and read

    tempRiceCode = []                                               # create temp list

    for code in itemCodeList.readlines():                           # separate data in txt file
        data = code.split(";")
        riceCode = data[0]
    tempRiceCode.append(riceCode)                                   # add data into txt file

    if (newItemCode not in tempRiceCode and len(newItemCode) == 4):
        itemCodeList.close()                                        # close txt file
        itemCodeList = open("itemCodeList.txt", "a")                    # open txt file and add data
        menuRiceList = open("menuRiceList.txt", "a")                    # open txt file and add data

        itemCodeList.write(newItemCode + ";" + "\n")
        itemInfo = input("Enter the item info: ")                   # get input form user
        itemPrice = input("Enter the price of the item: ")          # get input form user

        menuRiceList.write(newItemCode + ";" + itemInfo + ";" + itemPrice + ";" + "\n")
        print("Successfully Added Food Item!")
        menuRiceList.close()                                        # close txt file
        menu_rice()                                                 # call menu_special function
    else:
        print("Invalid code, please try again! ")
        addMenuRice()                                               # call addMenuRice function
    modifyFoodItem()                                                # call modifyFoodItem function


def addMenuNoodle():
    print("""
        ---------------Add Food Item---------------
        -----------Existing Menu Special-----------
            """)
    menu_noodle()                                                   # call menu_noodle function
    newItemCode = input("Enter an item code(Eg.A001): ")            # get input from user
    itemCodeList = open("itemCodeList.txt", "r")                        # open txt file and read

    tempNoodleCode = []                                             # create temp list

    for code in itemCodeList.readlines():                           # separate data in txt file
        data = code.split(";")
        noodleCode = data[0]
    tempNoodleCode.append(noodleCode)                               # add data into txt file

    if (newItemCode not in tempNoodleCode and len(newItemCode) == 4):
        itemCodeList.close()                                        # close txt file
        itemCodeList = open("itemCodeList.txt", "a")                    # open txt file and add data
        menuNoodleList = open("menuNoodleList.txt", "a")                # open txt file and add data

        itemCodeList.write(newItemCode + ";" + "\n")
        itemInfo = input("Enter the item info: ")                   # get input form user
        itemPrice = input("Enter the price of the item: ")          # get input form user

        menuNoodleList.write(newItemCode + ";" + itemInfo + ";" + itemPrice + ";" + "\n")
        print("Successfully Added Food Item!")
        menuNoodleList.close()                                      # close txt file
        menu_noodle()                                               # call menu_noodle function
    else:
        print("Invalid code, please try again! ")
        addMenuNoodle()                                             # call addMenuNoodle function
    modifyFoodItem()                                                # call modifyFoodItem function


def addMenuAlaCarte():
    print("""
        ---------------Add Food Item---------------
        -----------Existing Menu Special-----------
            """)
    menu_ala_carte()                                                # call menu_ala_carte function
    newItemCode = input("Enter an item code(Eg.A001): ")            # get input from user
    itemCodeList = open("itemCodeList.txt", "r")                        # open txt file and read

    tempAlCode = []                                                 # create temp list

    for code in itemCodeList.readlines():                           # separate data in txt file
        data = code.split(";")
        alaCode = data[0]
    tempAlCode.append(alaCode)                                      # add data into txt file

    if (newItemCode not in tempAlCode and len(newItemCode) == 4):
        itemCodeList.close()                                        # close txt file
        itemCodeList = open("itemCodeList.txt", "a")                    # open txt file and add data
        menuAlaCarteList = open("menuAlaCarteList.txt", "a")            # open txt file and add data

        itemCodeList.write(newItemCode + ";" + "\n")
        itemInfo = input("Enter the item info: ")                   # get input form user
        itemPrice = input("Enter the price of the item: ")          # get input form user

        menuAlaCarteList.write(newItemCode + ";" + itemInfo + ";" + itemPrice + ";" + "\n")
        print("Successfully Added Food Item!")
        menuAlaCarteList.close()                                    # close txt file
        menu_ala_carte()                                            # call menu_ala_carte function
    else:
        print("Invalid code, please try again! ")
        addMenuAlaCarte()                                           # call addMenuAlaCarte function
    modifyFoodItem()                                                # call modifyFoodItem function


def addMenuDessert():
    print("""
        ---------------Add Food Item---------------
        -----------Existing Menu Special-----------
            """)
    menu_dessert()                                                 # call menu_dessert function
    newItemCode = input("Enter an item code(Eg.A001): ")           # get input from user
    itemCodeList = open("itemCodeList.txt", "r")                       # open txt file and read

    tempDessertCode = []                                           # create temp list

    for code in itemCodeList.readlines():                          # separate data in txt file
        data = code.split(";")
        dessertCode = data[0]
    tempDessertCode.append(dessertCode)                            # add data into txt file

    if (newItemCode not in tempDessertCode and len(newItemCode) == 4):
        itemCodeList.close()                                       # close txt file
        itemCodeList = open("itemCodeList.txt", "a")                   # open txt file and add data
        menuDessertList = open("menuDessertList.txt", "a")             # open txt file and add data

        itemCodeList.write(newItemCode + ";" + "\n")
        itemInfo = input("Enter the item info: ")                  # get input form user
        itemPrice = input("Enter the price of the item: ")         # get input form user

        menuDessertList.write(newItemCode + ";" + itemInfo + ";" + itemPrice + ";" + "\n")
        print("Successfully Added Food Item!")
        menuDessertList.close()                                    # close txt file
        menu_dessert()                                             # call menu_dessert function
    else:
        print("Invalid code, please try again! ")
        addMenuDessert()                                            # call menu_dessert function
    modifyFoodItem()                                                # call modifyFoodItem function


def removeFoodItem():
    print("""
--------------Remove Food Item-------------
Remove Food Item In:
1.Menu Special
2.Menu Rice
3.Menu Noodle
4.Menu Ala Carte
5.Menu Dessert
    """)

    redirectremove(userInput())                                     # get inout from user


def redirectremove(x):
    if x == "1":
        removeMenuSpecial()                                         # call removeMenuSpecial function
    elif x == "2":
        removeMenuRice()                                            # call removeMenuRice function
    elif x == "3":
        removeMenuNoodle()                                          # call removeMenuNoodle function
    elif x == "4":
        removeMenuAlaCarte()                                        # call removeMenuAlaCarte function
    elif x == "5":
        removeMenuDessert()                                         # call removeMenuDessert function
    else:
        print("Try again!")
        removeFoodItem()


def removeMenuSpecial():
    print("""
--------------Remove Food Item-------------
-----------Existing Menu Special-----------
""")
    menu_special()                                                 # call menu_special function
    removeItemCode = input("Enter the item code(Eg.A001): ")       # get input from user
    menuSpecialList = open("menuSpecialList.txt", "r")                 # open list and read

    tempList = []                                                  # create temp list

    for line in menuSpecialList.readlines():                       # separate data
        data = line.split(";")
        itemCode = data[0]

        if not itemCode == removeItemCode:
            tempList.append(line)                                  # add data in txt file

    menuSpecialList.close()                                        # close txt file
    menuSpecialList = open("menuSpecialList.txt", "w")                 # open list and write

    for item in tempList:
        menuSpecialList.write(item)                                # write data into list
    menuSpecialList.close()                                        # close list and write

    tempItemCode = []                                              # create temp list

    itemCodeList = open("itemCodeList.txt", "r")                       # open and read txt file
    for code in itemCodeList.readlines():                          # separate data
        data = code.split(";")
        itemCode = data[0]
        if not itemCode == removeItemCode:
            tempItemCode.append(code)                              # add data into temp list
    itemCodeList.close()                                           # close txt file

    itemCodeList = open("itemCodeList.txt", "w")                       # open txt file and write
    for code in tempItemCode:
        itemCodeList.write(code)                                   # write data
    itemCodeList.close()                                           # close text write

    print("Successfully Removed Food Item!")
    modifyFoodItem()                                               # call modifyFoodItem function


def removeMenuRice():
    print("""
--------------Remove Food Item-------------
------------Existing Menu Rice-------------
""")
    menu_rice()                                                    # call menu_rice function
    removeItemCode = input("Enter the item code(Eg.A001): ")       # get input from user
    menuRiceList = open("menuRiceList.txt", "r")                       # open list and read

    tempList = []                                                  # create temp list

    for line in menuRiceList.readlines():                          # separate data
        data = line.split(";")
        itemCode = data[0]

        if not itemCode == removeItemCode:
            tempList.append(line)                                  # add data in txt file

    menuRiceList.close()                                           # close txt file
    menuRiceList = open("menuRiceList.txt", "w")                       # open list and write

    for item in tempList:
        menuRiceList.write(item)                                   # write data into list
    menuRiceList.close()                                           # close list and write

    tempItemCode = []                                              # create temp list

    itemCodeList = open("itemCodeList.txt", "r")                       # open and read txt file
    for code in itemCodeList.readlines():                          # separate data
        data = code.split(";")
        itemCode = data[0]
        if not itemCode == removeItemCode:
            tempItemCode.append(code)                              # add data into temp list
    itemCodeList.close()                                           # close txt file

    itemCodeList = open("itemCodeList.txt", "w")                       # open txt file and write
    for code in tempItemCode:
        itemCodeList.write(code)                                   # write data
    itemCodeList.close()                                           # close text write

    print("Successfully Removed Food Item!")
    modifyFoodItem()                                               # call modifyFoodItem function


def removeMenuNoodle():
    print("""
--------------Remove Food Item-------------
------------Existing Menu Noodle-----------
""")
    menu_noodle()                                                  # call menu_noodle function
    removeItemCode = input("Enter the item code(Eg.A001): ")       # get input from user
    menuNoodleList = open("menuNoodleList.txt", "r")                   # open list and read

    tempList = []                                                  # create temp list

    for line in menuNoodleList.readlines():                        # separate data
        data = line.split(";")
        itemCode = data[0]

        if not itemCode == removeItemCode:
            tempList.append(line)                                  # add data in txt file

    menuNoodleList.close()                                         # close txt file
    menuNoodleList = open("menuNoodleList.txt", "w")                   # open list and write

    for item in tempList:
        menuNoodleList.write(item)                                 # write data into list
    menuNoodleList.close()                                         # close list and write

    tempItemCode = []                                              # create temp list

    itemCodeList = open("itemCodeList.txt", "r")                       # open and read txt file
    for code in itemCodeList.readlines():                          # separate data
        data = code.split(";")
        itemCode = data[0]
        if not itemCode == removeItemCode:
            tempItemCode.append(code)                              # add data into temp list
    itemCodeList.close()                                           # close txt file

    itemCodeList = open("itemCodeList.txt", "w")                       # open txt file and write
    for code in tempItemCode:
        itemCodeList.write(code)                                   # write data
    itemCodeList.close()                                           # close text write

    print("Successfully Removed Food Item!")
    modifyFoodItem()                                               # call modifyFoodItem function


def removeMenuAlaCarte():
    print("""
--------------Remove Food Item-------------
----------Existing Menu Ala Carte----------
""")
    menu_ala_carte()                                               # call menu_ala_carte function
    removeItemCode = input("Enter the item code(Eg.A001): ")       # get input from user
    menuAlaCarteList = open("menuAlaCarteList.txt", "r")               # open list and read

    tempList = []                                                  # create temp list

    for line in menuAlaCarteList.readlines():                      # separate data
        data = line.split(";")
        itemCode = data[0]

        if not itemCode == removeItemCode:
            tempList.append(line)                                  # add data in txt file

    menuAlaCarteList.close()                                       # close txt file
    menuAlaCarteList = open("menuAlaCarteList.txt", "w")               # open list and write

    for item in tempList:                                          # write data into list
        menuAlaCarteList.write(item)
    menuAlaCarteList.close()                                       # close list and write

    tempItemCode = []                                              # create temp list

    itemCodeList = open("itemCodeList.txt", "r")                       # open and read txt file
    for code in itemCodeList.readlines():                          # separate data
        data = code.split(";")
        itemCode = data[0]
        if not itemCode == removeItemCode:
            tempItemCode.append(code)                              # add data into temp list
    itemCodeList.close()                                           # close txt file

    itemCodeList = open("itemCodeList.txt", "w")                       # open txt file and write
    for code in tempItemCode:
        itemCodeList.write(code)                                   # write data
    itemCodeList.close()                                           # close text write

    print("Successfully Removed Food Item!")
    modifyFoodItem()                                               # call modifyFoodItem function


def removeMenuDessert():
    print("""
--------------Remove Food Item-------------
-----------Existing Menu Dessert-----------
""")
    menu_dessert()                                                 # call menu_dessert function
    removeItemCode = input("Enter the item code(Eg.A001): ")       # get input from user
    menuDessertList = open("menuDessertList.txt", "r")                 # open list and read

    tempList = []                                                  # create temp list

    for line in menuDessertList.readlines():                       # separate data
        data = line.split(";")
        itemCode = data[0]

        if not itemCode == removeItemCode:
            tempList.append(line)                                  # add data in txt file

    menuDessertList.close()                                        # close txt file
    menuDessertList = open("menuDessertList.txt", "w")                 # open list and write

    for item in tempList:
        menuDessertList.write(item)                                # write data into list
    menuDessertList.close()                                        # close list and write

    tempItemCode = []                                              # create temp list

    itemCodeList = open("itemCodeList.txt", "r")                       # open and read txt file
    for code in itemCodeList.readlines():                          # separate data
        data = code.split(";")
        itemCode = data[0]
        if not itemCode == removeItemCode:
            tempItemCode.append(code)                              # add data into temp list
    itemCodeList.close()                                           # close txt file

    itemCodeList = open("itemCodeList.txt", "w")                       # open txt file and write
    for code in tempItemCode:
        itemCodeList.write(code)                                   # write data
    itemCodeList.close()                                           # close text write

    print("Successfully Removed Food Item!")
    modifyFoodItem()                                               # call modifyFoodItem function


def displayFoodRecords():
    display_choice = input("""
Choose your option (1-3)
1. Display all food category.
2. Display all food items from all category.
3. Back

Enter a number:""")                                               # accept input form user
    if display_choice == "1":
        displayFoodCategory()                                     # call displayFoodCategory function
    elif display_choice == "2":
        displayFoodItems()                                        # call displayFoodItems function
    elif display_choice == "3":
        admin_page()                                              # call admin_page function
    else:
        print("Please try again!")
        displayFoodRecords()                                      # call displayFoodCategory function


def displayFoodCategory():
    print("""
---------------Food Category---------------
Special
Rice
Noodle
Ala Carte
Dessert

Insert "1" to go back to previous page. 
""")
    redirectviewfoodadmin = input("Enter a number:""\n")          # get input from user
    if redirectviewfoodadmin == "1":
        displayFoodRecords()                                      # call displayFoodCategory function
    else:
        print("Please try again!")
        displayFoodCategory()                                     # call displayFoodCategory function


def displayFoodItems():
    print("""
-------------------------------------------
-------------------Menu--------------------
-------------------------------------------""")
    menu_special()                                                # call menu_special function
    print("")
    menu_rice()                                                   # call menu_rice function
    print("")
    menu_noodle()                                                 # call menu_noodle function
    print("")
    menu_ala_carte()                                              # call menu_ala_carte function
    print("")
    menu_dessert()                                                # call menu_dessert function
    print("")
    redirectfooditemsadmin = input("""
Insert '1' to go back to the previous page.
Enter a number: """)                                              # get input from user
    if redirectfooditemsadmin == "1":
        displayFoodRecords()                                      # call displayFoodCategory function
    else:
        print("Please try again!")
        displayFoodItems()                                        # call displayFoodItems function


def displayRecords():
    display_choice = input("""
Choose your option (1-3)
1. Display all order history
2. Display all payment history
3. Back

Enter a number:""")
    if display_choice == "1":
        display_order()
    elif display_choice == "2":
        display_payment()
    elif display_choice == "3":
        admin_page()
    else:
        print("Try again!")
        displayRecords()


def order():
    tempadminOrderReceived = []  # create temp list
    order_no = 0
    x = open("adminOrderReceived.txt", "r")  # open file and read
    for order in x.readlines():  # separate data
        data = order.split(";")
        custname = data[0]
        itemCode = data[1]
        itemInfo = data[2]
        itemPrice = float(data[3])
        tempadminOrderReceived.append(custname)
        order_no += 1
        lengthInDigit = len(itemCode + itemInfo)
        price_location = 40 - lengthInDigit
        print(f"""
-------------------------------------------
---------------Order {order_no}--------------------
-------------------------------------------
Customer name:{custname.upper()}

Item                                      Price
""")
        print(itemCode + "-" + itemInfo + " " * price_location, "{:.2f}".format(itemPrice))
        print("\n", " " * 34, "===============")
        print(" " * 35, "Total: RM", "{:.2f}".format(itemPrice))
        print(" " * 35, "===============")


def display_order():
    print("""
-------------------------------------------
---------------Order History-------------
-------------------------------------------""")
    order()
    choices = input("""
Insert '1' to go back to the previous page.
Enter a number: """)
    if choices == "1":
        displayRecords()
    else:
        print("Try again!")
        display_order()


def payment_history():
    tempadminOrderReceived = []  # create temp list
    order_no = 0
    x = open("adminOrderReceived.txt", "r")  # open file and read
    for order in x.readlines():  # separate data
        data = order.split(";")
        custname = data[0]
        itemCode = data[1]
        itemInfo = data[2]
        itemPrice = float(data[3])
        tempadminOrderReceived.append(custname)
        order_no += 1
        lengthInDigit = len(itemCode + itemInfo)
        price_location = 40 - lengthInDigit
        print(f"""
-------------------------------------------
---------------Order {order_no}--------------------
-------------------------------------------
Customer name:{custname.upper()}

Item                                      Price
""")
        print(itemCode + "-" + itemInfo + " " * price_location, "{:.2f}".format(itemPrice))
        print("\n", " " * 34, "===============")
        print(" " * 35, "Total: RM", "{:.2f}".format(itemPrice))
        print(" " * 35, "===============")
        print(" " * 31, f"Payment status:Paid")


def display_payment():
    print("""
-------------------------------------------
---------------Payment History----------------
-------------------------------------------
""")
    payment_history()
    choices = input("""
Insert '1' to go back to the previous page.
Enter a number: """)
    if choices == "1":
        displayRecords()
    else:
        print("Try again!")
        display_payment()


def searchOrderOrPayment():
    search_choice = input("""
Choose your option (1-3)
1. Search for an order.
2. Search for a payment history.
3. Back

Enter a number:""")                                               # get input from user
    if search_choice == "1":
        search_order()                                            # call search_order function
    elif search_choice == "2":
        search_payment()                                          # call search_payment function
    elif search_choice == "3":
        admin_page()                                              # call admin_page function
    else:
        print("Please try again!")
        searchOrderOrPayment()                                    # call searchOderOrPayment function


def search_order():
    orders_info = input("Please type the name of the customer to search for the order:")
    print(f"""
-------------------------------------------
---------------Order History---------------
-------------------------------------------
Customer name:{orders_info.upper()}

Item                                      Price
""")                                                              # get input from user
    tempadminOrderReceived = []                                   # create temp list
    totalPrice = 0
    x = open("adminOrderReceived.txt", "r")                           # open file and read
    for order in x.readlines():                                   # separate data
        data = order.split(";")
        custname = data[0]
        itemCode = data[1]
        itemInfo = data[2]
        itemPrice = float(data[3])
        tempadminOrderReceived.append(custname)
        totalPrice += itemPrice
        lengthInDigit = len(itemCode + itemInfo)
        price_location = 40 - lengthInDigit
        print(itemCode + "-" + itemInfo + " " * price_location, "{:.2f}".format(itemPrice))

    print("\n", " " * 34, "===============")
    print(" " * 35, "Total: RM", "{:.2f}".format(totalPrice))
    print(" " * 35, "===============")
    redirect_admin()                                              # call redirect_admin function


def redirect_admin():
    redirectadmin = input("""
Please choose an option (1-2)
1. Search for another orders.
2. Back

Enter your option:""")                                            # get input from user
    if redirectadmin == "1":
        search_order()                                            # call search_order function
    elif redirectadmin == "2":
        searchOrderOrPayment()                                    # call searchOrderOrPayment function
    else:
        print("Please try again!")
        redirect_admin()                                          # call redirect_admin function


def search_payment():
    payment_info = input("Please type the name of the customer to search for the payment history:")
    print(f"""
-------------------------------------------
---------------Payment History-------------
-------------------------------------------
Customer name:{payment_info.upper()}

Item                                      Price
""")                                                             # get input from user
    tempadminOrderReceived = []                                  # create temp list

    totalPrice = 0
    adminOrderReceived = open("adminOrderReceived.txt", "r")         # open txt file and read
    for order in adminOrderReceived.readlines():                 # separate data
        data = order.split(";")
        custname = data[0]
        itemCode = data[1]
        itemInfo = data[2]
        itemPrice = float(data[3])
        tempadminOrderReceived.append(custname)
        totalPrice += itemPrice
        lengthInDigit = len(itemCode + itemInfo)
        price_location = 40 - lengthInDigit
        print(itemCode + "-" + itemInfo + " " * price_location, "{:.2f}".format(itemPrice))

    print("\n", " " * 34, "===============")
    print(" " * 35, "Total: RM", "{:.2f}".format(totalPrice))
    print(" " * 35, "===============")
    print(" " * 31, f"Payment status:Paid")
    redirect_admin2()                                           # call redirect_admin2 function


def redirect_admin2():
    redirectadmin2 = input("""
Please choose an option (1-2)
1. Search for another payment history
2. Back

Enter your option:""")                                          # get input from user
    if redirectadmin2 == "1":
        search_payment()                                        # call search_payment function
    elif redirectadmin2 == "2":
        searchOrderOrPayment()                                  # call searchOrderOrPayment function
    else:
        print("Please try again!")
        redirect_admin2()                                       # call redirect_admin2 function


def userInput():  # Function to accept input from user
    return input("Enter a number: ")


main()