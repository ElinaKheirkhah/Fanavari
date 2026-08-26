#---------q4.8------------------
'''
Q8---- Esm haye kootah

Yek listi az user ha darim, berid va tedade afradi ke dar in list 

andazeye esmeshon kamtar az 5 hast ro beshmorid.


users=['ali','vahid','mohammadreza','hamidreza','gholamreza','amir','sara','maryam']
'''

print("=================count short names====================")
print("======================================================")

users=['ali','vahid','mohammadreza','hamidreza','gholamreza','amir','sara','maryam']

count = 0

for name in users :
    if len(name) < 5:
        count = count + 1
        
print(count)        


