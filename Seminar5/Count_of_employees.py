count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]

def sum_count(sp):
    total = 0
    for item in sp:
        # или if str(type(item)) == "<class 'list'>":
        # или if type(item) == type([]):
        if isinstance(item, list):
            total = total + sum_count(item)
        else: total += item
    return total
print(count_all)
print(type(count_all))
print(sum_count(count_all))




# count_new_york = tuple(count_new_york)
# a, b, c = count_new_york
# sum = count_angola + count_new_york

# def count_employees(count_all) -> int:
#     for i in range(len.(count_all))

 