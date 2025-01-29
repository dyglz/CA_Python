# String tipas | Text Type | <class 'str'>
# duomenys, išreikšti "teksto pavidalu"

# Python String Methods
# Note: All string methods returns new values. 
# They do not change the original string.

txt = "pyThon sTring methoDs"
print(txt)

# string.capitalize() 
#  
# returns a string where the first character
# is upper case, and the rest is lower case.
x = txt.capitalize()
print(x)

# string.casefold() 
#  
# returns a string where all the characters are lower case.
x = txt.casefold()
print(x)

# string.lower() 
#  
# returns a string where all the characters are lower case.
x = txt.lower()
print(x)

# string.center(length, character) 
#  
# will center align the string, 
# using a specified character (space is default) as the fill character.
x = txt.center(40, "^")
print(x)

# string.count(value, start, end) 
#  
# returns the number of times a specified value appears in the string.
x = txt.count("ho")
print(x)

# string.encode(encoding=encoding, errors=errors)
#  
# encodes the string, using the specified encoding. 
# If no encoding is specified, UTF-8 will be used.
txt2 = "My name is Ståle"
print(txt2.encode(encoding="ascii",errors="backslashreplace"))
print(txt2.encode(encoding="ascii",errors="ignore"))
print(txt2.encode(encoding="ascii",errors="namereplace"))
print(txt2.encode(encoding="ascii",errors="replace"))
print(txt2.encode(encoding="ascii",errors="xmlcharrefreplace"))

# string.endswith(value, start, end) 
#  
# returns True if the string ends with the specified value, otherwise False.
x = txt.endswith("s")
print(x)

# string.expandtabs(tabsize) 
#  
# sets the tab size to the specified number of whitespaces.
# default tabsize is 8
txt3 = "H\te\tl\tl\to"
print(txt3)
print(txt3.expandtabs())
print(txt3.expandtabs(2))
print(txt3.expandtabs(4))
print(txt3.expandtabs(10)) 

# string.find(value, start, end) 
#  
# returns index of the first occurrence of the specified value
# returns -1 if the value is not found
x = txt.find("z")
print(x)

# string.rfind(value, start, end) 
#  
# returns index of the last occurrence of the specified value
# returns -1 if the value is not found
x = txt.rfind("o")
print(x)


# string.index(value, start, end) 
#  
# returns index of the first occurrence of the specified value
# raises a ValueError if the value is not found
x = txt.index("T")
print(x)

# string.rindex(value, start, end) 
#  
# returns index of the last occurrence of the specified value
# raises a ValueError if the value is not found
x = txt.rindex("T")
print(x)


# string.isalnum() 
#  
# returns True if all the characters are alphanumeric, 
# meaning alphabet letter (a-z) and numbers (0-9)
# not alphanumeric: (space)!#%&? etc.
txt = "Company12"
x = txt.isalnum()
print(x)

# string.isalpha() 
#  
# returns True if all the characters are alphabet letters (a-z)
# not alphanumeric: (space)!#%&? etc.
txt = "Company"
x = txt.isalpha()
print(x)

# string.isascii() 
#  
# Returns True if all characters in the string are ascii characters
txt = "Company123"
x = txt.isascii()
print(x) 

# string.isdecimal() 
#  
# returns True if all the characters are decimals (0-9)
txt = "1234"
x = txt.isdecimal()
print(x) 

# string.isdigit() 
#  
# returns True if all the characters are digits, otherwise False
# Exponents, like ², are also considered to be a digit.
txt = "50800"
x = txt.isdigit()
print(x)

# string.isidentifier() 
#  
# returns True if the string is a valid identifier, otherwise False
# Exponents, like ², are also considered to be a digit.
# A string is considered a valid identifier if it only contains 
# alphanumeric letters (a-z) and (0-9), or underscores (_). 
# A valid identifier cannot start with a number, or contain any spaces.
txt = "Demo"
x = txt.isidentifier()
print(x) 

# string.islower() 
#  
# returns True if all the characters are in lower case, otherwise False
# Numbers, symbols and spaces are not checked, only alphabet characters.
txt = "hello world!"
x = txt.islower()
print(x) 

# string.isnumeric() 
#  
# returns True if all the characters are numeric (0-9), otherwise False
# Exponents, like ² and ¾ are also considered to be numeric values.
# "-1" and "1.5" are NOT considered numeric values, 
# because all the characters in the string must be numeric, 
# and the - and the . are not.
txt = "565543"
x = txt.isnumeric()
print(x) 

# string.isprintable() 
#  
# returns True if all the characters are printable, otherwise False
# Numbers, symbols and spaces are not checked, only alphabet characters.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x) 

# string.isspace() 
#  
# returns True if all the characters in a string are whitespaces, otherwise False
txt = "   "
x = txt.isspace()
print(x) 

# string.istitle() 
#  
# returns True if all words in a text start with a upper case letter, 
# AND the rest of the word are lower case letters, otherwise False
# Symbols and numbers are ignored.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x) 

# string.isupper() 
#  
# returns True if all the characters are in upper case, otherwise False
# Numbers, symbols and spaces are not checked, only alphabet characters
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) 

# string.join(iterable) 
#  
# takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

# string.ljust(length, character) 
#  
# will left align the string, using a specified character 
# (space is default) as the fill character
txt = "banana"
x = txt.ljust(20, "O")
print(x) 

# string.rjust(length, character) 
#  
# will right align the string, using a specified character 
# (space is default) as the fill character
txt = "banana"
x = txt.rjust(20, "O")
print(x) 

# string.lstrip(characters) 
#  
# removes any leading characters 
# (space is the default leading character to remove)
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",,,,,")
print(x) 

# string.maketrans(x, y, z) 
#  
# returns a mapping table that can be used 
# with the translate() method to replace specified characters.
txt = "Good night Sam!"
x = "mSa"     # incicate what you want to change
y = "eJo"     # what to replace with
z = "odnght"  # characters you want to remove
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable)) 

# string.translate(table) 
#  
# returns a string where some specified characters are replaced 
# with the character described in a dictionary, or in a mapping table
# If a character is not specified in the dictionary/table, the character will not be replaced.
# If you use a dictionary, you must use ascii codes instead of characters.
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable)) 

# string.partition(value) 
#  
# searches for a specified string, and 
# splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# string.rpartition(value) 
#  
# searches for the last occurrence of specified string, and 
# splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
txt = "I could eat bananas all day"
x = txt.rpartition("bananas")
print(x)

# string.replace(oldvalue, newvalue, count) 
#  
# replaces a specified phrase with another specified phrase.
# count: default is all occurrences
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 1)
print(x) 

# string.split(separator, maxsplit)  
#  
# splits a string into a list.
# can specify the separator, default separator is any whitespace
txt = "welcome to the jungle"
x = txt.split()
print(x)

# string.rsplit(separator, maxsplit)  
#  
# splits a string into a list, starting from the right.
# If no "max" is specified, this method will return the same as the split() method.
# maxsplit: default value is -1, which is "all occurrences"
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x) 

# string.strip(characters) 
#  
# removes any leading, and trailing whitespaces, 
# space is the default trailing character to remove
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite") 

# string.rstrip(characters) 
#  
# removes any trailing characters (characters at the end a string), 
# space is the default trailing character to remove
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x) 

# string.splitlines(keeplinebreaks) 
#  
# splits a string into a list. The splitting is done at line breaks
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x) 

# string.startswith(value, start, end) 
#  
# returns True if the string starts with the specified value, otherwise False
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x) 

# string.swapcase() 
#  
# returns a string where all the upper case letters are lower case and vice versa
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x) 

# string.title() 
#  
# returns a string where the first character in every word is upper case. 
# Like a header, or a title.
# If the word contains a number or a symbol, 
# the first letter after that will be converted to upper case.
txt = "Welcome to my world"
x = txt.title()
print(x) 

# string.upper() 
#  
# returns a string where all characters are in upper case.
# Symbols and Numbers are ignored.
txt = "Hello my friends"
x = txt.upper()
print(x) 

# string.zfill(len) 
#  
# adds zeros (0) at the beginning of the string, 
# until it reaches the specified length
# If the value of the len parameter is less than the 
# length of the string, no filling is done.
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10)) 




