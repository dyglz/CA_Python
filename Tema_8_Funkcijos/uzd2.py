# El. pašto tikrinimas

# Create a function that validates an email address based on user input
# Ensure the email address contains: 
# exactly one "@" symbol
# at least one "." in the domain part
# domain suffix (last part) is at least 2 characters long


def email_validation(user_email):
    at_sign_count = user_email.count("@")
    if at_sign_count != 1:
        return False
    elif at_sign_count == 1:
        email_parts = user_email.split("@")
        domain = email_parts[1]
        dot_sign_count = domain.count(".")
        if dot_sign_count < 1:
            return False
        elif dot_sign_count >= 1:
            last_dot_sign = domain.rfind(".")
            if len(domain) - int(last_dot_sign + 1) >= 2:
                return True
            else:
                return False
            

while True:

    user_input = input("Enter an email address or 'quit': ")
    if user_input.lower() == 'quit':
        break
    if user_input == "":
        print("Nothing entered!")
        continue
    
    user_email = user_input.replace(" ", "")
    if email_validation(user_email):
        print("Email is valid.")
    else:
        print("Email is not valid.")

    
    

# Enter an email address or 'quit': @.as
# [, .as] | dot sign found: 1
# Email is valid. (last dot ok)
# 
# add len() to ensure email contains at least x characters?
# what to do with the spaces in the input? invalid input or remove?
