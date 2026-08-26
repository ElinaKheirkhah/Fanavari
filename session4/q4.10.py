#---------q4.10------------------
'''
Q10----Tbadil celsius be fahrenheit

Ma yek dade darim az sensore yek karkhane ke dama ro be Celsius neveshte ast.

yek liste jadid besazid va in list bayaad adade farenheite ghabli ha bashad

formule tabdil : Farenheit = Celsius * 1.8 + 32
'''
print("=================Temperature Conversion====================")
print("===========================================================")

celsius_temps = [22, 25, 17, 16, 26, 13]

fahrenheit_temps = []

for temp in celsius_temps:
    fahrenheit_temps.append(temp * 1.8 + 32)

print(fahrenheit_temps)



