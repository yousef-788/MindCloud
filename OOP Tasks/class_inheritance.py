class Phone:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        try:
            num = int(number) 
        except (ValueError, TypeError):
            raise ValueError("Number must be an integer.")

        if name not in self.contacts:
            self.contacts[name] = num
        else:
            print(f"{name} is already in your contacts.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print(f"{name} not found in contacts.")

    def make_call(self, name):
        if name in self.contacts:
            print(f"calling {name}...")
        else:
            print(f"{name} not found in contacts.")


class Camera:
    def take_pic(self):
        print("The picture was taken successfully")


class Smartphone(Phone, Camera):
    pass

sp = Smartphone()
sp.add_contact("Mohamed", "01012345678")
sp.add_contact("Ali", "01098765432")
sp.make_call("Mohamed")
sp.take_pic()
