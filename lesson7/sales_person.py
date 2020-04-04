class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants):
        self.pants_sold.append(pants)

    def calculate_sales(self):
        return sum(map(lambda pants: pants.price, self.pants_sold))

    def display_sales(self):
        for pants in self.pants_sold:
            print("color: {}}, waist_size: {}}, length: {}}, price: {}}"
                  .format(pants.color, pants.waist_size, pants.length, pants.price))

    def calculate_commission(self, percentage):
        return self.calculate_sales() * percentage
