class Smartphone:

    def __init__(self, brand, model, storage, battery=100):
        self._brand = brand
        self._model = model
        self._storage = storage
        self._battery = battery

    def charge(self):
        self._battery = 100
        print(f"{self._brand} {self._model} is fully charged! 🔋")

    def use_battery(self, amount):
        if self._battery >= amount:
            self._battery -= amount
            print(f"Battery used: {amount}%. Remaining: {self._battery}%")
        else:
            print("Low battery! Please charge. ⚠️")

    def display_info(self):
        print(f"{self._brand} {self._model} ({self._storage}GB) - Battery: {self._battery}%")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)  # Inherit from Smartphone
        self.cooling_system = cooling_system  # New attribute

    # New method specific to GamingPhone
    def enable_gaming_mode(self):
        print(f"🚀 Gaming mode activated with {self.cooling_system} cooling!")

    # Override use_battery (polymorphism)
    def use_battery(self, amount):
        super().use_battery(amount * 2)  # Gaming phones use more battery


# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 256)
phone2 = GamingPhone("ASUS", "ROG Phone 6", 512, "liquid-cooled")

phone1.display_info()  # Apple iPhone 15 (256GB) - Battery: 100%
phone2.enable_gaming_mode()  # 🚀 Gaming mode activated with liquid-cooled cooling!
phone2.use_battery(20)  # Battery used: 40%. Remaining: 60% ⚡
