#Optional 2

'''
tabe ei bename available_products benevisid ke dictionary mahsoolat ro daryaft konad , yani
vorodish yek dictioanry bashe mesle :

products = {
    "laptop": 3,
    "phone": 0,
    "tablet": 5,
    "mouse": 0,
    "keyboard": 2
}

va sepas , faghat name mahsolati ke mojodi anha bish az sefr hast ro ba estefade az yield yeki yeki tolid konad (yani ye khoroji)

sepas yek generator besazido mahsolate mojod ro ba next() done done daryaft koni
'''

products = {
    "laptop": 3,
    "phone": 0,
    "tablet": 5,
    "mouse": 0,
    "keyboard": 2
}

def available_products (products_dict):
    for product,stock in products_dict.items():
        #print(f"{product} - {stock}")
        if stock > 0:
          #print(f"{product} - {stock}")  
          yield product




check_available_products = available_products(products)
next(check_available_products)

next(check_available_products)

next(check_available_products)

