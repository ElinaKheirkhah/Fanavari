
'''
dar main.py bayad in mavared ro import konid
create_user
create_account
request_loan
create_card
'''

from user import create_user

from bank.account import create_account,close_account

from bank.loan import request_loan

from bank.card import create_card


create_user()

create_account()

close_account()

request_loan()

create_card()
 

