#---------q5.1------------------
'''
Q1
Yek listi az nomreye daneshjooha darim , varede in list beshe va daneshjoohaye failed va pass ro dar biare
'''

print("=================Q1=======================")
print("================scores====================")

scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]

failed = []
passed = []

for score in scores:
    if score >= 10 :
        passed.append(score)
    else:
        failed.append(score)
        
print("passed:")
print(passed)

print("failed:")
print(failed)        
        