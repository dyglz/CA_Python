# su string galime išrinkti tam tikrus žodžio simbolius:

# find a character by index
name = "Code Academy"
print(name[5])
# A

# find character by index from the end of the string
print(name[-2])
# m

# interval index[5-12]
print(name[5:12])
# Academy

# interval from index 5 forward
print(name[5:])
# Academy

# interval till index 4
print(name[:4])
# Code

# interval index[5-12] print every 3rd letter
print(name[5:12:3])
# Ady

# interval from index 5 forward print every second letter
print(name[5::2])
# Aaey

# prints backwards
print(name[::-1])
# ymedacA edoC


