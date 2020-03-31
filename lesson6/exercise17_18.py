# directory = "/Users/thsaraiva/Documents/Python/UdacityCourse/"
# filename = "file.txt"


# f = open(directory + filename, 'r')
# print(f.read())
# f.close()

# or

# lines = []
# with open(directory + filename, 'r') as f:
# print(f.read(8))
# print(f.readline())
# print(f.read())
# for line in f:
#     lines.append(line)

# print(lines)


# Receives a file name as input and return a list of actors names


def create_cast_list(file_name):
    actor_names = []
    with open(file_name, 'r') as file:
        for actor_info in file:
            actor_names.append(actor_info.split(',')[0].strip())
    return actor_names


print(create_cast_list("/Users/thsaraiva/Documents/Python/UdacityCourse/imdb_actors_info.txt"))
