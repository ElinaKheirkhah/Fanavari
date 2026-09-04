#---------q5.3------------------
'''
Q3
az karbar hey esme mahsool begire va hey berize tooye yek listi bename products 
va inkaro onghadr edame bede ke moshtari benevise 'exit' va badesh kole list ro neshon bede
'''

print("=================Q3=======================")
print("==========================================")

products = []

while True:
    product = input("name mahsool ra vared konid: ")

    if product == "exit":
        print(products)
        break

    products.append(product)
    

