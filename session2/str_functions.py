#------------Str functions---------------

word_one = "friendship"

word_one[5]   #Out[3]: 'd'
word_one[10]   #IndexError: string index out of range

word_one[2:8]   #Out[13]: 'iendsh'
word_one[:7]    #Out[11]: 'friends'
word_one[3:]    #Out[12]: 'endship'

#----------------------------------------------------------------------------------------------------------

sentence_one = "python is a programming language."

sentence_one[6]   #Out[9]: ' '

sentence_one[3:15]  #Out[14]: 'hon is a pro'
sentence_one[:9]    #Out[16]: 'python is'
sentence_one[4:]    #Out[15]: 'on is a programming language.'

#-----------------------------------------------------------------------------------------------------------

sentence_two = "python is A programming language."

func_1 = sentence_two.capitalize()
print(func_1)  #Python is a programming language.
#--harfe aval ro capital mikone va hame baghiye ro small

#-----------------------------------------------------------------------------------------------------------
func_2 = sentence_two.casefold()
print(func_2)  #python is a programming language.
#--hame ro small mikone

#-----------------------------------------------------------------------------------------------------------
func_3 = "python".center(10, "z")
print(func_3) #zzpythonzz
#--miad string toro mizare vasat va un chizi neveshti ya age fasele gozashti ro az 2taraf 
#--ta un tedadi ke gofti beshe ezafe mikone
#--faghat ye character ya masalan khali mitune bashe

#-----------------------------------------------------------------------------------------------------------
func_4_1 = sentence_two.count("mi")
print(func_4_1)  #1
#--har stringi che character che kalame o jomle behesh bedi mige behet chand tas

func_4_2 = sentence_two.count("mi",3,10)
print(func_4_2)  #0
#--baze ham mituni behesh bedi - age nadi tu kolesh migarde

#-----------------------------------------------------------------------------------------------------------
func_5 = sentence_two.encode()
print(func_5)  #b'python is A programming language.'
#--string ro be bytes tabdil mikone

#-----------------------------------------------------------------------------------------------------------
func_6_1 = sentence_two.endswith(".")
print(func_6_1)  #True
#--check mikone ke string ba character ya string morede nazar tamoom mishe ya na

func_6_2 = sentence_two.endswith("hi")
print(func_6_2)  #False
#--va true/false mide

#-----------------------------------------------------------------------------------------------------------
func_7 = "python\tis".expandtabs(10)
print(func_7)  #python    is
#--tab (\t) ro be space tabdil mikone
#--pas bayad / ro tu stringet dashte bashi

#-----------------------------------------------------------------------------------------------------------
func_8 = sentence_two.find("programming")
print(func_8)  #12
#--migarde index e avalin jaei ke behesh mirese ro behet mige
#--agar chanta azash bashe in avali ro mige faghat

#-----------------------------------------------------------------------------------------------------------
name = "Elina"
age = 25

example1 = "My name is {} and I am {} years old."

result1 = example1.format(name, age)
print(result1)

example2 = "My favorite programming language is {}."

result2 = example2.format("Python")
print(result2)

#-- {} haye dakhele string ro ba meghdari ke be format midim por mikone

#-----------------------------------------------------------------------------------------------------------

# 10 format_map() nafahmidam

#-----------------------------------------------------------------------------------------------------------
#func_11_1 = sentence_two.index("hhh")
#print(func_11_1)  #ValueError: substring not found

func_11_2 = sentence_two.index("p")
print(func_11_2)  #0
#--index-e avalin jaye peyda shodan-e character ya substring ro barmigardoone
#--age peyda nashe ValueError mide

#*/*/farghesh ba find ine ke un age peyda nakone -1 mide vali in kollan error mide
#pas index vaghti estefade mishe ke motmaenim vojod dare vali find vaghti motmaen nistim

#-----------------------------------------------------------------------------------------------------------
func_12 = sentence_two.isalnum()
print(func_12)  #False
#--check mikone ke aya hame character haye string ya adad hastan ya horof
#--age hame adad ya horof bashan True mide
#--age space ya character haye mesle ! @ . dashte bashe False mide

example = "Python123"
print(example.isalnum())  #True

example = "Python 123"
print(example.isalnum())  #False

#-----------------------------------------------------------------------------------------------------------
func_13 = sentence_two.isalpha()
print(func_13)  #False
#--check mikone ke aya hame character haye string faghat horof hastan ya na
#--age faghat horof bashan True mide
#--space, adad va character haye digar dashte bashe False mide

example = "Python"
print(example.isalpha())  #True

example = "Python123"
print(example.isalpha())  #False

#-----------------------------------------------------------------------------------------------------------
func_14 = sentence_two.isascii()
print(func_14)  #True
#--check mikone ke aya hame character haye string ASCII hastan ya na
#--age hame ASCII bashan True mide
#--character haye mesle horofe farsi ASCII nistan

example = "Python 123 !"
print(example.isascii())  #True
#--hatta space va ! ham ASCII hastan

#-----------------------------------------------------------------------------------------------------------
func_15 = sentence_two.isdecimal()
print(func_15)  #False
#--check mikone ke aya hame character haye string decimal digit hastan ya na
#--age faghat decimal digit bashe True mide
#--horof, space va character haye digar False mide

example = "12345"
print(example.isdecimal())  #True

example = "12.5"
print(example.isdecimal())  #False
#chon . dare

#-----------------------------------------------------------------------------------------------------------
func_16 = sentence_two.isdigit()
print(func_16)  #False
#--check mikone ke aya hame character haye string digit hastan ya na
#--age hame digit bashan True mide
#--age horof ya space ya character haye digar bashe False mide

example = "12345.5"
print(example.isdigit())  #True

example = "123a"
print(example.isdigit())  #False

#-----------------------------------------------------------------------------------------------------------
func_17 = sentence_two.isidentifier()
print(func_17)  #False
#--check mikone ke aya string mitune yek identifier dar Python bashe ya na
#--identifier yani esm-e variable, function, class va ...

example = "my_variable"
print(example.isidentifier())  #True

example = "my variable"
print(example.isidentifier())  #False

#-----------------------------------------------------------------------------------------------------------
func_18 = sentence_two.islower()
print(func_18)  #False
#--check mikone ke aya horofe string lowercase hastan ya na
#--age hame horof lowercase bashan True mide
#--age hatta yek horof uppercase dashte bashim False mide

#-----------------------------------------------------------------------------------------------------------
func_19 = sentence_two.isnumeric()
print(func_19)  #False
#--check mikone ke aya hame character haye string numeric hastan ya na
#--age hame numeric bashan True mide
#--age horof ya space ya character haye digar dashte bashe False mide

#**az ghablia gostarde tare va ye seri character haye adadi ro ham ghabul mikone
#**isdecimal() < isdigit() < isnumeric()

#-----------------------------------------------------------------------------------------------------------
func_20 = sentence_two.isprintable()
print(func_20)  #True
#--check mikone ke aya hame character haye string ghabele print shodan hastan ya na
#--space va character haye adi printable hastan
#--character haye mesle \n va \t printable nistan

example = "Hello\nPython"
print(example.isprintable())  #False
#--chon \n yani raftan ba khate baad va printable nist

#-----------------------------------------------------------------------------------------------------------
func_21 = sentence_two.isspace()
print(func_21)  #False
#--check mikone ke aya hame character haye string whitespace hastan ya na
#--whitespace yani space, tab (\t), newline (\n) va ...
#--age hame whitespace bashan True mide

example = " \n  "
print(example.isspace())  #True

#-----------------------------------------------------------------------------------------------------------
func_23 = sentence_two.isupper()
print(func_23)  #False
#--check mikone ke aya hame horofe string uppercase hastan ya na
#--age hame horof uppercase bashan True mide
#--age hatta yek horof lowercase dashte bashim False mide

#-----------------------------------------------------------------------------------------------------------
func_24 = "-".join(["Python", "is", "good"])
print(func_24)  #Python-is-good
#--item haye dakhele list ya iterable ro be ham vasl mikone
#--character ya stringi ke ghabl az join neveshtim beyneshon gharar migire 
#--mituni khali bezari ke fasele bendaze masalan

#-----------------------------------------------------------------------------------------------------------
func_25 = "Python".ljust(10, "-")
print(func_25)  #Python----
#--string ro az samt chap justify mikone va ta tool morede nazar berese character ezafe mikone
#faghat ye charcter migire

#-----------------------------------------------------------------------------------------------------------
func_26 = sentence_two.lower()
print(func_26)  #python is a programming language.
#--hame harf haye uppercase ro lowercase mikone

#-----------------------------------------------------------------------------------------------------------
example = "   Python"
func_27 = example.lstrip()
print(func_27)  #Python
#--space haye samt chap string ro hazf mikone

#-----------------------------------------------------------------------------------------------------------
#28 maketrans nafahmidam

#-----------------------------------------------------------------------------------------------------------
example = "Python is programming"
func_29 = example.partition("is")
print(func_29)  #('Python ', 'is', ' programming')
#--string ro bar asase value morede nazar be 3 bakhsh taghsim mikone
#--bakhsh aval ghabl az value
#--khode value
#--bakhsh dovom baad az value
#--va khorooji tuple hast

#-----------------------------------------------------------------------------------------------------------
func_30 = sentence_two.replace("A", "a")
print(func_30)  #python is a programming language.
#--ye value ro ba value dige jaygozin mikone
#--mitune kalame ham bashe

#-----------------------------------------------------------------------------------------------------------
example = "Python kheili khub va Python kheili rahate."

func_31 = example.rfind("Python")
print(func_31)  #22
#--mesle find() migarde vali index-e akharin jayi ke value peyda shode ro mide
#--age peyda nashe -1 mide

#-----------------------------------------------------------------------------------------------------------
example = "Python kheili khub va Python kheili rahate."

func_32 = example.rindex("Python")
print(func_32)  #22
#--mesle rfind() akharin jaye peyda shodan-e value ro mide
#--age peyda nashe ValueError mide

#-----------------------------------------------------------------------------------------------------------
func_33 = "Python".rjust(10, "-")
print(func_33)  #----Python
#--string ro az samt rast justify mikone va character ezafe mikone ta be tool morede nazar berese

#-----------------------------------------------------------------------------------------------------------
example = "Python is good and Python is easy"

func_34 = example.rpartition("Python")
print(func_34)  #('Python is good and ', 'Python', ' is easy')
#--string ro bar asase akharin jaei ke value hast be 3 bakhsh taghsim mikone

#-----------------------------------------------------------------------------------------------------------
example = "Python is a programming language"

func_35 = example.rsplit(" ", 3)
print(func_35)  #['Python is', 'a', 'programming', 'language']
#--string ro bar asase separator split mikone vali az samt rast

#-----------------------------------------------------------------------------------------------------------
example = "Python   "
func_36 = example.rstrip()
print(func_36)  #Python
#--space haye samt rast string ro hazf mikone

#-----------------------------------------------------------------------------------------------------------
example = "Python is a programming language"

func_37 = example.split()
print(func_37)  #['Python', 'is', 'a', 'programming', 'language']
#--string ro be chand bakhsh taghsim mikone va natije ro be sorate list mide
#--age separator bedim bar asase un string ro split mikone

#-----------------------------------------------------------------------------------------------------------
example = "Python\nJava\nC++"

func_38 = example.splitlines()
print(func_38)  #['Python', 'Java', 'C++']
#--string ro bar asase line break be chand bakhsh taghsim mikone va list mide

#-----------------------------------------------------------------------------------------------------------
func_39 = sentence_two.startswith("python")
print(func_39)  #True
#--check mikone ke string ba character ya string morede nazar shoroo mishe ya na
#--va True ya False mide

#-----------------------------------------------------------------------------------------------------------
example = "   Python   "

func_40 = example.strip()
print(func_40)  #Python
#--space haye aval va akhar string ro hazf mikone

#-----------------------------------------------------------------------------------------------------------
example = "Python IS Good"

func_41 = example.swapcase()
print(func_41)  #pYTHON is gOOD
#--uppercase ro lowercase va lowercase ro uppercase mikone

#-----------------------------------------------------------------------------------------------------------
func_42 = sentence_two.title()
print(func_42)  #Python Is A Programming Language.
#--avalin harfe har kalame ro uppercase mikone
#--baghie harf haye kalame ro lowercase mikone

#-----------------------------------------------------------------------------------------------------------

#43 translate nafahmidam 

#-----------------------------------------------------------------------------------------------------------
func_44 = sentence_two.upper()
print(func_44)  #PYTHON IS A PROGRAMMING LANGUAGE.
#--hame harf haye lowercase ro uppercase mikone

#-----------------------------------------------------------------------------------------------------------
example = "123"

func_45 = example.zfill(6)
print(func_45)  #000123
#--az samt chap be string zero ezafe mikone ta be tool morede nazar berese
#--hatta age kalame ya harchi bahse























