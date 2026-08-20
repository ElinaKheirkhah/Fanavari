#---------q3.5------------------
'''
az karbar esme product ro begire berize to zarf

gheymatesho begire berize too zarf

code takhfif begire

age code takhfif barabar bood ba z14

20% az gheymat kam kone nmaayesh bede
bege gheymate nahaei ine 


q3.5.2. --> ag code takhfif eshtebah zad --> bege 
ghalat zadid

q3.5.3 --> ag ghalat zad, bege yekbar dg mitoni emtehan kone
ag doros zad anjam bde (takhfif) ag na --> bege block shodid
'''

print("=============shopping===============")
print("============================================")

esme_mahsool = input("lotfan esme mahsool ra vared konid: ")
gheymate_mahsool = int(input("lotfan gheymate mahsool ra vared konid: "))
code_takhfif = input("lotfan code takhfif ra vared konid: ").upper()

if code_takhfif == "Z14":
    gheymate_nahaei = int(gheymate_mahsool * 0.8)
    print(f"shoma mahsoole {esme_mahsool} ra ba gheymate {gheymate_nahaei} kharidari kardid va code takhfife {code_takhfif} rooye kharide shoma emal shod.")

else:
    print("code takhfif eshtebah ast. yek bar dige mitavanid emtehan konid.")

    code_takhfif = input("lotfan code takhfif ra dobare vared konid: ").upper()

    if code_takhfif == "Z14":
        gheymate_nahaei = int(gheymate_mahsool * 0.8)
        print(f"shoma mahsoole {esme_mahsool} ra ba gheymate {gheymate_nahaei} kharidari kardid va code takhfife {code_takhfif} rooye kharide shoma emal shod.")

    else:
        print("shoma block shodid.")
