class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement 'move()'.")
    
class Car(Vehicle):
    def move(self):
        print("Driving on the road! 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky! ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water! ⛵")
    
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()

# Output:
# Driving on the road! 🚗
# Flying in the sky! ✈️
# Sailing on water! ⛵