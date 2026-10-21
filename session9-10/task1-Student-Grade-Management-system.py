#===============================================
#=====================Task 1====================
#===============================================
#=======Student Grade Management System=========
#===============================================




FILE_PATH = 'C:/Users/ASUS/Desktop/grades.txt'

#-------------------------------------------------
#ino baraye save kardane data daneshjooyan ezafe kardam ke har bar az aval file ro read nakonam
def get_grades():
    
    try:
        with open(FILE_PATH, 'r') as file:
            grades_list = file.readlines()

    except FileNotFoundError:
        return []

    students = []
    
    try:
        for line in grades_list:
            #print(line)
            #print(type(line))
            name, grade = line.strip().split(" - ")
            grade = float(grade)

            if not name or not 0 <= grade <= 20:
                raise ValueError

            students.append((name, grade))

    except ValueError:
        raise ValueError("Error: data haye file namotabar ast.")

    #print(students)
    return students

#get_grades()


#-------------------------------------------------
def add_grade (name:str ,grade:float):
    
    try:
        grade = float(grade)

    except (ValueError, TypeError):
        print("Error: nomre bayad adad bashad.")
        return

    if not 0 <= grade <= 20:
        print("Error: nomre bayad beyne 0 ta 20 bashad.")
        return

    
    try:
        students = get_grades()
    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return

    for index, (student_name, student_grade) in enumerate(students):

        if student_name == name:
            students[index] = (name, grade)

            with open(FILE_PATH, 'w') as file:
                for student_name, student_grade in students:
                    file.write(f'{student_name} - {student_grade}\n')

            print("nomreye daneshju update shod.")
            return
    
    with open(FILE_PATH, 'a') as file:
        file.write(f'{name} - {grade}\n')
        
    print("esm va nomreye daneshju be file ezafe shod")    
    

#-------------------------------------------------    
def read_grades():
    try:
        all_students = get_grades()

        for name, grade in all_students:
            print(f'{name} - {grade}')

    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        
#-------------------------------------------------        

def calculate_average():
    try:
        students = get_grades()

        count_grades = len(students)

        if count_grades == 0:
            raise ValueError("hich nomrei vojood nadard.")

        sum_grades = 0

        for name, grade in students:
            sum_grades = sum_grades + grade

        miangin = sum_grades / count_grades

        print(f'miangine nomarate daneshjooyan {miangin} mibashad.')

    except (ValueError, OSError) as error:
        print(f"Error: {error}")


#-------------------------------------------------

def find_top_student():
    try:
        students = get_grades()

        if len(students) == 0:
            raise ValueError("hich nomrei vojood nadarad.")

        top_grade = students[0][1]
        top_grade_name = students[0][0]

        for student in students:
            name, grade = student

            if grade > top_grade:
                top_grade = grade
                top_grade_name = name

        print(f'balatarin nomreye list: {top_grade_name} -- {top_grade}')

    except (ValueError, OSError) as error:
        print(f"Error: {error}")
 
      
#-------------------------------------------------


add_grade("elen", 20)

add_grade("milad", 19)

add_grade("sara", 18)

add_grade("milad", 16) #nomreye daneshju update shod.

add_grade("milad", "f") #Error: nomre bayad adad bashad.

add_grade("milad", 23) #Error: nomre bayad beyne 0 ta 20 bashad.

read_grades()

calculate_average()

find_top_student()
