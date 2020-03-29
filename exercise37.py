# 1. Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split()[0] for name in names]
print(first_names)
print(" ## END  ## \n")

# 2. Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

multiples_3 = [number * 3 for number in range(1, 21)]
print(multiples_3)
print(" ## END  ## \n")

# 3 Use a list comprehension to create a list of names passed that only include those that scored at least 65.
scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
