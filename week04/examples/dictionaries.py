#** what is a dictionary
#key values pairs. 
#Dynamic and can be nested and change

#Syntax
#your_dictionary = { key: value, key: value}

bad_guys = {
  'daredevil': "kingpin", 
  'spiderman': "green goblin",
  'hulk': "abomination"
}


print(bad_guys['daredevil']) # this way we can access to the value of the key. if we put a key that is not in a dictionary would give you a keyerror

#to add a new key with its value

bad_guys['Superman'] = "Lex Lutor" #add to the dictionary 
print(bad_guys)

#to update a value just selecct a key and add the new value

bad_guys['hulk'] = "red Hulk"
print(bad_guys)

# delete a key:value use "del"

del bad_guys['spiderman']

print(bad_guys)

