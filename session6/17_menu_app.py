"""
17_menu_app

yek tabe besazid ke vorodie e nagire balke dakhelesh yek while shoro she yek menu az ghaza biare , 
va ta zamani ke user 'order' ro nazade hey azash (input) begire va vaghty tamom shod, 
tamame ordere moshtari ro dakhele yek list berize va list ro khoroji bede

"""

def menu_app () -> list :
    '''
    voroodi nmigirad
    sefreshat ra migirad va list midahad
    '''
    print("menu:")
    print("---------------------")
    print("pizza - steak - burger - sandwich - salad")
    print("---------------------")
    
    orders = []
    while True:
        order = input("sefareshe khod ra vared konid:  ")
        if order == "order":
            break
        orders.append(order)
    return orders     

    
result_1 = menu_app()
print(result_1)
