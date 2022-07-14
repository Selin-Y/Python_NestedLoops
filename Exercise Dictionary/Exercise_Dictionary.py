#### Exercise Dictionary

# 1.Question
# Print dictionary value, key and item values to the screen respectively.

elements = {"hydrogen": 1, "oxygen": 8, "carbon": 6, "helium": 2}

print(elements.keys())
for i in elements.values():
    print(i, end=" ")

print()
for item in elements.items():
    print(item)

# 2.Question
# Add the character length of the key values to the value values of the provinces whose population information is written incorrectly.

population = {
    "İstanbul":10,
    "Ankara":9,
    "İzmir":8
}
print(population)

# for key, value in population.items():
#    population[key] = value + len(key)

for item in population.items():
    population[item[0]] = item[1] + len(item[0])

print(population)

# 3.Question

# In the dictionary consisting of the names of the players of the friends series,
# combine the name and surname with _,
# then convert all the letters to lowercase and update the value values with the update method.
# Use functions when manipulating value values.
# Joey Tribbiani -> joey_tribbiani

def set_value(name):
    return name.replace(" ", "_").lower()

friends = {
    "joey":"Joey Tribbiani",
    "rachel":"Rachel Green",
    "monica":"Monica Geller",
    "phoebe":"Phoebe Buffay",
    "chandler":"Chandler Bing",
    "ross":"Ross Geller"
}

for key, value in friends.items():
    friends.update({key:set_value(value)})

print(friends)

# 4.Question

# Press the value of item1 key to the screen.
my_dict = {
    "Python":{
        "weeks":{
            "data_structures":"list",
            "dictionary": {
                "item1":1, "item2":2
                    }
                }
            }
        }

print(my_dict["Python"]["weeks"]["dictionary"]["item1"])

# 5.Question

# Merging two dictionary.
my_dict1 = {"Merve":20, "Emre":22, "Burak":29}
my_dict2 = {"Burak":32, "Asena":19, "Bircan":26}

new_dict = {**my_dict1, **my_dict2}
print(new_dict)

# 6.Question

# Merging two lists and create a dictionary.

key_list = ["Adana", "İstanbul", "İzmir"]
value_list = ["01", "34", "35"]

cities = dict()
for i in range(len(key_list)):
    cities[key_list[i]] = value_list[i]

print(cities)

# 7.Question

# Merging two list with zip and create a dictionary.
key_list = ["Adana", "İstanbul", "İzmir"]
value_list = ["01", "34", "35"]

# zip(keys, values)
my_dict = dict(zip(key_list, value_list))
print(my_dict)

# 8.Question

# The list contains the key values that we want to extract.
# Add check to avoid error if there is no key value
# Remove those key values from the dictionary according to the list elements.

my_info = {"name":"Belly", "surname":"Laugh", "title":"Engineer", "year":2022}
my_list = ["surname", "year", "job"]
print(my_info)

for i in my_list:
    if i in my_info.keys():
        del my_info[i]
        #my_info.pop(i)

print(my_info)
