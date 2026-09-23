"""
4_calculate_garde
yek tabe benevisid ke systeme nomre dehi hast , va nomre beyne 0 ta 100 begire va dar java ino bargardoone

```bsh
90-100 -> A
80-89 -> B
70-79 -> C
60-69 -> D
below 60 -> F
```
"""

def system_nomredehi (nomre: int) -> str :
    '''
    nomre ra be onvane voroodi migirad
    tebghe 5 baze az A-F ra khorooji midahad
    '''
    
    if nomre > 100:
        return "nomre nmitavanad az 100 bishtar bashad"
    elif nomre >= 90:
        return "A"
    elif nomre >= 80:
        return "B"
    elif nomre >= 70:
        return "C"
    elif nomre >= 60:
        return "D"
    elif nomre >= 0:
        return "F"
    else:
        return "nomre nmitavanad az 0 kamtar bashad"
    
result_1 = system_nomredehi(150)
print(result_1)

result_2 = system_nomredehi(96)
print(result_2)   

result_3 = system_nomredehi(80)
print(result_3)

result_4 = system_nomredehi(73)
print(result_4) 

result_5 = system_nomredehi(69)
print(result_5)

result_6 = system_nomredehi(35)
print(result_6) 

result_7 = system_nomredehi(-18)
print(result_7) 