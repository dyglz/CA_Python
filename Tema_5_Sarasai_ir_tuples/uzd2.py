# Pirkinių sąrašas

shopping_list = ['pienas', 'kiaušiniai', 'duona', 'sviestas']
print(shopping_list)
print(shopping_list[0])

index_wrong_item = shopping_list.index('duona')
shopping_list.pop(index_wrong_item)
shopping_list.insert(index_wrong_item, 'bananas')
# shopping_list[shopping_list.index("duona")] = "bananas"
print(shopping_list)

shopping_list.insert(0, 'obuolys')
print(shopping_list)

shopping_list.append('miltai')
shopping_list.append('cukrus')
# shopping_list.extend(["miltai", "cukrus"])
print(shopping_list)

print(shopping_list[2:4])