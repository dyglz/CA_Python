# Bibliotekos knygų skolinimosi patikrinimas

user = input("Ar esate bibliotekos narys? (taip / ne): ").lower()

if user == "taip":
    age = int(input("Įveskite savo amžių: "))
    if age >= 12:
        print("Jūs galite skolintis visas knygas.")
    else:
        adult = input("Ar jus lydi suaugęs asmuo? (taip / ne): ").lower()
        if adult == "taip":
            print("Jūs galite skolintis visas knygas.")
        else:
            print("Jūs galite skolintis tik vaikų knygas.") 
else:
    print("Jūs negalite skolintis jokių knygų.")




# user = input("Ar esate bibliotekos narys? (taip / ne): ").lower()
# if user == "taip":
#     age = int(input("Įveskite savo amžių: "))
#     if age < 12:
#         adult = input("Ar jus lydi suaugęs asmuo? (taip / ne): ").lower()
#         if adult == "ne":
#             print("Jūs galite skolintis tik vaikų knygas.")
#         else:
#             print("Jūs galite skolintis visas knygas.")
#     else:
#         print("Jūs galite skolintis visas knygas.")
# else:
#     print("Jūs negalite skolintis jokių knygų.")


