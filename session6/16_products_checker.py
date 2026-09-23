"""
16_products_checker

yek list az mahsolat darim ke har mahsool yek dictionary hast mesle 

```python
products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]
```

vorodie tabe yeki products ro begrie va yeki code e mahsol va dar khoroji gheymat ro pas bede


b) vorodi products begire va code e mahsol va name mahsool ro bargardoone 


c) vorodi products begire va code mahsool va khoroji yek tuple begire injori:

(z7,zara bag 500 ,  95)
"""

#a

def products_price (products: list, chosen_product_code: str) -> int :
    '''
    liste mahsoolat va code mahsool ra be onvane voroodi migirad
    gheymat ra khorooji midahad
    '''
    for product in products:
        if product["code"] == chosen_product_code:
            return product["price"]
    
    

products_list=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]

result_1 = products_price(products_list , "z5")
print(result_1)

result_2 = products_price(products_list , "z2")
print(result_2)

#----------------------------------------------------------------------------------
#b

def products_name (products: list, chosen_product_code: str) -> str :
    '''
    liste mahsoolat va code mahsool ra be onvane voroodi migirad
    name ra khorooji midahad
    '''
    for product in products:
        if product["code"] == chosen_product_code:
            return product["name"]
    
    

products_list=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]

result_1 = products_name(products_list , "z5")
print(result_1)

result_2 = products_name(products_list , "z2")
print(result_2)


#----------------------------------------------------------------------------------
#c

def products_info (products: list, chosen_product_code: str) -> tuple :
    '''
    liste mahsoolat va code mahsool ra be onvane voroodi migirad
    code,name,gheymat ra khorooji midahad
    '''
    for product in products:
        if product["code"] == chosen_product_code:
            return (product["code"],product["name"],product["price"])
    
    

products_list=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]

result_1 = products_info(products_list , "z5")
print(result_1)

result_2 = products_info(products_list , "z2")
print(result_2)


