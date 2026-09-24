"""
q7.1

yek dictionary aZ mahsoolat darim 

products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}


Chandin tabe benevisid ke in dictionary ro besoorate vorodi begire
va


- bishtarin gheymat ro pas bede
- esme mahsoli ke bishtarin gheymat ro dare pas bede
- hamin 2 taro baraye **kamtarin** ham anjam dahid
- jame kole mahsoolat ro pas bede
- miangine kole mahsolat ro pas bede

"""

products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}

#-----------------------------------1--------------------------------------

def maximum_price (products: dict) -> int :
    return max(products.values())
        
        
result_1 = maximum_price(products)
print(result_1)

#-----------------------------------2--------------------------------------

def maximum_price_product (products: dict) -> str :
    maximum_price = max(products.values())
    for product_name,price in products.items():
        if price == maximum_price:
            return product_name
        
        
result_2 = maximum_price_product(products)
print(result_2)

#-----------------------------------3--------------------------------------

def minimum_price (products: dict) -> int :
    return min(products.values())
        
        
result_3 = minimum_price(products)
print(result_3)

#-----------------------------------4--------------------------------------

def minimum_price_product (products: dict) -> str :
    minimum_price = min(products.values())
    for product_name,price in products.items():
        if price == minimum_price:
            return product_name
        
        
result_4 = minimum_price_product(products)
print(result_4)

#-----------------------------------5--------------------------------------

def sum_products_price (products: dict) -> int :
    return sum(products.values())
        
        
result_5 = sum_products_price(products)
print(result_5)

#-----------------------------------6--------------------------------------

def average_products_price (products: dict) -> float :
    return sum(products.values()) / len(products)
        
        
result_6 = average_products_price(products)
print(result_6)






















