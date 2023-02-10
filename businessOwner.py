import csv
class BusinessOwner:
    def __init__(self):
        self.username = None
        self.password = None

    def businessOwnerLogin(self):
        actList = []
        with open('businessOwnerLogin.csv','r+',newline ="") as f:
            r = csv.reader(f)
            data = list(r)
            for i in data:
                for j in i :
                    actList.append(j)

        while (True):
            print("----------------------------------------------------------------")
            print()
            self.username = input("Enter  username  :")
            self.password = input("Enter  password  :")
            if self.username == str(actList[0]) and self.password == str(actList[1]):
                print()
                print("Login successfully")
                break
            else:
                print("Enter correct username and password")
            print()
            print("---------------------------------------------------------------")



