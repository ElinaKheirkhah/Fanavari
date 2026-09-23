"""
2_check_number

yek file besazid va tabe(fucntion) haye zir ro besazid

a) tabe bayad vorodi number ro begire , agar zoj bood khoroji bede 'Even' agar fard bood  bede 'Odd'

b) tabe yek vorodi number begire agar zoj bod True bde agar fard bood False pas bede

c) yek tabe benevisid number begire va check kone agar mosbat bood 'Positive' agar manfi bood 'Negative' agar sefr bood 'Zero' pas bede
"""

#a

def odd_or_even (number :int) -> str:
    '''
    yek number be onvane voroodi migirad 
    zoj ya fard budane an ra khorooji midahad
    '''
    
    if number % 2 == 0 :
        return "Even"
    else:
        return "Odd"
    
result_1 = odd_or_even(25)
print(result_1)

result_2 = odd_or_even(28)
print(result_2)

#------------------------------------------------------------------------------
#b

def is_even (number :int) -> bool:
    '''
    yek number be onvane voroodi migirad 
    agar zoj bashad True khorooji midahad
    agar fard bashad False khorooji midahad
    '''
    
    if number % 2 == 0 :
        return True
    else:
        return False
    
result_1 = is_even(25)
print(result_1)

result_2 = is_even(28)
print(result_2)
  
#kholase tar    
def is_number_even(number: int) -> bool:
    return number % 2 == 0    
    
result_1 = is_number_even(25)
print(result_1)

result_2 = is_number_even(28)
print(result_2)

#------------------------------------------------------------------------------
#c

def negative_or_positive (number :float) -> str:
    '''
    yek number be onvane voroodi migirad 
    agar adad mosbat bashad positive agar manfi bashad negative va agar sefr bashad haman sefr khorooji midahad
    '''
    
    if number > 0 :
        return "Positive"
    elif number < 0 :
        return "Negative"
    else :
        return "Zero"
    
result_1 = negative_or_positive(12.36)
print(result_1)

result_2 = negative_or_positive(-65025.865)
print(result_2)

result_3 = negative_or_positive(0)
print(result_3)

result_4 = negative_or_positive(0.3658)
print(result_4)