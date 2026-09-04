#---------q5.2------------------
'''
Q2
yek listi az nomre haye daneshjoha va esmashon dairm, 
dar enteha faghat esme daneshjohaei ke pass shodan ro neshon bede (optional : onaro rank bandi ham kone)
'''

print("=================Q2=======================")
print("==========================================")

students = ['ali','vahid','sara','hamid','reza','elham','mohsen','zahra','paniz','parmida']
scores = [20,17,9 , 13, 7 , 20 , 18 , 3 , 1 , 14]

passed: []
for student , score in zip(students , scores):
    if score >= 10 :
        print(student , ":" , score)
    
        