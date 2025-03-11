#  Surikiuotas knygų sąrašas

# Parašykite funkciją, kuri priima žodynų sąrašą, reprezentuojantį knygas, 
# kuriame kiekviena knyga turi raktus „title“ (pavadinimas) 
# ir „author“ (autorius), ir grąžina sąrašą, 
# surikiuotą pagal autoriaus vardą.

def sorted_books(books_list: list[dict[str, str]]) -> list[dict[str, str]]:
    return sorted(books_list, key = lambda book: book['author'])


books_list = []
book_count = int(input("Enter number of books: "))
for i in range(book_count):
    title = input("Enter book title:")
    author = input("Enter author name: ")
    books_list.append({"title": title, "author": author})

sorted_books_list = sorted_books(books_list)
print(f"Sorted books: {sorted_books_list}")