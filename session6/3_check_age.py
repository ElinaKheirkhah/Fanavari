"""
3_check_age
yek tabe benevsidi ke vorodi sen ro begire agar sen kamtar az 18 bood , 'access denied' khoroji bede, dar gheyre insoorat 'Welcome'
"""

def access (sen: int) -> str :
    '''
    sen ra be onvane voroodi migirad
    agar 18 va bala tar welcome va agar zire 18 access denied khorooji midahad
    '''
    
    if sen >= 18:
        return "Welcome"
    else :
        return "access denied"
    
result_1 = access(17)
print(result_1)

result_2 = access(28)
print(result_2)   


