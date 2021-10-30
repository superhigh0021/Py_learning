class Vehicle:
    def __init__(self):
        self.__MaxSpeed = 0
        self.__weight = 0


class Bicycle(Vehicle):
    def __init__(self):
        self.__height = 0

    def SetMaxSpeed(self, speed):
        self.__MaxSpeed = speed

    def print_height(self):
        print(self.__height)

    def modify_height(self, height):
        self.__height = height

    def del_height(self):
        del self.__height

    height = property(print_height, modify_height, del_height)


v = Bicycle()
v.modify_height(12)
print(v.height)