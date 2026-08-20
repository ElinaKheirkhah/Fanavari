#-----------tuple functions----------------
#indexed , unchangable , allow duplicated
#()

programming_language = ("python" , 1500 , "javascript" , 25.36 , "html" , True , "react")

programming_language[3] #Out[82]: 25.36
programming_language[:2] #Out[83]: ['python', 1500]
programming_language[3:] #Out[84]: [25.36, 'html', True, 'react']

programming_language[2] [2] #Out[85]: 'v'

#------------------------------------------------------------------------------
#index

names = ["milad" , "amin" , "mohammad" , "milad" , "ali"]

print(names.index("milad")) #0

#avalin bari ke un element ro bebine indexesho mige hatta age 100ta azash bashe

#------------------------------------------------------------------------------
#count

names = ["milad" , "amin" , "mohammad" , "milad" , "ali"]

print(names.count("milad")) #2

#mige ke chandta az un elemnti ke gofti tu tuple hast
