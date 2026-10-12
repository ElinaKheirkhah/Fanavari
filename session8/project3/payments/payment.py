
'''
dakhele payments/payment.py tabeye calculate_fee ro az file fee.py improt konid

hamchenin dakhele payments/payment.py bayad login ro az package accounts import konid
'''

from .fee import calculate_fee

from accounts.authentication import login



def make_payment():
    print("make_payment checked")
    
    
    
calculate_fee()    

login()