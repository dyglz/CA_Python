# Use find and string slicing to extract the portion 
# of the string after the colon character 
# and then use the float function to convert the extracted
# string into a floating point number.


str = 'X-DSPAM-Confidence:0.8475'

index_colon = str.find(":")
print(index_colon)
new_str = float(str[index_colon + 1:])
print(new_str)
print(type(new_str))