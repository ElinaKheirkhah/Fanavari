"""
20_bank_system

in sakht tarin soalemon hast , fekr konid ma etealat hesab ro darim dar jaei bename accounts.

```bsh

 = [
    {
        "username": "ali",
        "password": "1234",
        "balance": 5000,
        "transactions": []
    },
    {
        "username": "sara",
        "password": "5678",
        "balance": 8000,
        "transactions": []
    }
]
```

a) yek tabe login benevisid , accounts va username va password, bere too account begarde agar username nabod None aps bede, agar bod check kone udsername va password  motabeghat dare agar dasht True pass bede dar gheyre insoorat False pas bede

```python
login(accounts, username, password)
```

b1) tabeye withdraw ro benevisid , account ro bede va hesab , va biad balance 

masalan vorodi ine 

```python
accounts[0]
```

va hamchnin yek mablagh mesle 2000 

bad biad az oon dictioanry az balancd , oon mablagh ro kam kone  (Bardasht) va dictionary update shode ro bargardone


b2) hamon tabeye b1 ro benevisid , ama na tanha oon mablagh ro kam az balance kam kone, balke oon mablagh ro b liste transaction ham ezafe kone .



c1) tabeye deposit benevisid , hamon tabeye (b) ama oon mablagh ro behesh ezafe kone (variz)


c2) na tanha oon mablagh ro be balance ezafe kone , balke oon mbalgh ro be list etransaction ham ezafe kone.


d) yek tabe dashte bashim ke biad baraye ma account ro agar behesh bedim , transaction haro neshon bede


```python
show_transactions(account)
```



e [advance] ) yek tabe besazid baraye transfer money


```python
transfer(accounts, sender_username, receiver_username, amount)
```

masalan shoma bedi yek hamchin chizi

```python

transfer(accounts, "ali", "sara", 1000)
```

baayd biayd az balance ali 1000 kam konid b balance sara 1000 ezafe konid, tooye transaction ha ham benevisid va dar nahayat liste accounts ro bargardoonid.



f) yek tabe benevisid bename get_balance ke do vorodi migire yeki accoun yeki currency.

besoorate by default currency bashe USD , va har account ke dadan bere va gheymato bargardone.

agar currency ro kardan 'RIAL' oon adad ro zarb dar gheymate dola kone . masalan * 2500000 kone


"""

accounts_list = [
    {
        "username": "ali",
        "password": "1234",
        "balance": 5000,
        "transactions": []
    },
    {
        "username": "sara",
        "password": "5678",
        "balance": 8000,
        "transactions": []
    }
]


#a

def login(accounts: list, username: str, password: str) -> bool or None :
    '''
    accounts va username va password ra migirad va account ra barresi mikonad agar username peyda shavad password ra check karde 
    va True ya False barmigardad, dar gheire in soorat None mide
    '''
    
    for account in accounts:
        if account["username"] == username:
            if account["password"] == password:
                return True
            else:
                return False
    return None

    
result_1 = login(accounts_list,"sara","5678")
print(result_1)

result_2 = login(accounts_list,"ali","1680")
print(result_2)

result_3 = login(accounts_list,"milad","5678")
print(result_3)

#-------------------------------------------------------------------------------
#b1

def withdraw(accounts: list, username: str, amount: int) -> list :
    '''
    accounts va username va amount ra migirad va amount ra az balance account kam mikonad va accounts update shode ra barmigardad
    '''
    
    for account in accounts:
        if account["username"] == username:
            account["balance"] = account["balance"] - amount
    return accounts

    
result_4 = withdraw(accounts_list,"sara",1000)
print(result_4)


#-------------------------------------------------------------------------------
#b2

def withdraw_update(accounts: list, username: str, amount: int) -> list :
    '''
    amount ra az balance account kam mikonad va hamzaman transactione withdraw ra sabt mikonad va accounts update shode ra barmigardad
    '''
    
    for account in accounts:
        if account["username"] == username:
            account["balance"] = account["balance"] - amount
            account["transactions"].append(("withdraw",amount))
    return accounts

    
result_5 = withdraw_update(accounts_list,"sara",1800)
print(result_5)

#-------------------------------------------------------------------------------
#c1

def deposit(accounts: list, username: str, amount: int) -> list :
    '''
    accounts va username va amount ra migirad va amount ra be balance account ezafe mikonad va accounts update shode ra barmigardad
    '''
    
    for account in accounts:
        if account["username"] == username:
            account["balance"] = account["balance"] + amount
    return accounts

    
result_6 = deposit(accounts_list,"sara",3000)
print(result_6)


#-------------------------------------------------------------------------------
#c2

def deposit_update(accounts: list, username: str, amount: int) -> list :
    '''
    amount ra be balance account ezafe mikonad va hamzaman transaction e deposit ra sabt mikonad va accounts update shode ra barmigardad
    '''
    
    for account in accounts:
        if account["username"] == username:
            account["balance"] = account["balance"] + amount
            account["transactions"].append(("deposit",amount))
    return accounts

    
result_7 = deposit_update(accounts_list,"ali",1500)
print(result_7)


#-------------------------------------------------------------------------------
#d

def show_transactions(accounts: list, username: str) -> list :
    '''
    account ra migirad va list e transaction haye an account ra barmigardad
    '''
    
    for account in accounts:
        if account["username"] == username:
            return account["transactions"]

    
result_8 = show_transactions(accounts_list,"ali")
print(result_8)


#-------------------------------------------------------------------------------
#e
#dar halate pishrafte tar bayad mojoodi avalie karbar ro baraye variz check konm
def transfer(accounts: list, sender_username: str, receiver_username: str, amount: int) -> list :
    '''
    accounts va username ferestande va girande va amount ra migirad amount ra az hesabe ferestande kam 
    va be hesabe girande ezafe karde va transaction ha ra sabt mikonad
    '''
    
    for account in accounts:
        if account["username"] == sender_username:
           account["balance"] = account["balance"] - amount 
           account["transactions"].append(("variz be ", receiver_username ,amount))
        elif account["username"] == receiver_username:
             account["balance"] = account["balance"] + amount 
             account["transactions"].append(("variz az ", sender_username ,amount))
    return accounts         
    
result_9 = transfer(accounts_list,"ali","sara",2500)
print(result_9)

result_10 = transfer(accounts_list,"ali","sara",1000)
print(result_10)


#-------------------------------------------------------------------------------
#f
def get_balance(accounts: list, username: str, currency: str = "USD") -> list :
    '''
    account va currency ra migirad va balance account ra bar asas currencye entekhabi barmigardad agar currency RIAL bashad
    balance ra dar 250000 zarb mikonad
    '''
    
    for account in accounts:
        if account["username"] == username:
            if currency == "USD":
                return account["balance"]
            elif currency == "RIAL":
                return account["balance"] * 250000
    return None        
    
result_11 = get_balance(accounts_list,"ali","RIAL")
print(result_11)

result_12 = get_balance(accounts_list,"sara")
print(result_12)





















