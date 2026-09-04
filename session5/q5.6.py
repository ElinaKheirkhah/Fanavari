#---------q5.6------------------
'''
Q6
hamin login system ro benevisind be sharti ke agar bish az 3 bar ehstebah vared kard ,
begid account ghofl shode va dige nazarid username ya password bezane va ende program
'''

print("=================Q6=======================")
print("==========================================")

wrong_count = 0

while True:
    password = input('password ro vared konid: ')

    if len(password) > 8:
        if not password.isdigit() and not password.isalpha():
            if not password.islower() and not password.isupper():
                break

            else:
                print('password nemitone faghat kochik bashe ya faghat bozorg bashe')

        else:
            print('passworde shoma ham bayad digit dahste bashe ham horof')

    else:
        print('password zire 8 rgham nabashad')

    wrong_count = wrong_count + 1

    if wrong_count >= 3:
        print('account ghofl shod!')
        break

print('passworde shoma moafaghiat sabt shod')