#---------q4.2------------------
'''
Q2----- Takhfif

az user gheymate kala ro begirid , age gheymate kala bishtar az 1 milion toman bashad
20% takhfif, agar gheymate kala beyne 500,000 ta 1 million toman bashe , 15 darsad takhfif 
agar gheymate kala zire 500 hezar toman bashad, 10% takhfif emal konid va dar nahayat
gheymate bad az takhfif ro b user neshan dahid
'''

print("=================product price====================")
print("==================================================")

product_price = int(input("lotfan gheymate kala ra be toman vared konid: "))

if product_price >= 1000000 :
    discount = 20
    final_price = int(product_price * 0.8)
elif product_price >= 500000 :
    discount = 15
    final_price = int(product_price * 0.85)
elif product_price > 0 :
    discount = 10
    final_price = int(product_price * 0.9)
else:
    print("gheymate vared shode motabar nemibashad.")
    
    
if product_price > 0 :    
    print("darsade takhfif: " , discount , " darsad")    
    print("gheymate nahaei baad az takhfif:" , final_price , "toman")    