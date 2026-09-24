"""
q7.2

yek dictionary az mahsolato mojodi ro darid , in ro be soorate vorodi yek tabe migire
va do khoroji mide, do ta list mide ke yeki list esme mahsolati hast ke
mojodi darand , yeki list mahsolati ke mojodi nadaand

inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}

"""

inventory_list = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}


def check_stock (inventory: dict) :
    available_products = []
    out_of_stock_products = []
    
    for product in inventory:
        if inventory[product] > 0:
            available_products.append((product, inventory[product]))
        else:
            out_of_stock_products.append((product, inventory[product]))
    return available_products , out_of_stock_products
        

    
result = check_stock(inventory_list)
print(result)




