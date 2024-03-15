from enum import IntEnum

class CarType(IntEnum):
    BIG = 1
    MEDIUM = 2
    SMALL = 3

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        self.curr_big = 0
        self.curr_medium = 0
        self.curr_small = 0

    def addCar(self, carType: int) -> bool:
        if carType == CarType.BIG and self.big > self.curr_big:
            self.curr_big += 1
            return True
        
        if carType == CarType.MEDIUM and self.medium > self.curr_medium:
            self.curr_medium += 1
            return True

        if carType == CarType.SMALL and self.small > self.curr_small:
            self.curr_small += 1
            return True
        
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
