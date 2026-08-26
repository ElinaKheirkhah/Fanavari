#---------q4.12------------------
'''
Q12---- Gereftane mahsool

ba estefade az halgheye for , yek systemi benevisid , ke 5 bar az karbar esme yek
mahsool begire (masalan zara, nike ,..) va agar toole oon mahsool kamtar az 6 bashad
dakhele yek listi bename sabade_kharid berizad.
'''

print("=================Product selection====================")
print("======================================================")

shopping_basket = []

for i in range(5):
    product = input("name mahsoole khod ra vared konid:")
    
    if len(product) < 6:
        shopping_basket.append(product)

print(shopping_basket)


