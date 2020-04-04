class Pants:
    def __init__(self, pants_color, pants_waits_size, pants_length, pants_price):
        self.color = pants_color
        self.waist_size = pants_waits_size
        self.length = pants_length
        self.price = pants_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)
