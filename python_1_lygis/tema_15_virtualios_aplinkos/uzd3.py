# Išorinis paketas

# Sukurkite Python modulį ir jame importuokite bet kurį pasirinktą 
# išorinį Python paketą, įrašytą su pip programa. 
# Šiame modulyje sukurkite funkciją, kuri panaudotų įrašyto paketo funkcionalumą. 
# Importuokite šį modulį į main.py testavimo skriptą ir jame 
# panaudokite / ištestuokite savo funkciją.


import jokes

print("Random programming joke:")
print(f"    {jokes.get_random_joke()}\n")

print("Choose a language (e.g., 'en', 'de', 'es'): ")
language = input("Enter the language: ")

print("Choose a category ('neutral', 'chuck', 'all'): ")
category = input("Enter the category: ")

joke = jokes.get_random_joke_multilang(language=language, category=category)
print("Random programming joke:")
print(f"    {joke}")