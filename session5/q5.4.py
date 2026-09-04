#---------q5.4------------------
'''
Q4
ATM --> yek system ATM sakhte beshe, be karbar bege 'Menu : mojoodi, variz, bardasht , khoroj , amaaliate digar', 
ta zamani ke karbar mojodi  , variz , bardasht ro entekhab kone baraye harkodom kheyli sade benevise
'amaliate variz entekhab shod , ya  amaliate felan entekhab shod' bad beporse 'amaliate digar, khoroj' , 
agar amaliate diagr ro entekhab kard mojadad menu ro neshon bede 'mojoodi , variz,bardasht' , 
ama agar rooye khoroj zad bege mamnon khoroj ba moafaghiat anajm shod
'''

print("=================Q4=======================")
print("==========================================")

while True:

    print("Menu:")
    print("1. mojoodi")
    print("2. variz")
    print("3. bardasht")

    choice = input("entekhab konid: ")

    if choice == "1":
        print("amaliate mojoodi entekhab shod")

    elif choice == "2":
        print("amaliate variz entekhab shod")

    elif choice == "3":
        print("amaliate bardasht entekhab shod")

    else:
        print("entekhab namotabar ast")
        continue

    other = input("amaliate digar ya khoroj? ")

    if other == "khoroj":
        print("mamnon, khoroj ba movafaghiat anjam shod")
        break

    elif other == "amaliate digar":
        continue