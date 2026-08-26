#---------q4.3------------------
'''
Q3---- check mouse

ma yek list darim az mahsoolat , va injori hast : 
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

yek vorodi az karbar begirid va az karbar bekahhdi esme yek mahsol ro bege
agar oon mahsol dakhele in list bashe begid mahsool dar dastress hast , 
agar nabood benevisid dar dastress nist.
'''
#----------------rah 1------------------------

print("=================check product====================")
print("================================================")

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

product_name = input("lotfan name mahsool ra vared konid: ").capitalize()

if products.count(product_name) > 0 :
    print("mahsool dar dastres ast.")
else :
    print("mahsool dar dastres nist.")


#----------------rah 2------------------------

print("=================check product====================")
print("================================================")

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

product_name = input("lotfan name mahsool ra vared konid: ").capitalize()

if  product_name in products:
    print("mahsool dar dastres ast.")
else :
    print("mahsool dar dastres nist.")






