# Imagine you're a teacher who needs to send a message to each of your students reminding them of their missing
# assignments and grade in the class. You have each of their names, number of missing assignments, and grades on
# a spreadsheet and just have to insert them into placeholders in this message you came up with:
#
#     Hi [insert student name],
#
#     This is a reminder that you have [insert number of missing assignments] assignments left to submit before
#     you can graduate. Your current grade is [insert current grade] and can increase to [insert potential grade]
#     if you submit all assignments before the due date.
#
# You can just copy and paste this message to each student and manually insert the appropriate values each time,
# but instead you're going to write a program that does this for you.
#
# Write a script that does the following:
# 1. Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once
# for a list of grades. Use this input to create lists for names, assignments, and grades.
#
# 2. Use a loop to print the message for each student with the correct values. The potential grade is simply the
# current grade added to two times the number of missing assignments.

# word = input('Enter a word:')
# print(word)

# age = int(input('Enter student age:'))
# print(age)
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

names = input('Enter student\'s names: ').split(',')
counts = input('Enter number of missing assignments: ').split(',')
grades = input('Enter list of grades: ').split(',')

for name, count, grade in zip(names, counts, grades):
    count_int = int(count.strip())
    grade_int = int(grade.strip())
    print(message.format(name.strip(), count_int, grade_int, grade_int + 2 * count_int))

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
