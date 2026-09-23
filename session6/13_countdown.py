"""
13_countdown

yek tabe benevisid ke vorodi yek adad begire va az oon adad ta 0 , print kone .

masalan begire 5 --> va print kone

```bsh
5
4
3
2
1
0
```
"""


def countdown (number : int) :
    '''
    yek adad ra be onvane voroodi migirad
    az un adad ta 0 ra print mikonad
    '''
    
    for num in range (number, -1 , -1):
        print(num)
    
countdown(12)

countdown(153)


