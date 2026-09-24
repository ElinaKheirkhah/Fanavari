"""
q7.3

Yek tabe benvisid ke yek listi az karmandan ba etelaatesho migire
employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}

- balatarin hoghogh ro harki migire esmesho pas bedde
- kamtarin hogh ro harki migire esmesho pas bede
- yek listi az esme afradi k hoghoghe bish az 3000 migiran pas bede
- do vorodi begire tabe, yeki in dictionary (employees) yeki ye adad ke bedre liste esme afradi ke hoghoghe bishtar az oon adad ro migiran ro pas bede
- miangine kole hoghogh haro pas bede

"""

employees_list = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


#-----------------------------------1--------------------------------------

def find_maximum_salary_name (employees: dict) -> str :
    maximum_salary = 0

    for employee in employees:
        if employees[employee]["salary"] > maximum_salary:
            maximum_salary = employees[employee]["salary"]
            maximum_salary_name = employees[employee]["name"]
    return maximum_salary_name

    
result_1 = find_maximum_salary_name(employees_list)
print(result_1)

#-----------------------------------2--------------------------------------

def find_minimum_salary_name (employees: dict) -> str :
    minimum_salary = float("inf")

    for employee in employees:
        if employees[employee]["salary"] < minimum_salary:
            minimum_salary = employees[employee]["salary"]
            minimum_salary_name = employees[employee]["name"]
            
    return minimum_salary_name

    
result_2 = find_minimum_salary_name(employees_list)
print(result_2)

#-----------------------------------3--------------------------------------

def find_salary_more_than_3000 (employees: dict) -> list :
    salary_more_than_3000 = []
    for employee in employees:
        if employees[employee]["salary"] > 3000:
            salary_more_than_3000.append(employees[employee]["name"])
            
    return salary_more_than_3000

    
result_3 = find_salary_more_than_3000(employees_list)
print(result_3)

#-----------------------------------4--------------------------------------

def find_salary_more_than_this (employees: dict, chosen_salary: int) -> list :
    salary_more_than_this = []
    for employee in employees:
        if employees[employee]["salary"] > chosen_salary:
            salary_more_than_this.append(employees[employee]["name"])
            
    return salary_more_than_this

    
result_4 = find_salary_more_than_this(employees_list,3500)
print(result_4)

#-----------------------------------5--------------------------------------

def average_salary (employees: dict) -> float :
    sum_salary = 0
    count_salary = 0
    for employee in employees:
        sum_salary = sum_salary + employees[employee]["salary"]
        count_salary = count_salary + 1
            
    return sum_salary / count_salary

    
result_5 = average_salary(employees_list)
print(result_5)










