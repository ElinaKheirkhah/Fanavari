#Optional 3

'''
yek tabe be name create_profile benevisid ke do vorodie ejbari begire bename name,age 
alave bar in , betavanim har che tedade etelate ezafi ro ba estefade az **kwargs begire.

masalan : city, job, emnail , harchiii

khob tabe bayad inkaro kone :
- namo sen ro namayesh bede
- tamame etelaate ezafi ro namayesh dahad
- tedade etelaate ezafi ro chap kone
- agar city vojod dasht ,shahro ro jodagone neshon bede
- agar email vojod nadasht ebenvise : email not provided
dar enteha ham tamame etelaate karbar ro dakhele yek dictionary jadid bezare o return kone
'''


#man chon hame etelaate ezafi ro joda va kamel namayesh dadam dige shahr ro joda nakardam


def create_profile(name,age,**extra_data):
    print("--------------------------------")
    print(f"esm: {name}")
    print(f"sen: {age}")
    
    #print(type(extra_data)) #<class 'dict'>
    count_extra = 0
    for extra_key,extra_value in extra_data.items():
        count_extra = count_extra + 1
        print(f"etelaate ezafi({count_extra}): {extra_key} - {extra_value}")
    #print(f"tedade etelaate ezafi: {len(extra_data)}")
    print(f"tedade etelaate ezafi: {count_extra}")
    
    if "email" not in extra_data:
        print("email not provided")
    
    print("--------------------------------")    
        
    profile = {
        "name": name,
        "age": age,
        **extra_data
    }

    return profile
    
    
    
create_profile("elen",25,city="tehran",phone="09190153108", email="elina@gmail.com")  
    
create_profile("elen",25,city="tehran",phone="09190153108")  

    
test_profile = create_profile("elen",25,city="tehran",phone="09190153108", email="elina@gmail.com")

print(test_profile)
















