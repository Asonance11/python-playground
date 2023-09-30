# string slicing

full_name = "John Smith"
first_name = full_name[:4]
last_name = full_name[5:] 

print(first_name)
print(last_name)

# string slicing with negative numbers

website1 = "http://google.com"
website2 = "http://whoami.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])