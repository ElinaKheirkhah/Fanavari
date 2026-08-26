#---------q4.9------------------
'''
Q9----Afzayeshe gheymat

yek listi darim az gheymate mahsol haye yek foroshgah , yek liste jadid besazid
ke tamame gheymate mahsoolat ro 10% afzayesh dahad.

'''

print("=================increase product price====================")
print("===========================================================")

raw_prices = [200000, 650000, 1350000, 3670000, 5620000]

increased_prices = []

for price in raw_prices:
    increased_prices.append(int(price * 1.1))

print(increased_prices)

