from pants import Pants
from sales_person import SalesPerson
from time import time, sleep


def check_results_pants():
    p = Pants('red', 35, 36, 15.12)
    assert p.color == 'red'
    assert p.waist_size == 35
    assert p.length == 36
    assert p.price == 15.12

    p.change_price(10) == 10
    assert p.price == 10

    assert p.discount(.1) == 9

    print('You made it to the end of the check. Nice job!')


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


start = time()
check_results_pants()
sleep(1)
check_results_sp()
end = time()
print("Total time: {} seconds".format((end - start).strftime("%H:%M:%S")))
