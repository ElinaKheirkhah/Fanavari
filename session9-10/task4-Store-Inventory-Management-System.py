#===============================================
#=====================Task 4====================
#===============================================
#======Store Inventory Management System========
#===============================================


class Product:
    def __init__(self,name,price,quantity,category):
        if type(price) is not int:
            raise TypeError("Gheymat bayad adad bashad.")

        if price < 0:
            raise ValueError("Gheymat nemitavanad manfi bashad.")
    
        if type(quantity) is not int:
            raise TypeError("Tedad bayad adad sahih bashad.")
    
        if quantity < 0:
            raise ValueError("Mojoodi nemitavanad manfi bashad.")
            
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity
        self.product_category = category
        
    
    def sell(self, sell_count: int):
        if type(sell_count) is not int:
            print("Tedad bayad adad sahih bashad.")
            return
    
        if sell_count <= 0:
            print("tedade foroosh bayad bishtar az sefr bashad.")
            return
    
        elif sell_count <= self.product_quantity:
            self.product_quantity -= sell_count
            print("tedade mahsool az mojoodi kam shod.")
    
        else:
            print("mojoodi baraye foroosh kafi nemibashad.")

    
    def add_stock(self,add_stock_count: int):
       if type(add_stock_count) is not int:
           print("Tedad bayad adad sahih bashad.")
           return
        
       if add_stock_count <= 0:
           print("tedade afzayeshe mojoodi bayad bishtar az sefr bashad.")
           return
   
       else:
           self.product_quantity += add_stock_count
           print("be tedade mojoodi ezafe shod.")

    
    def update_price(self, new_product_price):
        if type(new_product_price) is not int:
            print("gheymat bayad adad sahih bashad.")
            return
        
        if new_product_price < 0:
            print("gheymate mahsool nmitavanad manfi bashad.")
            return
    
        else:
            self.product_price = new_product_price
            print("gheymate mahsool update shod.")
    
    def apply_discount(self, discount_percent: int):
        if type(discount_percent) is not int:
            print("darsade takhfif bayad adad sahih bashad.")
            return
        
        if discount_percent < 0:
            print("darsade takhfif nmitvanad manfi bashad.")
            return
        elif discount_percent > 100:
            print("darsade takhfif bayad beyne 0 ta 100 bashad.")
            return
        else:
            price_after_discount = int(self.product_price - self.product_price * discount_percent/100)
            return price_after_discount
    
    def total_value(self):
        return self.product_quantity * self.product_price
    
    def __str__(self):
        return (
            "-------------\n"
            "Product Data:\n"
            f"Name: {self.product_name}\n"
            f"Price: {self.product_price}\n"
            f"Quantity: {self.product_quantity}\n"
            f"Category: {self.product_category}\n"
            "-------------"
        )



#---------------------test------------------------       

product_1 = Product("LV", 3500000, 5, "bag")

print(product_1)


product_1.sell(2)
product_1.sell(0)
product_1.sell(-4)
product_1.sell(5)
product_1.sell(3)
product_1.sell("test")


product_1.add_stock(7)
product_1.add_stock(0)
product_1.add_stock(-9)

product_1.update_price(2700000)
product_1.update_price(-2700000)

product_1.apply_discount(50)
product_1.apply_discount(-5)
product_1.apply_discount(120)

product_1.total_value()

#----------------------challenge----------------------

product_1 = Product("backpack", 3500000, 5, "bag")
product_2 = Product("sneakers", 7600000, 7, "shoes")
product_3 = Product("coat", 4800000, 3, "clothes")

products_list = [product_1,product_2,product_3]

#print(products_list)
max_total_value = products_list[0].total_value()
max_total_value_name = products_list[0].product_name
                                     
for product in products_list:
    if product.total_value() > max_total_value:
        max_total_value = product.total_value()
        max_total_value_name = product.product_name
print (f"mahsool ba balatarin arzesh {max_total_value_name} ba {max_total_value} mibashad.")    






















