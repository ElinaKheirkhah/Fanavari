#-----------dictionary functions----------------
#{}


#------------------------------------------------------------------------------
#clear

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

profile.clear()
print(profile) #{}

#hame element haye dakhelesho pak mikone khali mishe

#------------------------------------------------------------------------------
#copy

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

profile_copy = profile.copy()
print(profile_copy) #{'firstName': 'Elina', 'lastName': 'Kheirkhah', 'gender': 'female', 'age': 25, 'major': 'industrial design', 'job': 'software developer'}

#ye copy migire azash
#age original taghir kone, in dige taghir nmikone baad az copy shodan

#------------------------------------------------------------------------------
#fromkeys

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }


keys = ["firstName", "lastName", "gender", "age", "major", "job"]

test = profile.fromkeys(keys)
print(test) #{'firstName': None, 'lastName': None, 'gender': None, 'age': None, 'major': None, 'job': None}

keys = ["firstName", "lastName", "gender", "age", "major", "job"]

test = profile.fromkeys(keys, "Unknown")
print(test) #{'firstName': 'Unknown', 'lastName': 'Unknown', 'gender': 'Unknown', 'age': 'Unknown', 'major': 'Unknown', 'job': 'Unknown'}

#az key hayi ke behesh midim yek dictionary jadid misaze
#agar value bedim hameye key ha hamoon value ro migiran
#agar value nadim value hameye key ha None mishe

#------------------------------------------------------------------------------
#get

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

name = profile.get("firstName")
print(name) #Elina

#key ro midi value ro mide

#------------------------------------------------------------------------------
#items

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

print(profile.items()) #dict_items([('firstName', 'Elina'), ('lastName', 'Kheirkhah'), ('gender', 'female'), ('age', 25), ('major', 'industrial design'), ('job', 'software developer')])

#Returns a list containing a tuple for each key value pair

#------------------------------------------------------------------------------
#keys

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

print(profile.keys()) #dict_keys(['firstName', 'lastName', 'gender', 'age', 'major', 'job'])

#Returns a list containing the dictionary's keys
#key ha ro mide

#------------------------------------------------------------------------------
#pop

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

profile.pop("age")

print(profile) #{'firstName': 'Elina', 'lastName': 'Kheirkhah', 'gender': 'female', 'major': 'industrial design', 'job': 'software developer'}

#key ro behesh midi ta un key value ro hazf kone

pop_test = profile.pop("gender")
print(pop_test) #female

#ahaaaa mituni value ro berizi tu ye zarf bedune key

#------------------------------------------------------------------------------
#popitem

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

profile.popitem()
print(profile) #{'firstName': 'Elina', 'lastName': 'Kheirkhah', 'gender': 'female', 'age': 25, 'major': 'industrial design'}
#akharin key value ro khodesh hazf mikone
#tu zarf ham rikhte mishe value sh

#------------------------------------------------------------------------------
#setdefault

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

test = profile.setdefault("age")
print(test) #25

#miad value e un key ke gofti ro mide

test_2 = profile.setdefault("number")
print(test_2) #none
print(profile) #{'firstName': 'Elina', 'lastName': 'Kheirkhah', 'gender': 'female', 'age': 25, 'major': 'industrial design', 'job': 'software developer', 'number': None}

test_3 = profile.setdefault("city" , "tehran")
print(profile) #{'firstName': 'Elina', 'lastName': 'Kheirkhah', 'gender': 'female', 'age': 25, 'major': 'industrial design', 'job': 'software developer', 'number': None, 'city': 'tehran'}
#agar vojoud nadasht miad ezafsh mikone

#------------------------------------------------------------------------------
#update

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

profile.update({"age": 26, "city": "Tehran"})
print(profile) #{'firstName': 'Elina', 'lastName': 'Kheirkhah', 'gender': 'female', 'age': 26, 'major': 'industrial design', 'job': 'software developer', 'city': 'Tehran'}
#agar key vojod dashte bashe value esh ro update mikone
#agar key vojod nadashte bashe key va value ro ezafe mikone
#mitune chand ta key va value ro hamzaman update ya ezafe kone

#------------------------------------------------------------------------------
#values

profile = {
    "firstName" : "Elina" ,
    "lastName" : "Kheirkhah",
    "gender" : "female",
    "age" : 25,
    "major" : "industrial design",
    "job" : "software developer"
    }

print(profile.values()) #dict_values(['Elina', 'Kheirkhah', 'female', 25, 'industrial design', 'software developer'])

#Returns a list of all the values in the dictionary
#valus ha ro mide





