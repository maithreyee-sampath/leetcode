class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        #by default initializes the kind of car spaces we have available
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        #first check if we have the availability:
        # if yes then reduce by 1 and return true or else return false

        if self.spaces[carType-1] > 0:
            self.spaces[carType-1] -=1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)