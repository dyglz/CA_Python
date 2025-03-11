# Atsitiktiniai žodžiai

# Naudodami venv arba pipenv, įdiekite Random-Word paketą ir sukurkite 
# nedidelį Python skriptą, kuris atspausdintų 5 atsitiktinius žodžius 
# visomis didžiosiomis raidėmis ir surikiuotus abėcėlės tvarka.


from random_word import RandomWords
r = RandomWords()

# for i in range(5):
#     random_word = r.get_random_word()
#     capitalized = random_word.upper()
#     print(capitalized)


random_words = [r.get_random_word() for i in range(5)]
capitalized_words = [word.upper() for word in random_words]
sorted_words = sorted(capitalized_words)

for word in sorted_words:
    print(word) 