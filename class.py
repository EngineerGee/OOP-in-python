# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def show_info(self):
        print(f"Device: {self.brand} {self.model}")

# Child Class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.__battery = battery   # encapsulated attribute (private)

    def charge(self, amount):
        """Increase battery level safely."""
        if 0 < amount <= 100:
            self.__battery = min(100, self.__battery + amount)
        print(f"Battery now: {self.__battery}%")

    def use(self, hours):
        """Decrease battery level when using phone."""
        drain = hours * 10
        self.__battery = max(0, self.__battery - drain)
        print(f"Used for {hours} hrs. Battery now: {self.__battery}%")

    # Getter for battery
    def get_battery(self):
        return self.__battery


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S21", "128GB", 75)
phone1.show_info()
print("Battery:", phone1.get_battery(), "%")
phone1.charge(15)
phone1.use(3)
