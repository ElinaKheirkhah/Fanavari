#---------q5.7------------------
'''
Q7
yek liste ghaza darim va menuye resturan hast , in list esmesh hast foods ,
aval be karbar hamash namayesh dade beeshe va done done karbar hey entekhab kone,
har zamani ke karbar nevesht ('order') dige azash esme ghaza porside nashe, 
balke kole list ba estefade az for, besoorate factor behesh namayesh dade beshe
'''

print("=================Q7=======================")
print("==========================================")

foods = [
    "ghormeh sabzi",
    "fesenjan",
    "kebab",
    "zereshk polo",
    "baghali polo",
    "abgoosht",
    "gheymeh",
    "adaspolo"
]

orders = []

print("Menu:")

for food in foods:
    print(food)

while True:

    order = input("ghaza ra entekhab konid: ")

    if order == "order":
        print("Factor:")
        
        for food in orders:
            print(food)

        break

    orders.append(order)
    
    
    
    
    
    
    
    