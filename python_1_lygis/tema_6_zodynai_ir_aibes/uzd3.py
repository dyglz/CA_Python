# Žodžių žodynas

definitions = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",
    }

while True:
    user_keyword = input("Please, enter a word which you are looking for (or 'end'): ")
    if user_keyword.lower() == 'end':
        print("End of the program")
        break   
    elif user_keyword in definitions:
        print(f"'{user_keyword}' meaning: {definitions[user_keyword]}")
#       print(f"Žodžio {user_input} reikšmė: {dictionary.get(user_input)}")
        break
    else:
        print("This word does not exist in the dictionary.")


