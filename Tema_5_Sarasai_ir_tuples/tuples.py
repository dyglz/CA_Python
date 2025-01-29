my_tuple = (1, 2, 3)
colors = "raudona", "žalia", "mėlyna"  # skliaustai neprivalomi
empty_tuple = ()
single_item_tuple = ("elementas",)  # kablelis yra būtinas vieno elemento tuple

print(colors[0])  # Išvestis: raudona
print(my_tuple[1:3])  # Išvestis: (2, 3)

my_tuple = (1, 2, 3)
# TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = 500 