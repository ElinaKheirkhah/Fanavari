#---------q4.6------------------
'''
Q6----Mohasebe majmooei gheymat ha
Yek listi az esm ha darim ,ba estefade az halgheye for , majmooe toole tamame
esm haro hesab konid.

names = ["Ali", "Sara", "Reza", "Mina"]
'''
#----------------rah 1---------------------

print("=================names length====================")
print("================================================")

names = ["Ali", "Sara", "Reza", "Mina"]

for name in names:
   print(len(name))
   
#----------------rah 2---------------------

print("=================names length====================")
print("================================================")

names = ["Ali", "Sara", "Reza", "Mina"]

total_length = 0

for name in names:
    total_length = total_length + len(name)

print(total_length)


