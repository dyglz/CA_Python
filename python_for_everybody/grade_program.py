# Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, 
# print a grade using the following table

def computegrade(input_score):
    if input_score >= 0.9:
        print(str("Grade A"))
    elif input_score >= 0.8:
        print(str("Grade B"))
    elif input_score >= 0.7:
        print(str("Grade C"))
    elif input_score >= 0.6:
        print(str("Grade D"))
    else:
        print(str("Grade F"))

try:
    input_score = float(input("Enter score between [0.00 - 1.00]: "))
    if 0.00 <= input_score <= 1.00:
        computegrade(input_score)
    else:
        print("Error. Input out of range [0.00 - 1.00]!")
except ValueError: 
    print("Error. Input has to be a number!")