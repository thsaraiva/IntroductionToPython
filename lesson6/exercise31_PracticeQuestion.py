# 1. Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary.
#
# 2. The main (separate) function should take user input (user's first name and last name)
#
# 3. and parse the user input to
# identify the first letter of the first name. It should then use it to print the flower name with the same first
# letter (from dictionary created in the first function).
# Sample Output:
# >>> Enter your First [space] Last name only: Bill Newman
# >>> Unique flower name with the first letter: Bellflower


def create_flowers_dictionary(filename):
    dic = {}
    try:
        with open(filename) as flower_file:
            for line in flower_file:
                items = line.split(':')
                flower_dic[items[0].strip()] = items[1].strip()
    except OSError:
        print('Error opening {}} file!'.format(filename))
    return dic


if __name__ == '__main__':
    name = input('Enter your name: ')
    first_letter = name[0]
    flower_dic = create_flowers_dictionary('../resources/flowers.txt')
    if len(flower_dic) == 0:
        print('Program finished with error!')
    else:
        print('Unique flower name with the first letter: {}.'.format(flower_dic.get(first_letter)))
