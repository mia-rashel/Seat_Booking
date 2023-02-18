#import user_info
import csv
import sqlite3
import businessOwner

class CreateRoom:

    global matrix, total_seats_booked
    matrix = []

    def __init__(self):
        self.room_size = None
        self.regular_price = None
        self.room_type = None

    def makeaRoom(self, usernm):
        print("1.Restaurant ")
        print("2.Movie Theatre")
        print("3.Airplane")
        print("4.Conference Room")
        ch = int(input("Choose Service Type: \t"))
        if ch == 1:
            room_type = "Restaurant"

        if ch == 2:
            room_type = "Movie Theatre"
        if ch == 3:
            room_type = "Airplane"
        if ch == 4:
            room_type = "Conference Room"

        room_size = int(input("Enter room size"))
        total_seats = room_size * room_size
        io_pricing = int(input("Enter regular seat price"))

        con = sqlite3.Connection('businessownerDb.sqlite3')
        cur = con.cursor()

        cur.execute(
            'CREATE TABLE IF NOT EXISTS "boRoomData" (boname text, servicetype text, seatID int, Pricing int, Status text);')

        seat_id = 1
        while seat_id <= total_seats:

            cur.execute('''INSERT INTO boRoomData (boname, servicetype, seatID, Pricing, Status) VALUES (?, ?, ?, ?, ?)''',
                    (usernm, room_type,seat_id, io_pricing, 'available'))
            seat_id = seat_id +1

        con.commit()

        frontrow_price = ((100 * io_pricing) / 100) + io_pricing
        lastrow_price = io_pricing - ((25 * io_pricing) / 100)
        middlerow_price = io_pricing + ((25 * io_pricing) / 100)
        regular_price = io_pricing
        lastr = total_seats-room_size

        cur.execute("UPDATE boRoomData SET Pricing = ? WHERE seatID <= ? ", (frontrow_price, room_size ))
        con.commit()
        cur.execute("UPDATE boRoomData SET Pricing = ? WHERE seatID >= ? ", (lastrow_price, lastr ))
        con.commit()
        #cur.execute("UPDATE boRoomData SET Pricing = ? WHERE seatID <= ? ", (frontrow_price, room_size ))
        #con.commit()


        record = cur.execute("SELECT * FROM boRoomData").fetchall()
        print(record)

        con.close()

    def service_type(self):
        print("1.Restaurant ")
        print("2.Movie Theatre")
        print("3.Airplane")
        print("4.Conference Room")

        ch = int(input("Choose Service Type: \t"))

        if ch ==1:
            self.room_type = "Restaurant"

        if ch ==2:
            self.room_type = "Movie Theatre"
            w.writerows(self.room_type)
        if ch ==3:
            self.room_type = "Airplane"
            w.writerows(self.room_type)
        if ch ==4:
            self.room_type = "Conference Room"
            w.writerows(self.room_type)

        pass

    def capacity(self):

        self.room_size = int(input("Enter Room Size "))

        for i in range(self.room_size + 1):
            a = []
            for j in range(self.room_size + 1):
                a.append("S")
            matrix.append(a)

        total_seats = self.room_size * self.room_size
        return total_seats, self.room_size, self.room_size

    def set_ticket_price(self):
        pass

    def show_the_seats(self):

        for i in range(0, self.room_size + 1):
            if i == 0:
                for j in range(0, self.room_size + 1):
                    print(j, end=" ")
            else:
                print(i, end=" ")
                for k in range(self.room_size):
                    print(matrix[i - 1][k], end=" ")
            print()

    def total_seats(self):
        pass

    def see_your_room(self,usernm):
        con = sqlite3.Connection('businessownerDb.sqlite3')
        cur = con.cursor()
        rec = []
        rec = cur.execute("SELECT boname FROM boRoomData WHERE boname = (?)", [usernm]).fetchall()

        records_without_boname = cur.execute("SELECT boname,servicetype,seatID,Pricing,Status FROM boRoomData WHERE boname = ? ", [usernm]).fetchall()
        #print(rec)
        #for record in rec:
        if rec:
            for i in records_without_boname:
                print(i)
        else:
            print("No records found. Do you want to make a new room?")
            print("1.Yes")
            print("2.No")

            ch = int(input("Choose your option:\t"))
            if ch==1:
                self.makeaRoom()
            else:
                pass




        #else:
           # print("No room")

           # if record == True:
                #for record_without_boname in records_without_boname:
                    #print(record_without_boname)


            #else:
                #print("You dont have any room. Do you want to create a room.Do you want to create a room?")
                #print("1.Yes")
                #print("2.No")

                #ch = int(input("Chose your option:\t"))
                #if ch ==1:
                    #CreateRoom()
                #else:
                    #pass


