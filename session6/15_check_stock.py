"""
15_check_stock

yek tabe benevisid ke do vorid begire, yeki dictionary az mahsoolat va yeki esme mahsool

masalan

```python
products = {
    "iphone": 5,
    "macbook": 2,
    "airpods": 0
}
```

va 

```bsh
iphone
```

va dar khoroji agar mojodi 0 nabashe True bede, agar na False bede
"""

def check_stock (products: dict, chosen_product: str) -> bool :
    '''
    liste mahsoolat ra be onvane voroodi migirad
    dar soorate dashtane mojoodi True va naashtane mojoodi False khorooji midahad
    '''
    for product,stock in products.items():
        if product == chosen_product :
            if stock == 0:
                return False
            else:
                 return True
    
    
products_list = {
    "iphone": 5,
    "macbook": 2,
    "airpods": 0,
    "apple_watch":12
}

result_1 = check_stock(products_list,"airpods")
print(result_1)

result_2 = check_stock(products_list,"iphone")
print(result_2)






