
# duomenų tipai naudojami kintamojo tipui apibrėžti
# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	    NoneType


# String tipas | Text Type | <class 'str'>
# duomenys, išreikšti "teksto pavidalu"
some_chars = "Python Data Types"
print(some_chars)
print(type(some_chars))
# Setting data type
x = str("Hello World")
print(type(x))

# Sveikieji skaičiai (integer) <class 'int'>
# ℤ = {..., -3, -2, -1, 0, 1, 2, 3, ...}
x = 5
print(type(x))
# Setting data type
x = int(20)
print(type(x))

# Racionalieji skaičiai (float) <class 'float'>
# ℚ = {..., -2.5, ..., 0, ..., 2.5, ...}
x = 5.5
print(type(x))
# Setting data type
x = float(20.5)
print(type(x))

# Numeric Type | <class 'complex'>
x = 1j
print(type(x))
# Setting data type
x = complex(1j)
print(type(x))


# Boolean Type | <class 'bool'>
x = True
print(type(x))
# Setting data type
x = bool(5)
print(type(x))


# Sequence Type | <class 'list'>
x = ["apple", "banana", "cherry"]
print(type(x))
# Setting data type
x = list(("apple", "banana", "cherry"))
print(type(x))


# Sequence Type | <class 'tuple'>
x = ("apple", "banana", "cherry")
print(type(x))
# Setting data type
x = tuple(("apple", "banana", "cherry"))
print(type(x))


# Sequence Type | <class 'range'>
x = range(6)
print(type(x))
# Setting data type
x = range(6)
print(type(x))


# Mapping Type | <class 'dict'>
x = {"name" : "John", "age" : 36}
print(type(x))
# Setting data type
x = dict(name="John", age=36)
print(type(x))


# Set Type | <class 'set'>
x = {"apple", "banana", "cherry"}
print(type(x))
# Setting data type
x = set(("apple", "banana", "cherry"))
print(type(x))


# Set Type | <class 'frozenset'>
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
# Setting data type
x = frozenset(("apple", "banana", "cherry"))
print(type(x))


# Binary Type | <class 'bytes'>
x = b"Hello"
print(type(x))
# Setting data type
x = bytes(5)
print(type(x))


# Binary Type | <class 'bytearray'>
x = bytearray(5)
print(type(x))
# Setting data type
x = bytearray(5)
print(type(x))


# Binary Type | <class 'memoryview'>
x = memoryview(bytes(5))
print(type(x))
# Setting data type
x = memoryview(bytes(5))
print(type(x))


# None Type | <class 'NoneType'>
x = None
print(type(x))


