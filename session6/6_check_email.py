"""
6_check_email
yek tabe benvisid ke email ro begire va check kone ke email hast ya na.

chijori mifahmim? bayad fasele beynesh nabashe, bayad @ dashte bashe bayad .com dashte bashe .

agar email bood bayad **True** pass bede agar na **False** pas bede

"""

def check_email (email: str) -> bool :
    '''
    email ra be onvane voroodi migirad
    check mishavad va agar email bashad khorooji True dar gheyre in soorat False midahad
    '''
    
    if " " in email:
        return False
    elif "@" not in email:
        return False
    elif ".com" not in email:
        return False
    else:
        return True
    
result_1 = check_email("elinakheirkhah@gmail.com")
print(result_1)

result_2 = check_email("elina kheirkhah.gmail.com")
print(result_2)   

result_3 = check_email("elina kheirkhah@gmail_com")
print(result_3)  
