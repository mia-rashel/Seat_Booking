
from businessOwner import *
from admin import *
from customer import *
from createRoom import *


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

    if ch == 2:

        businessOwnerObj.businessOwnerLogin()
        createRoomObj.capacity()
        print("1.Show the Seats.")
        ch = int(input())
        if ch ==1:
            createRoomObj.show_the_seats()

    if ch == 3:
        # admin class object creation
        customerObj.customerLogin()


start()  # calling function
# =======================================================================