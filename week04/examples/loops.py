#loop trough a collection

names = ['John', 'Felix', 'Ana', 'Javier', "Silvia", "Zule"]

#**For Loop

for item in ['Jonh', 'jane']:
  print(item)

#** loop several times: using range (0,2)

""" for index in range(0,4):
  print(index)
 """
for number in range(0,10):
  if number % 2 == 0:
    print(number)

#** While loop. Commonly you use while loops when you want something change in auto

index = 0
while index < len(names):
  names.sort()
  print(names[index])
  index+=1

  