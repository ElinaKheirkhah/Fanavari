"""
1_calculate_age

Dar in file shoam bayad yek tabe (function) benevisid ke yek vorodi begire (sale tavalod) va sen ro hesb kone va sen ro khoroji bede . 

a ) hamin soal hast ke vorodi fght sale tavalod hast

b ) yek tabe digar besazid do vorodi begire, sale tavalod va tarikh . tarikh agar miladi bod besorate miladi hesab kone agar shamsi bood shamsi hesab kone.  
yani be tabe masalan bedim (1377,'shamsi') ya inke bedim (1999,'miladi')

c) hamoon tabeye (b) ro benevisid , agar tabe fght yek vorodi gereft , be sorate pish farz miladi dar nazar begire


d) tabe ro begone ei benevisid ke fght yek vorodi begire yani fght tarikh , ama khodesh betone tashkhis bede k miladi user dade ya shamsi (hint : range ro check koni )
"""

#baraye handle kardane error ha dar b va c bayad be har kodum ye if else ya elif ezafe shavad ke agar noe tarikh ra eshtebah vared kard error dahad


#a

def calculate_age (sale_tavalod : int):
    '''
    sale tavalod shamsi ra be onvane voroodi migirad 
    sen ra khorooji midahad
    '''    
    sen = 1405 - sale_tavalod
    return sen


result = calculate_age(1381)
print(result)
    

#------------------------------------------------------------------------------
#b

def calculate_age (sale_tavalod: int, noe_tarikh: str):
    '''
    sale tavalod va shamsi/miladi budane an ra be onvane voroodi migirad 
    sen ra khorooji midahad
    '''  
    if noe_tarikh == "shamsi":
        sen = 1405 - sale_tavalod
    elif noe_tarikh == "miladi":
        sen = 2026 - sale_tavalod
    return sen    

result_1 = calculate_age(1381,"shamsi")
print(result_1)

result_2 = calculate_age(2002,"miladi")
print(result_2)


#------------------------------------------------------------------------------
#c

def calculate_age (sale_tavalod: int, noe_tarikh: str = "miladi"):
    '''
    sale tavalod va shamsi/miladi budane an ra be onvane voroodi migirad 
    sen ra khorooji midahad
    agar noe tarikh moshakhas nashavad, pishfarz miladi dar nazar gerefte mishavad
    '''  
    if noe_tarikh == "shamsi":
        sen = 1405 - sale_tavalod
    elif noe_tarikh == "miladi":
        sen = 2026 - sale_tavalod
    return sen    

result_1 = calculate_age(1381,"shamsi")
print(result_1)

result_2 = calculate_age(2002,"miladi")
print(result_2)

result_3 = calculate_age(2002)
print(result_3)


#------------------------------------------------------------------------------
#d

def calculate_age (sale_tavalod : int):
    '''
    sale tavalod shamsi ra be onvane voroodi migirad 
    shamsi ya miladi budane tarikh ra tashkhis midahad
    sen ra khorooji midahad
    '''    
    if sale_tavalod in range(1300, 1405):
        sen = 1405 - sale_tavalod
    elif sale_tavalod in range(1920, 2026):
        sen = 2026 - sale_tavalod
    return sen

#khode sal haei ke toosh hastim ro hesab nakardam chon khorooji sen 0 mishavad va tedade mah ro dar in func hesab nmikonim

result_1 = calculate_age(1381)
print(result_1)

result_2 = calculate_age(2002)
print(result_2)