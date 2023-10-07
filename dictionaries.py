# Dictionary

capitals = {'USA': 'Washington DC', 'Nigeria': 'Abuja', 'Japan': 'Tokyo', 'China': 'Beijing'}

print(capitals)
print(capitals['Nigeria'])
print(capitals.get('Germany'))

capitals.update({'Germany': 'Berlin'})
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.pop('China')
capitals.clear()

for key, value in capitals.items():
    print(key, value)
