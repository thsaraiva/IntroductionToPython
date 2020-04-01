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


if __name__ == '__main__':
    def check_results_pants():
        pants = Pants('red', 35, 36, 15.12)
        assert pants.color == 'red'
        assert pants.waist_size == 35
        assert pants.length == 36
        assert pants.price == 15.12

        pants.change_price(10) == 10
        assert pants.price == 10

        assert pants.discount(.1) == 9

        print('You made it to the end of the check. Nice job!')


    check_results_pants()


    def check_results_sp():
        pants_one = Pants('red', 35, 36, 15.12)
        pants_two = Pants('blue', 40, 38, 24.12)
        pants_three = Pants('tan', 28, 30, 8.12)

        salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

        assert salesperson.first_name == 'Amy'
        assert salesperson.last_name == 'Gonzalez'
        assert salesperson.employee_id == 2581923
        assert salesperson.salary == 40000
        assert salesperson.pants_sold == []
        assert salesperson.total_sales == 0

        salesperson.sell_pants(pants_one)
        salesperson.pants_sold[0] == pants_one.color

        salesperson.sell_pants(pants_two)
        salesperson.sell_pants(pants_three)

        assert len(salesperson.pants_sold) == 3
        assert round(salesperson.calculate_sales(), 2) == 47.36
        assert round(salesperson.calculate_commission(.1), 2) == 4.74

        print('Great job, you made it to the end of the code checks!')


    check_results_sp()
