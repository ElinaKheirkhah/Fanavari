"""
11_failed_score

yek tabe benevisid ke listi az nomre haor begire va nomre haye fail ro hazf kone va oon list ro bargardoone

masalan vorodi
```bsh
[18, 7, 13, 9, 20, 5]
``` 

begire va khoroji bede
```bsh
[18, 13, 20]
```

b) halam hamon vorodi yek list begire az nomre ha va khoroji liste onaei ke fail shodan ro pass bede 


c) hala hamon vorodi yek list begire az nomre ha va dar khoroji bejaye list, tedade afradi ke pass shodan ro pass bede
"""

#a

def passed_scores (scores: list) -> list :
    '''
    liste nomarat ra be onvane voroodi migirad
    az list fail shode ha ra hazf mikonad va liste jadid ra be onvane khorooji midahad
    '''
    
    new_scores_list = []
    for score in scores:
        if score >= 10:
            new_scores_list.append(score)
    return new_scores_list
    
result_1 = passed_scores([10,17,16,8,11,6.5])
print(result_1)

#------------------------------------------------------------------------------
#b

def failed_scores (scores: list) -> list :
    '''
    liste nomarat ra be onvane voroodi migirad
    liste failed shode ha ra be onvane khorooji midahad
    '''
    
    new_scores_list = []
    for score in scores:
        if score < 10:
            new_scores_list.append(score)
    return new_scores_list
    
result_1 = failed_scores([10,17,16,8,11,6.5])
print(result_1)

 
#------------------------------------------------------------------------------
#c

def count_passed_scores (scores: list) -> int :
    '''
    liste nomarat ra be onvane voroodi migirad
    tedade nomarate pass shode ra be onvane khorooji midahad
    '''
    
    count_passed = 0
    for score in scores:
        if score >= 10:
            count_passed = count_passed + 1
    return count_passed
    
result_1 = count_passed_scores([10,17,16,8,11,6.5])
print(result_1)

 























