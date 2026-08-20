#---------q3.4------------------
'''
nomreye daneshjo ro begri ye adadi beyne 0 ta 20

age
18-20 --> A
16-18 --> B
14-16 --> C
10-14 --> d
<10 --> f (faill)
'''

print("=============nomreye daneshju===============")
print("============================================")

nomreye_kham = input("lotfan nomreye khod ra vared konid: ")

if nomreye_kham.isdigit():
    nomreye_daneshju = int(nomreye_kham)
    if 0 <= nomreye_daneshju <= 20:
        if 18 <= nomreye_daneshju <= 20:
            print("A")
        elif 16 <= nomreye_daneshju < 18:
            print("B")
        elif 14 <= nomreye_daneshju < 16:
            print("C")
        elif 10 <= nomreye_daneshju < 14:
            print("D")
        else:
            print("F")
    else:
        print("nomreye vared shode kharej az mahdude ast.")
else:
    print("nomreye vared shode dorost nemibashad.")    