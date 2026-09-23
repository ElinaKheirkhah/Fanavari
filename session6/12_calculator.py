"""
12_calculator

yek tabe benvisid ke do adad begire va yek operation

agar operation jam bod anjam bede va javab ro khoroji bede

agar tafrigh --> menha kone bargardon

agar zarb bood --> zarb kone bargardoone

agar taghsim bood --> taghsim kone bargardone

agar operation chizi joz jam,tafrigh,zarb,taghsim bood , None bargardoone
"""

def calculator (number1 : float, number2 : float, operation : str) -> float :
    '''
    2ta adad va yek operation ra be onvane voroodi migirad
    javab ra be onvane khorooji midahad
    '''
    
    if operation == "jam":
        result = number1 + number2
        return result
    elif operation == "tafrigh":
       result = number1 - number2
       return result
    elif operation == "zarb":
       result = number1 * number2
       return result
    elif operation == "taghsim":
       result = number1 / number2
       return result
    else :
        None
       #mitunim in shekli ham error bedim:
       #raise ValueError("operation vared shode eshtebah ast.")
    
result_1 = calculator(40,20,"zarb")
print(result_1)

result_2 = calculator(40,20,"zadrb")
print(result_2)




















