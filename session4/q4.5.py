#---------q4.5------------------
'''
Q5----Adade fard

In mesal az se bakhsh a,b,c tashkil shode
Adade farde beyne 15 ta 115 ro  a)chap konid b)dakhele yek list berizid c)beshmorid
'''

print("=================odd numbers====================")
print("================================================")

odd_numbers_list = []

count = 0

for odd_number in range(15,116,2):
    print(odd_number)
    odd_numbers_list.append(odd_number)
    count = count + 1
    
print(odd_numbers_list)

print(count)    