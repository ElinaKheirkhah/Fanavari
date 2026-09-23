"""
18_user_management

yek systeme sade modiriat karbar msiazim

ma yek listi az user ha(dictionary) darim ke etelaateshon hastand , in list ro mitonid ba estefade az gpt hata boizorgtaresh ham konid

```python
users = [
    {
        "username": "ali",
        "age": 25,
        "city": "Tehran",
        "active": True
    },
    {
        "username": "sara",
        "age": 17,
        "city": "Tabriz",
        "active": True
    }
]
```


a) yek tabe besazid bename 

```python
add_user(users, username, age, city)
```

in biad hamon user ro dictionary kone va be oon products ezafe kone va active ham pish farz True hast , va badesh liste user ha update shode ro bargardoone



b) Hala yek tabe besazid bename

```python
find_user(users, username)
```

ke biad tooye oon list begarde oon user ro peyda kone agar vojod nadasht None pas bede, agarvojod dasht dictionary marboot be user ro pas bede

c) yek tabe beszid ke check kone oon user ejaze dastresi dare ya na

```python
check_access(users, username)
```

baayd vase oon username check kone agar age>=18 va active bashe true pas bede, agar na False pas bede


d) yek tabe benvisid

```python
get_adult_users(users)
```

va faghat karbar haye balaye 18 sale ro dar yek list gharar bede va oon list ro pas bede.




tamame in 4 tabe ro dakheel file bename 18_user_management.py benevisid.

"""

#a

users_list = [
    {
        "username": "ali",
        "age": 25,
        "city": "Tehran",
        "active": True
    },
    {
        "username": "sara",
        "age": 17,
        "city": "Tabriz",
        "active": True
    },
    {
        "username": "milad",
        "age": 35,
        "city": "Tehran",
        "active": False
    }
]

def add_user(users: list, username: str, age: int, city: str, active: bool = True) -> list :
    '''
    liste user ha va etelaate yek user jadid ra be onvene voroodi migirad
    list user haye update shode ra khorooji midahad
    '''
    
    users.append({"username": username,"age": age,"city": city,"active": active})
    return users     

    
result_1 = add_user(users_list,"Elina",25,"Tehran")
print(result_1)

#--------------------------------------------------------------------------------
#b

users_list = [
    {
        "username": "ali",
        "age": 25,
        "city": "Tehran",
        "active": True
    },
    {
        "username": "sara",
        "age": 17,
        "city": "Tabriz",
        "active": True
    },
    {
        "username": "milad",
        "age": 35,
        "city": "Tehran",
        "active": False
    }
]

def find_user(users: list, username: str) -> dict or None:
    '''
    liste user ha va username yek user ra be onvene voroodi migirad
    dar soorate vojood dashtan etelaatash ra khorooji midiahad
    '''
    for user in users:
        if user["username"] == username:
            return user
    return None
      

    
result_1 = find_user(users_list,"milad")
print(result_1)

result_2 = find_user(users_list,"amin")
print(result_2)



#--------------------------------------------------------------------------------
#c

users_list = [
    {
        "username": "ali",
        "age": 25,
        "city": "Tehran",
        "active": True
    },
    {
        "username": "sara",
        "age": 17,
        "city": "Tabriz",
        "active": True
    },
    {
        "username": "milad",
        "age": 35,
        "city": "Tehran",
        "active": True
    }
]

def check_access(users: list, username: str) -> bool:
    '''
    liste user ha va username yek user ra be onvene voroodi migirad
    dar soorate balaye 18sal va active budan True ra khorooji midiahad dar gheyre in soorat False
    '''
    for user in users:
        if user["username"] == username:
            if user["age"] >= 18 and user["active"]:
                return True
            else:
                return False
      

    
result_1 = check_access(users_list,"milad")
print(result_1)

result_2 = check_access(users_list,"sara")
print(result_2)


#--------------------------------------------------------------------------------
#d

users_list = [
    {
        "username": "ali",
        "age": 25,
        "city": "Tehran",
        "active": True
    },
    {
        "username": "sara",
        "age": 17,
        "city": "Tabriz",
        "active": True
    },
    {
        "username": "milad",
        "age": 35,
        "city": "Tehran",
        "active": True
    }
]

def get_adult_users(users: list) -> list:
    '''
    liste user ha ra be onvene voroodi migirad
    dar soorate balaye 18sal budan dar yek list an ra khorooji midiahad
    '''
    adult_users_list = []
    for user in users:
        if user["age"] >= 18:
            adult_users_list.append(user)
    return adult_users_list        
      

    
result_1 = get_adult_users(users_list)
print(result_1)






