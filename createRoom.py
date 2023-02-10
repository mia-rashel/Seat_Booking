#import user_info


class CreateRoom:

    global matrix, total_seats_booked
    matrix = []

    def __init__(self):
        self.room_size = None
        self.regular_price = None

    def capacity(self):

        self.room_size = int(input("Enter Room Size "))
        self.regular_price = int(input("Enter Regular Price "))
        for i in range(self.room_size + 1):
            a = []
            for j in range(self.room_size + 1):
                a.append("S")
            matrix.append(a)

        total_seats = self.room_size * self.room_size
        return total_seats, self.room_size, self.room_size

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
