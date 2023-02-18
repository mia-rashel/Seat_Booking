import csv
import sqlite3


class Customer:

    def __init__(self):
        self.username = None
        self.password = None

    def customerLogin(self):

        con = sqlite3.Connection('customerDb.sqlite3')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS "CustomerData" (username text, password text);')
        cur.execute('''INSERT INTO CustomerData (username, password) VALUES ('shubha', 'shubha12')''')
        cur.execute('''INSERT INTO CustomerData (username, password) VALUES ('rashel', 'rashel12')''')
        cur.execute('''INSERT INTO CustomerData (username, password) VALUES ('suebee', 'sueB12')''')
        con.commit()

        while True:
            print("----------------------------------------------------------------")
            self.username = input("Enter  username  :")
            self.password = input("Enter  password  :")

            result = con.execute("SELECT * FROM CustomerData WHERE username=? AND password=?",
                                 (self.username, self.password)).fetchone()

            if result:
                print("User login success:", result)
            else:
                print("User not found")
            con.close()
            break

    def customerNewUser(self):

        con = sqlite3.Connection('customerDb.sqlite3')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS "CustomerData" (username text, password text);')
        self.username = input("Enter  username  :")
        self.password = input("Enter  password  :")

        cur.execute('''INSERT INTO CustomerData (username, password) VALUES (?, ?)''', (self.username, self.password))

        con.commit()
        record = con.execute("SELECT * FROM CustomerData").fetchall()
        result = con.execute("SELECT * FROM CustomerData WHERE username=? AND password=?",
                             (self.username, self.password)).fetchone()
        print(record)

        if result:
            print("User login success:", result)
        else:
            print("User not found")
        con.close()

    def customerSelectService(self):
        print("----------------------------------------------------------------")
        print("1. Book A Seat\t")
        print("2. See Bookings\t")
        userInput = int(input("Choose your option:"))
        pass

    def customerSelectServiceType(self):
        print("----------------------------------------------------------------")
        print("Choose your service: Restaurant\Cinema\Airplane\Conference\t")
        print("\t")
        userInput = input("Choose your option:")
        return userInput

    def customerSelectFrom(self):
        print("----------------------------------------------------------------")
        print("1. Business Owner\t")
        print("2. Reseller\t")
        userInput = int(input("Choose your option:"))
        return userInput



    def customerDisplayBusinessOwnerList(self):
        con = sqlite3.Connection('businessownerDb.sqlite3')
        cur = con.cursor()
        record = con.execute("SELECT * FROM boRoomData").fetchall()
        print(record)

    pass

    def customerDisplayResellerList(self):
        pass

    def customerBookAseat(self):

        print("----------------------------------------------------------------")
        print("1. Book A Seat\t")
        print("2. See Bookings\t")
        userInput = int(input("Choose your option:"))

        pass

    def customerShowSeatBooking(self):

        pass
