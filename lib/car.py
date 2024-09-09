from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    pass


hilux = Car(56, 3)

fielder = Vehicle(35, 2)

print(hilux.go())

print(fielder.go())

print(int.__bases__)