"""
14_multiplication_table

yek tabe benevisid ke jadval zarb bashe masalan vorodi begire 5 va ino print kone

```bsh
5 × 1 = 5
5 × 2 = 10
...
5 × 10 = 50
```
"""

def multiplication_table (number: int) :
    '''
    yek adad ra be onvane voroodi migirad
    va zarbe an dar 1 ta 10 ra print mikonad
    '''
    
    for mazrab in range(1,11):
        print(f"{number} * {mazrab} = {number*mazrab}")
    
multiplication_table(8)

multiplication_table(13)