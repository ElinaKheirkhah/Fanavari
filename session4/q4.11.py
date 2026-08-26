#---------q4.11------------------
'''
Q11----Mohasebe Soode foroshe mahsool
ma yek listi darim az gheymate kharide mahsoolat , va yek listi darim az ghyemate foroshe mahsoolat
shoma bayad soode har kodom az mahsoollat ro dar yek liste jodagane hesab konid

buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]
'''
#--------------rah 1---------------------------

print("=================Product Profit Calculation====================")
print("===============================================================")

buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]

profits = []

for i in range(4):
    profit = sell_prices[i] - buy_prices[i]
    profits.append(profit)
    
print(profits)    

#--------------rah 2---------------------------

print("=================Product Profit Calculation====================")
print("===============================================================")

buy_prices = [100, 200, 150, 400]
sell_prices = [130, 250, 190, 500]

profits = []

for i in range(len(buy_prices)):
    profit = sell_prices[i] - buy_prices[i]
    profits.append(profit)
    
print(profits)    


