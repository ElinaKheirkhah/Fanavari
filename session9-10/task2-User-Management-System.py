#===============================================
#=====================Task 2====================
#===============================================
#===========User Management System==============
#===============================================


FILE_PATH = 'C:/Users/ASUS/Desktop/users-management.txt'

#-------------------------------------------------

def get_users():
    
    try:
        with open(FILE_PATH, 'r') as file:
            users_list = file.readlines()

    except FileNotFoundError:
        return []

    users = []
    
    try:
        for line in users_list:
            #print(line)
            #print(type(line))
            number, name, email, status = line.strip().split(",")

            users.append((int(number), name, email, status))

    except ValueError:
        raise ValueError("Error: data haye file namotabar ast.")


    return users

#-------------------------------------------------

def add_user(name: str, email: str, status: str):

    try:
        users = get_users()

    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return

    for number, user_name, user_email, user_status in users:

        if user_email == email:
            print("email tekrari mibashad.")
            return
    
    if status not in ("active","blocked"):
        print("status bayad active ya blocked bashad.")
        return
    
    if  not email.endswith(".com"):
        print("email bayad motabar bashad.")
        return

    if len(users) == 0:
        number = 1
    else:
        number = max(user[0] for user in users) + 1

    with open(FILE_PATH, 'a') as file:
        file.write(f'{number},{name},{email},{status}\n')

    print("user e jadid be file ezafe shod.")


#-------------------------------------------------

def find_user(name_or_number: str | int):
    try:
        users = get_users()

    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return
    
    for number, user_name, user_email, user_status in users:

        if user_name == name_or_number or str(number) == str(name_or_number):
            print(f"{number},{user_name},{user_email},{user_status}")
            return
    print("user peyda nashod.")    


#-------------------------------------------------

def delete_user(user_number: int):
    try:
        users = get_users()

    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return

    for number, user_name, user_email, user_status in users:
        if user_number == number:
            users.remove((number, user_name, user_email, user_status))

            with open(FILE_PATH, 'w') as file:
                for number, user_name, user_email, user_status in users:
                    file.write(f"{number},{user_name},{user_email},{user_status}\n")

            print("user ba movafaghiat hazf shod.")
            return

    print("user peyda nashod.")

#-------------------------------------------------

def update_user(search_name: str, user_email_or_status: str):
    try:
        users = get_users()

    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return

    for index, (number, user_name, user_email, user_status) in enumerate(users):
        if user_name == search_name:
            
            if user_email_or_status in ("active", "blocked"):
                user_status = user_email_or_status
                
            elif user_email_or_status.endswith(".com"):
                for other_number, other_name, other_email, other_status in users:
                    if other_email == user_email_or_status and other_number != number:
                        print("email tekrari mibashad.")
                        return
                user_email = user_email_or_status
                
            else:
                raise ValueError("data vared shode email ya status nemibashad.")

            users[index] = (number, user_name, user_email, user_status)

            with open(FILE_PATH, 'w') as file:
                for number, user_name, user_email, user_status in users:
                    file.write(f"{number},{user_name},{user_email},{user_status}\n")

            print("user ba movafaghiat update shod.")
            return

    print("user peyda nashod.")


#-------------------------------------------------

def list_users():
    try:
        users = get_users()

    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return
    
    for number, user_name, user_email, user_status in users:
        print(f"{number},{user_name},{user_email},{user_status}")

#-------------------------------------------------

def generate_report():
    try:
        users = get_users()

    except (ValueError, OSError) as error:
        print(f"Error: {error}")
        return
    
    all_users_count = 0
    active_users_count = 0
    blocked_users_count = 0
    
    for number, user_name, user_email, user_status in users:
        all_users_count += 1
        if user_status == "active":
            active_users_count += 1
        elif user_status == "blocked":
            blocked_users_count += 1
            
    print(f"tedade kole user ha: {all_users_count}")
    print(f"tedade user haye active: {active_users_count}")
    print(f"tedade user haye blocked: {blocked_users_count}")

#-------------------------------------------------
#-------------------------------------------------

while True:
    print("\n===== User Management =====")
    print("1. Add user")
    print("2. Find user")
    print("3. Delete user")
    print("4. Update user")
    print("5. List users")
    print("6. Generate report")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        status = input("Enter user status (active/blocked): ")

        add_user(name, email, status)

    elif choice == "2":
        name_or_number = input("Enter user name or ID: ")
        find_user(name_or_number)

    elif choice == "3":
        try:
            user_number = int(input("Enter user ID to delete: "))
            delete_user(user_number)

        except ValueError:
            print("Error: user ID must be a number.")

    elif choice == "4":
        search_name = input("Enter user name to update: ")
        user_email_or_status = input("Enter new email or status: ")

        try:
            update_user(search_name, user_email_or_status)

        except ValueError as error:
            print(f"Error: {error}")

    elif choice == "5":
        list_users()

    elif choice == "6":
        generate_report()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")



#-------------------------------------------------
#-------------------------------------------------


'''


add_user("elen", "elen@gmail.com", "active")
find_user("elen") 
find_user(1)

add_user("milad", "milad@gmail.com", "active")

add_user("sara", "sara@gmail.com", "active")



delete_user(1)

update_user("milad", "blocked")

list_users()

generate_report()
'''

