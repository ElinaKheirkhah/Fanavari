#---------q3.3------------------
'''
yek machine hesab besazid , 
yek adade (number1) yek adade number2
yechizi begire operation (jam , tafrigh,taghsim,zarb)
anjam bede print kone
'''

print("=============mashin hesab===============")
print("========================================")

first_number = int(input("lotfan adadde aval ra vared konid: "))
amaliate_riazi = input("yeki az in 4 amaliate riazi ra entekhab konid (+ - * /): ")
second_number = int(input("lotfan adadde dovom ra vared konid: "))

if amaliate_riazi == "+":
    result = first_number + second_number
    print(result)

elif amaliate_riazi == "-":
    result = first_number - second_number
    print(result)

elif amaliate_riazi == "*":
    result = first_number * second_number
    print(result)

elif amaliate_riazi == "/":
    if second_number == 0:
        print("taghsim bar 0 emkan pazir nist.")
    else:
        result = first_number / second_number
        print(result)

else:
    print("amaliate vared shode eshtebah ast.")