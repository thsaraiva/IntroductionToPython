# 1. Write your own generator function that works like the built-in function enumerate. Calling the function like this:
#
# lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
#
# for i, lesson in my_enumerate(lessons, 1):
#     print("Lesson {}: {}".format(i, lesson))
#
# should output:

# Lesson 1: Why Python Programming
# Lesson 2: Data Types and Operators
# Lesson 3: Control Flow
# Lesson 4: Functions
# Lesson 5: Scripting

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    return zip(range(start, len(iterable) + start), iterable)


for index, lesson in my_enumerate(lessons, 4):
    print("Lesson {}: {}".format(index, lesson))

print(" ## END  ## \n")


# 2. If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files),
# being able to take and use chunks of it at a time can be very valuable.
#
# Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.
#
# Calling the function like this:
#
# for chunk in chunker(range(25), 4):
#     print(list(chunk))
#
# should output:
#
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]
# [16, 17, 18, 19]
# [20, 21, 22, 23]
# [24]

def chunker(iterable, size):
    pos = 0
    while pos < len(iterable):
        yield iterable[pos:pos + size]
        pos += size


for chunk in chunker(range(25), 4):
    print(list(chunk))
