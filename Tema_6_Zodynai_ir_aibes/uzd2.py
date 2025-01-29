# Aibė unikalumui

student_list = []
student_set = set(student_list)

while True:
    student_name = input("Please, enter student's name or 'done': ").title()
    if student_name == "Done":
        break
    student_set.add(student_name)


print(student_set)
print(type(student_set))