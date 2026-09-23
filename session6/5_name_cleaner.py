"""
5_name_cleaner
yek tabe benevisid ke esme kamel (esm famil) ro begire va dorostesh kone kamel va khoroji bede

```bsh
"   aLi   pILeHvAr     "
```

va khroji bayad in bashe

```bsh
"Ali Pilehvar Meibody"
```
"""

def name_cleaner (name: str) -> str :
    '''
    name ra be onvane voroodi migirad
    moratab va ziba mikonad va an ra be onvane khorooji midahad
    '''
    clean_name = " ".join(name.split()).title()
    return clean_name
    
result_1 = name_cleaner("   elina  KheirkHah  ")
print(result_1)

result_2 = name_cleaner("   aLi   pILeHvAr     ")
print(result_2)   