#-----------list functions----------------
#indexed , changable , allow duplicated
#[]

programming_language = ["python" , 1500 , "javascript" , 25.36 , "html" , True , "react"]

programming_language[3] #Out[61]: 25.36
programming_language[:2] #Out[62]: ['python', 1500]
programming_language[3:] #Out[63]: [25.36, 'html', True, 'react']

programming_language[2] [2] #Out[64]: 'v'

#------------------------------------------------------------------------------
#append(element)

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe"]

shopping.append("sneakers")
print(shopping) #['bag', 'jeans', 'tshirt', 'top', 'shoe', 'sneakers']

#ezafe mishe chizi ke migi be onvane elemente akhar

#------------------------------------------------------------------------------
#clear

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe"]

shopping.clear()
print(shopping) #[]

#hame element haye dakhelesho pak mikone khali mishe

#------------------------------------------------------------------------------
#copy

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe"]

shopping_copy = shopping.copy()
print(shopping_copy) #['bag', 'jeans', 'tshirt', 'top', 'shoe']

#ye copy migire azash
#age original taghir kone, in dige taghir nmikone baad az copy shodan

#------------------------------------------------------------------------------
#count

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe" , "jeans"]

print(shopping.count("jeans")) #2

#mige ke chandta az un elemnti ke gofti tu list hast

#------------------------------------------------------------------------------
#extend

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe"]
brands = ["nike" , "adidas" , "veja" , "oysho"]

shopping.extend(brands)
print(shopping) #['bag', 'jeans', 'tshirt', 'top', 'shoe', 'nike', 'adidas', 'veja', 'oysho']

#element haye ye iteerable dige ro ezafe mikone be uni ke mikhay

#------------------------------------------------------------------------------
#index

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe" , "top"]

print(shopping.index("top")) #3

#avalin bari ke un element ro bebine indexesho mige hatta age 100ta azash bashe

#------------------------------------------------------------------------------
#insert(index,value)

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe"]

shopping.insert(2, 125)
print(shopping) #['bag', 'jeans', 125, 'tshirt', 'top', 'shoe']

#mire tu un index mishine - havaset bashe jaygozin nmishe ke chizi ke jashe hazf she

#------------------------------------------------------------------------------
#pop

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe"]

print(shopping.pop(2)) #tshirt
print(shopping) #['bag', 'jeans', 'top', 'shoe']

#ham un elementi ke un index ro dare hazf mikone ham mituni berizish tu ye variable

#------------------------------------------------------------------------------
#remove

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe" , "bag"]

shopping.remove("bag")
print(shopping) #['jeans', 'tshirt', 'top', 'shoe', 'bag']

#avalin bari ke un element ro bebine pak mikone faghat hatta age 100ta azash bashe

#------------------------------------------------------------------------------
#reverse

shopping = ["bag" , "jeans" , "tshirt" , "top" , "shoe"]

shopping.reverse()
print(shopping) #['shoe', 'top', 'tshirt', 'jeans', 'bag']

#orderesho barax mikone

#------------------------------------------------------------------------------
#sort

shopping = ["bag" , "jean" , "tshirt" , "top" , "shoe" , "Zip"]

shopping.sort()
print(shopping) #['Zip', 'bag', 'jean', 'shoe', 'top', 'tshirt']

#be tartibe alefbas vali aval capital ha baad small ha
#agar int va str ro ghati bezari error mide
