from array import array

#list are collections of items 

names = ['John', 'Felix', 'Ana', 'Javier'] #mutable

#add items 

names.append("Silvia")

print(names)

print(names[2]) # zero index

#arrays collections of numeric items and the same data type
#must create an array object from array import array

scores = array('d') #name of the variable array
scores.append(97)
scores.append(98)

print(scores)

print(scores[0])

#common operations 

print(len(names)); 

names.insert(0, "Zule") #insert at the beggining. 

#print(names)

names.sort() #alfabetical order, number min to max. Mutates the original list. 

print(names)

#retrieving ranges

family_boys = names[1:3] #start with index 1 and do not include last index. 
family_boys = names[:3]

print(family_boys)


# Dictionaries {key: value} key values pair 

person = {'first': 'John'}

person['last'] = 'Doe' #add something to the dictionary [key] = "value"

print(person)

print(person['first']) # person [index value]

print(person['last']) # person [index value]



