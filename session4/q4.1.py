#---------q4.1------------------
'''
Q1----- Login 

az User , usernamesh ro begirid va passwordesh ro ham begirid , agar
username barabar bashe ba admin va password bashe 1234 benevesid Login ba moafaghiat
anajm shod, agar na , benevisid password ya username ghalat hast.
'''

print("=================Login====================")
print("==========================================")

username = input("lotfan username khod ra vared konid: ")
password = input("lotfan password khod ra vared konid: ")

if username == "admin" and password == "1234":
    print("login ba movafaghiat anjam shod.")
else:
    print("password ya username ghalat ast.")    