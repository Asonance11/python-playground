# Sets

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'fork'}

utensils.add('napkin')
utensils.remove('fork')
utensils.clear()
utensils.update(dishes)
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

for i in dinner_table:
    print(i)