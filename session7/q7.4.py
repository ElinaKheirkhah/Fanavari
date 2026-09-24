"""
q7.4

yek tabe benevisid ke yek listi az tuple ha dare o ino be onvane vorodi migirie

sales = [
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
]


- yek tabe benvisid  ke khoroji yek dictionary bede ke har fard yek key hast va jolosh jame kharidesho zade
- yek tabe benevisid ke khorojish yek dictionary bede ke key ha esme mahsolat bashe va jolosh tedde foroshe mahsolat
- yek tabe benevsiid ke khoroji ye adad bede ke majhmooe daramade foroshgah hast

"""

sales_list = [
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
]

#-----------------------------------1--------------------------------------

def make_sales_information (sales: list) -> dict :
    sales_information = {}

    for name, product, price in sales:
        if name in sales_information:
            sales_information[name] = sales_information[name] + price
        else:
            sales_information[name] = price

    return sales_information
        

    
result_1 = make_sales_information(sales_list)
print(result_1)

#-----------------------------------2--------------------------------------

def count_product_sales (sales: list) -> dict :
    product_sales = {}

    for name, product, price in sales:
        if product in product_sales:
            product_sales[product] = product_sales[product] + 1
        else:
            product_sales[product] = 1

    return product_sales
        

    
result_2 = count_product_sales(sales_list)
print(result_2)

#-----------------------------------3--------------------------------------

def sum_sales_amount (products: list) -> int :
    sum_amount = 0
    for name,product,price in products:
       sum_amount = sum_amount + price 
        
    return sum_amount   
    
result_3 = sum_sales_amount(sales_list)
print(result_3)




