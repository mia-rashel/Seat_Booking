
from businessOwner import *
from admin import *
from customer import *
from createRoom import *
import time


def start():  # called function
    print("1. Admin Login :\t")
    print("2. Business Owner Login :\t")
    print("3. Customer Login :\t")
    print()
    adminObj = Admin()
    customerObj = Customer()
    createRoomObj = CreateRoom()
    businessOwnerObj = BusinessOwner()
    ch = int(input("Choose Correct option :"))

    if ch == 1:
        # admin class object creation
        adminObj.adminLogin()

    elif ch == 2:

        if ch == 2:
            print("1. New User\t")
            print("2. User Login :\t")
            opt_c = int(input("Choose Your option :"))
            if opt_c == 1:
                name = businessOwnerObj.businessOwnerNewUser()
            if opt_c == 2:
                name = businessOwnerObj.businessOwnerLogin()
        while ch != 0 :
            print("1. See Your Room")
            print("2. Make Your Room")

            ch = int(input("Choose Your Option:\t"))
            if ch ==1:

                createRoomObj.see_your_room(name)

            elif ch==2:
                createRoomObj.makeaRoom(name)

            else:
                print("Choose the Correct Option")

            time.sleep(2)
    elif ch == 3:
        # admin class object creation
        print("1. New User\t")
        print("2. User Login :\t")
        opt_c = int(input("Choose Your option :"))
        if opt_c == 1:
            customerObj.customerNewUser()
        if opt_c == 2:
            customerObj.customerLogin()


start()  # calling function
# =======================================================================