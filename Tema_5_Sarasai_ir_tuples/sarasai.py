my_list = []

name = "Tomas"
name2 = "Jonas"
name3 = "1"
name4 = 1
name5 = "1"

my_list.append(name) # kintamojo idejimas i sarasa
my_list.append(name2) # visada eis i GALA listo
my_list.append(name3)
my_list.append(name4)
my_list.append(name5)

print(my_list)

print(my_list.count('1')) # suskaiciuoti kiek '1' yra liste

my_list.insert(1, 50) # ideti '50' i lista 1 indeksu
print(my_list)

my_list.remove("Jonas")
print(my_list)

my_list.insert(1, "Jonas") #ideti kitamaji i lista (1 indeksas)
print(my_list)

del my_list[-1]  # paskutinio elemento pašalinimas iš sąrašo
print(my_list) 

print(len(my_list)) # atspausdinti, kiek kintamuju yra liste

number_list = [50, 99, 1, -50]
print(max(number_list))

number_list = [50, 99, 1, -50]
print(min(number_list))

for item in number_list:
    print(item + 1)

third_list = ["pirmas", "antras", "trečias"]
print(third_list[:1])
print(third_list[::2]) # kas antras
print(third_list[::-1]) # nuo galo
print(third_list[0:2]) # intervalas


one_list = [1, 2, 3]
print(1 in one_list) # output -> True/False
if 1 in one_list:   
    print("I have 1 in my list")
else:
    print("I do not have 1 in my list")

