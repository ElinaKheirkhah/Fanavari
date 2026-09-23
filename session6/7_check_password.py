"""
7_check_password

a) yek tabe benevisid ke password ro begire va bayad hadeaghal 8 character , hadeaghal yek adad, hadeaghal yek harf dakehelsh bashe.
agar bood faghat print kone 'password sabt shod' ,agar nabood print kone 'password kamel nist'


b) hamon tabe ro benevisid ama agar password dorost bod chizi print nakone balke khorojhi bede True , dar gheyre insorat khoroji bede False

c) Yek tabe besazid bename check_password_strength ke ghodrate password ro besanje yani dar khoroji yek adad bede beyne 1 ta 4 . 

- 4: agar ham bala 8 ragham bod va ham harf dahst ham adad , ham bozorg ham kochak 

- 3 : agar ham bala 8 ragham bod ham harf dahst ham adad dasht 

- 2 : agar bala 8 raghamm bood

- 1 : agar paeine 8 bood 1 bede

"""

#farz ro bar in migirim ke karbar faghat az adad va horoof estefade konad va az alamat ha mesle ! @# $ estefade nakonad
#chon in shekli bakhsh haei az logic taghir mikonad

#a

def check_password (password: str) :
    '''
    password ra be onvane voroodi migirad
    check mikonad ke bishtar az 8 char va tarkibi az adad o horoof bashad
    '''
    
    if password.isdigit() or password.isalpha() or len(password)<8 :
        print("password kamel nist")
    else:
        print("password sabt shod")
    
check_password("elinaKh12")

check_password("elinaaakh")

check_password("5257436465")

check_password("ss36465")

#---------------------------------------------------------------------------------
#b

def check_password (password: str) -> bool :
    '''
    password ra be onvane voroodi migirad
    check mikonad ke bishtar az 8 char va tarkibi az adad o horoof bashad
    va khorooji bool midahad
    '''
    
    if password.isdigit() or password.isalpha() or len(password)<8 :
        return False
    else:
        return True
    
result_1 = check_password("elinaKh12")
print(result_1)

result_2 = check_password("elinaaakh")
print(result_2)   

result_3 = check_password("ss36465")
print(result_3) 


#---------------------------------------------------------------------------------
#c

def check_password_strength  (password: str) -> int :
    '''
    password ra be onvane voroodi migirad
    sakhti password ra check mikonad va beyne 1 ta 4 khorooji midahad
    '''
    
    if not password.isdigit() and not password.isalpha() and not password.isupper() and not password.islower() and len(password)>8 :
        return 4
    elif not password.isdigit() and not password.isalpha() and len(password)>8 :
        return 3
    elif len(password)>8 :
        return 2
    elif len(password)<8 :
        return 1


result_1 = check_password_strength("elinaKh12")
print(result_1)

result_2 = check_password_strength("elinaaakh")
print(result_2)   

result_3 = check_password_strength("ss36465")
print(result_3) 


#rahe 2

def check_password_strength  (password: str) -> int :
    '''
    password ra be onvane voroodi migirad
    sakhti password ra check mikonad va beyne 1 ta 4 khorooji midahad
    '''
    if len(password) > 8 :
        
        if not password.isdigit() and not password.isalpha():
            if not password.isupper() and not password.islower():
                return 4
            else:
                return 3
        else :
            return 2
    else :
        return 1

result_1 = check_password_strength("elinaKh12")
print(result_1)

result_2 = check_password_strength("elinaaakh")
print(result_2)   

result_3 = check_password_strength("ss36465")
print(result_3)




















