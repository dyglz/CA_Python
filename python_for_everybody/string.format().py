# format_map() -> Formats specified values in a string
# string.format(value1, value2...) 
# 
# formats the specified value(s) and insert them 
# inside the string's {placeholder}.
# returns the formatted string.

# can be identified using:
# named indexes {price}
# numbered indexes {0}
# empty placeholders {}

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36) 
# My name is John, I'm 36




# Formatting types

# :<
# Left aligns the result (within the available space)
txt = "We have {:<8} chickens."
print(txt.format(49))
# We have 49       chickens.

# :>
# Right aligns the result (within the available space)
txt = "We have {:>8} chickens."
print(txt.format(49))
# We have       49 chickens.

# :^
# Center aligns the result (within the available space)
txt = "We have {:^8} chickens."
print(txt.format(49))
# We have       49 chickens.

# :=
# Places the sign to the left most position
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
# The temperature is -      5 degrees celsius.

# :=
# Indicates if the result has a positive or negative sign
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
# The temperature is between -3 and +7 degrees celsius.

# :-
# Indicates only if the number is negative
# (positive numbers are displayed without any sign)
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
# The temperature is between -3 and 7 degrees celsius.

# : 
# Use a space to insert an extra space before positive numbers 
# (and a minus sign before negative numbers)
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
# The temperature is between -3 and  7 degrees celsius.

# :,
# Use a comma as a thousand separator
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
# The universe is 13,800,000,000 years old.

# :_
# Use a underscore as a thousand separator
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
# The universe is 13_800_000_000 years old.

# :b
# Decimal to Binary format
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
# The binary version of 5 is 101

# :c
# Converts the value into the corresponding unicode character

# :d
# Binary to Decimal format
txt = "We have {:d} chickens."
print(txt.format(0b101))
# We have 5 chickens.

# :e
# Scientific format, with a lower case e
txt = "We have {:e} chickens."
print(txt.format(5))
# We have 5.000000e+00 chickens.

# :e
# Scientific format, with an upper case E
txt = "We have {:E} chickens."
print(txt.format(5))
# We have 5.000000E+00 chickens.

# :f
# Use "f" to convert a number into a fixed point number, 
# default with 6 decimals, but use a period followed by a number 
# to specify the number of decimals:
txt = "The price is {:.2f} dollars."
print(txt.format(45))
# The price is 45.00 dollars.
# without the ".2" inside the placeholder, 
# this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45))
# The price is 45.000000 dollars.

# :F
# Fix point number format, in uppercase format 
# (show inf and nan as INF and NAN)
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
# The price is INF dollars.
#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))
# The price is inf dollars.

# :g
# General format

# :G
# General format (using a upper case E for scientific notations)

# :o
# Decimal to Octal format
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
# The octal version of 10 is 12

# :x
# Decimal to Hex format, lower case
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
# The Hexadecimal version of 255 is ff

# :X
# Decimal to Hex format, upper case
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
# The Hexadecimal version of 255 is FF

# :n
# Number format

# :%
# Percentage format
txt = "You scored {:%}"
print(txt.format(0.25))
# You scored 25.000000%
txt = "You scored {:.0%}"
print(txt.format(0.25))
# You scored 25%
















