names = ['Shivani', 'Jason', 'Yusef', 'Sakura']
greeted_names = map(lambda x: 'Hi ' + x, names)

# This prints something similar to: <map object at 0x10ed93cc0>
print(greeted_names)
# Recall, that map returns an iterator 

# We can print all names in a for loop
for name in greeted_names:
    print(name)

numbers = [13, 4, 18, 35]
div_by_5 = filter(lambda num: num % 5 == 0, numbers)

# We can convert the iterator into a list
print(list(div_by_5)) # [35]