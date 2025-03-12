# operations with lists

def add_to_list(lst: list, item) -> list:
    lst.append(item)
    return lst

def remove_from_list(lst: list, item) -> list:
    if item in lst:
        lst.remove(item)
    return lst

def count_items(lst: list) -> int:
    return len(lst)

def reverse_list(lst: list) -> list:
    return lst[::-1]
