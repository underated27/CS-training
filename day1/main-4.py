class VendingMachine:
    def __init__(self, capacity=200, stock=70):
        self.capacity = capacity
        self.stock = stock

    def request_pepsi(self):
        n = int(input("How many bottles of Pepsi would you like? "))
        if n <= self.stock:
            for _ in range(n):
                print("Take your Pepsi")
            self.stock -= n
        else:
            for _ in range(self.stock):
                print("Take your Pepsi")
            print("Out of stock")
            self.stock = 0
        print("Happy drinks")


machine = VendingMachine()
machine.request_pepsi()
machine.request_pepsi()
machine.request_pepsi()
