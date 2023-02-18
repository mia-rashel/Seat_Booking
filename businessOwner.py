
import sqlite3

class BusinessOwner:
    def __init__(self):
        self.username = None
        self.password = None

    def businessOwnerLogin(self):
        con = sqlite3.Connection('businessownerDb.sqlite3')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS "BusinessOwnerData" (username text, password text);')
        cur.execute('''INSERT INTO BusinessOwnerData (username, password) VALUES ('shubha', 'shubha12')''')
        cur.execute('''INSERT INTO BusinessOwnerData (username, password) VALUES ('rashel', 'rashel12')''')
        con.commit()

        while True:
            print("----------------------------------------------------------------")
            self.username = input("Enter  username  :")
            self.password = input("Enter  password  :")

            result = con.execute("SELECT * FROM BusinessOwnerData WHERE username=? AND password=?",
                                 (self.username, self.password)).fetchone()

            if result:
                print("User login success:", result)
            else:
                print("User not found")
            con.close()
            break
        return self.username

    def businessOwnerNewUser(self):

        con = sqlite3.Connection('businessownerDb.sqlite3')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS "BusinessOwnerData" (username text, password text);')
        self.username = input("Enter  username  :")
        self.password = input("Enter  password  :")

        cur.execute('''INSERT INTO BusinessOwnerData (username, password) VALUES (?, ?)''', (self.username, self.password))

        con.commit()

        result = con.execute("SELECT * FROM BusinessOwnerData WHERE username=? AND password=?",
                             (self.username, self.password)).fetchone()

        if result:
            print("User login success:", result)
        else:
            print("User not found")
        con.close()

        return self.username
