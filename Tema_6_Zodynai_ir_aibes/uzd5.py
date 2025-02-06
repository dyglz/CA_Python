# Mokinių pažymiai

# Pažymių žodyno kūrimas: Paprašykite vartotojo įvesti mokinių vardus ir pažymius,
# išsaugokite juos žodyne, kur vardas yra raktas, o pažymys – reikšmė.
# Vidurkio skaičiavimas: Naudokite Python sum() ir len() funkcijas.
# Mokinių su prastais pažymiais pašalinimas: Iteruokite per žodyną, 
# suraskite mokinius, kurių pažymiai yra mažesni nei 80, ir pašalinkite juos.
# Mokinio egzistavimo tikrinimas: Paprašykite įvesti mokinio vardą, 
# patikrinkite, ar šis vardas yra žodyne, ir atspausdinkite, ar toks mokinys rastas.


students_grades = {}

def remove_grades():
    students_to_remove = []
    for key, value in students_grades.items():
        if value < 80:
            students_to_remove.append(key)
    
    for student in students_to_remove:
        del students_grades[student]

    print(f"Students with grades in range [80-100]\n {students_grades}")

while True:
    new_student = input("Enter student's name (or 'done'): ")
    if new_student == "done":
        if students_grades:
            average = sum(students_grades.values()) / len(students_grades)
            print(f"The average grade is: {average:.2f}")
        else:
            print("Nothing entered! ")
        remove_grades()
        break

    try:
        grade = float(input("Enter the grade [0 - 100]: "))
        if 0 < grade <= 100:
            students_grades[new_student] = grade
            print(students_grades)
        else:
            print("Please, enter a grade between 0 - 100! ")
    except ValueError:
        print("Invalid input!")



while True:
    search_student = input("Enter student's name for search (or 'done'): ")
    if search_student == "done":
        print("End of the program. ")
        break
    if students_grades.get(search_student):
        student_index = students_grades[search_student]
        print(f"{search_student} is found! Grade: {student_index}")
    else:
        print(f"{search_student} is not found! ")