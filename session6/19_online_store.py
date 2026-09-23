"""
19_online_store

ma yek foroshgahe koochak darim hamchin chizi 

```python
products = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}
]
```


a ) tabe ei benevisid ke 

```python
find_product(products, code)
```

code mahsool ro begire agar peyda kard , dictionary mahsol ro bargardone, age peyda nakard None pass bede



b) tabe ei benevisid ke yek list bename cart begire :


cart=[]


```python
add_to_cart(products, cart, code)
```

va sepas oon code agar vojod dasht va stock>0 bodo be cart ezafe kone va khoroji cart ro pas bede


c) hamon tabeye (b) ro benevisid ama agar vojod dasht , az products stock ro yedone kam kone va liuste products ro pass bede

d[advanced] ) hamon soale ghabli hast , ama ham be cart ezafe kone , ham products ro ok kone va joftesho pas bede (yani do ta khoroji)
"""

#a

products_list = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}
]

def find_product (products: list, code: str) -> dict or None :
    '''
    liste product ha va code yek product ra be onvene voroodi migirad
    dar soorate vojood dashtan etelaatesh ra khorooji midahad
    '''

    for product in products:
        if product["code"] == code:
            return product
    return None
        

    
result_1 = find_product(products_list,"p2")
print(result_1)

result_2 = find_product(products_list,"p6")
print(result_2)


#------------------------------------------------------------------------------
#b

products_list = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}
]

customer_card = []

def add_to_card (products: list, code: str, card: list) -> list or None :
    '''
    liste product ha va code yek product va cutomer card ra be onvene voroodi migirad
    dar soorate vojood dashtan mahsool va mojood budan be card ezafe shode va an ra khorooji midahad
    '''

    for product in products:
        if product["code"] == code and product["stock"] > 0:
            card.append((code,product["name"]))
            return card
    return None    

    
result_1 = add_to_card(products_list,"p2",customer_card)
print(result_1)

result_2 = add_to_card(products_list,"p4",customer_card)
print(result_2)


#------------------------------------------------------------------------------
#c

products_list = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}
]


def update_stock (products: list, code: str) -> list :
    '''
    liste product ha va code yek product va cutomer card ra be onvene voroodi migirad
    dar soorate vojood dashtan mahsool va mojood budan az stock kam karde va list update shode ra khorooji midahad
    '''

    for product in products:
        if product["code"] == code and product["stock"] > 0:
            product["stock"] = product["stock"] - 1
            return products
    
result_1 = update_stock(products_list,"p2")
print(result_1)


#------------------------------------------------------------------------------
#d

products_list = [
    {"code": "p1", "name": "Keyboard", "price": 50, "stock": 4},
    {"code": "p2", "name": "Mouse", "price": 30, "stock": 7},
    {"code": "p3", "name": "Monitor", "price": 250, "stock": 2},
    {"code": "p4", "name": "Headphone", "price": 80, "stock": 0}
]

customer_card = []

def update_stock_and_add_to_card (products: list, code: str, card: list):
    '''
    liste product ha va code yek product va cutomer card ra be onvene voroodi migirad
    dar soorate vojood dashtan mahsool va mojood budan be card ezafe shode va stock update mishavad va har do list ra khorooji midahad
    '''

    for product in products:
        if product["code"] == code and product["stock"] > 0:
            card.append((code,product["name"]))
            product["stock"] = product["stock"] - 1
            return card , products
    return None    

    
result_1 = update_stock_and_add_to_card(products_list,"p2",customer_card)
print(result_1)

