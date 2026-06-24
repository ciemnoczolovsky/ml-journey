#Chapter 6 - Dictionaries Warm up
#Defining dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Using one of dictionary elements
new_points = alien_0['points']
print(f"\nCongrats! You've got {new_points} points!")

#Adding more keys to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Modyfing dictionary values
print(f"\nAlien has {alien_0['color']} color.")

alien_0['color'] = "yellow"
print(f"Alien has {alien_0['color']} color.")

alien_0['speed'] = "fast"
print(f"\nStarting point x-position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'mid':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New vallue for x_position: {alien_0['x_position']}\n")

#Deleting key<->value from a dictionary
del alien_0['points']
print(alien_0)

#Dictionary of simmilar objects
favourite_languages = {
    'patryk': 'python',
    'marek': 'java',
    'tomek': 'java',
    'ania': 'C++'
}

print(f"Patryk's favourite programming language is..."
      f"{favourite_languages['patryk'].title()}.\n")

#Get method
gosia_favourite_language = favourite_languages.get('gosia', 
                                                   'User not found.\n')
print(gosia_favourite_language)

#Chapter6 - Excercise 6.1 - creating list and displaying all values
print("#Chapter6 - Excercise 6.1 - creating list and displaying all values")
my_personal_informations  = {
    'name':'Patryk',
    'surname': 'Ciemnoczolowski',
    'age': 30,
    'city': 'Wroclaw'
}

print(f"Name: {my_personal_informations['name']}")
print(f"Surname: {my_personal_informations['surname']}")
print(f"Age: {my_personal_informations['age']}")
print(f"City: {my_personal_informations['city']}\n")

#Chapter6 - Iterating through dictionary - Warmup
for key,value in my_personal_informations.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

for name,language in favourite_languages.items():
    print(f"{name.title()}\'s favourite programming language is..."
          f"{language.title()}!")

#Chapter6 - Iterating through all of dictionary keys - Warmup - keys()
for name in favourite_languages.keys():
    print(name.title())

friends = ['marek','tomek']
for name in favourite_languages.keys():
    if name in friends:
        language = favourite_languages[name].title()
        print(f"Hello, {name.title()}! I see that your favourite"
              f"programming language is {language}!")
    else:
        print(f"Hello, {name.title()}!")

if 'gustaw' not in favourite_languages.keys():
    print("Gustaw, please fill the form.\n")

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thanks for filling the form!")

print(f"\n{len(favourite_languages)} programming languages have been"
      " chosen in our form:")
for language in sorted(favourite_languages.values()):
    print(language.title())

#Sets
print(f"\nFollowing programming languages have been chosen in our form:")
for language in set(favourite_languages.values()):
    print(language.title())

print("\nSet implementation:")
players = {'Cristiano Ronaldo', 'Lionel Messi', 'Eden Hazard', 'Garteh Bale'}
print(players)

#Chapter 6 - Excercise 6.4 - creating glossary dictionary and iterating
#through it, then adding one more record and iterating again
print('\n#Chapter 6 - Excercise 6.4')
glosary_en_pl = {
    'tuple' : 'krotka',
    'set' : 'zbiór',
    'dictionary' : 'słownik',
    'list comprehension' : 'zagniezdzenie listy',
    'loop' : 'pętla',
}

print(f"Your Python glossary (you have {len(glosary_en_pl)} records):")
for element in glosary_en_pl.keys():
    print(f"\'{element}\' means \'{glosary_en_pl[element]}\'")

glosary_en_pl["library"] = "biblioteka"
print(f"\nYour updated Python glossary"
      f"(you have {len(glosary_en_pl)} records):")
for element in glosary_en_pl.keys():
    print(f"\'{element}\' means \'{glosary_en_pl[element]}\'")

#Chapter 6 - Excercise 6.5 - rivers dictionary
print('\n#Chapter 6 - Excercise 6.5')
rivers = {
    'vistula' : 'poland',
    'amazon' : 'brazil',
    'nile' : 'egypt'
}

for river in rivers.keys():
    print(f"{river.title()} is flowing through {rivers[river].title()}.")

print("All rivers present in a dictionary:")
for river in rivers.keys():
    print(river.title())

print("All countries present in a dictionary:")
for country in rivers.values():
    print(country.title())

#Chapter 6 - Excercise 6.6 - programming language poll
print('\n#Chapter 6 - Excercise 6.6')
chosen_person = ['patryk','marek','elzbieta','krystian']

for person in chosen_person:
    if person not in favourite_languages.keys():
        print(f"Hello, {person.title()}."
              " We encourage you to participate in a poll.")
    else:
        print(f"Hello, {person.title()} "
              "thanks for filling the form for our poll!")

#Chapter 6 - Nesting Warmup
alien_0 = {
    'color': 'green',
    'points': 5
    }
alien_1 = {
    'color': 'yellow',
    'points': 10
    }
alien_2 = {
    'color': 'red',
    'points': 15
    }

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#Chapter 6 - Creating automated dicts in list
aliens = []

for alien_number in range(30):
    new_alien = {
        'color' : 'green',
        'points' : 5,
        'speed' : 'slow'
    }
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:10]:
    alien['color'] = 'yellow'
    alien['points'] = 10,
    alien['speed'] = 'medium'

for alien in aliens:
    print(alien)

#Chapter 6 - lists in dict
pizza = {
    'crust' : 'thin',
    'toppings' : ['mushrooms','double cheese']
}

print(f"You've just ordered pizza on {pizza['crust']} crust"
      f"with following toppings {pizza['toppings']}.")

favourite_languages = {
    'patryk': ['python','javascript'],
    'marek': ['c'],
    'tomek': ['java','php','rust'],
    'ania': ['C++','haskell'],
}

for name, languages in favourite_languages.items():
    print(f"\nUlubione języki programowania uzytkownika {name.title()} are:")
    for language in languages:
        print(f"\t{language.title()}")

#Chapter 6 - Excercise 6.7
print("Chapter 6 - Excercise 6.7")
pciemnoczolowski  = {
    'name':'Patryk',
    'surname': 'Ciemnoczolowski',
    'age': 30,
    'city': 'Wroclaw'
}

mcybulski = {
    'name':'Marek',
    'surname': 'Cybulski',
    'age': 30,
    'city': 'Puszczykowo'
}

akrokosz = {
    'name':'Adrian',
    'surname': 'Krokosz',
    'age': 34,
    'city': 'Siekierki'
}

people = [pciemnoczolowski,mcybulski,akrokosz]

for person in people:
    print(person['name'])
    print(person['surname'])
    print(person['age'])
    print(person['city']+"\n")

#Chapter 6 - Excercise 6.8
print("Chapter 6 - Excercise 6.8")
aura = {
    'type' : 'dog',
    'name' : 'aura',
    'age (in yrs)' : '0.25',
    'weight (in kg)' : '4.5',
    'owner' : 'Patryk'
}

kicia = {
    'type' : 'cat',
    'name' : 'kicia',
    'age (in yrs)' : '8',
    'weight (in kg)' : '3.27',
    'owner' : 'Gosia'
}

gucio = {
    'type' : 'bird',
    'name' : 'gucio',
    'age (in yrs)' : '15',
    'weight (in kg)' : '0.15',
    'owner' : 'Rafał'
}

pets = [aura,kicia,gucio]

for pet in pets:
    for key,value in pet.items():
        print(f"{key.title()}: {value.title()}")
    print("\n")

#Chapter 6 - Excercise 6.9
print("#Chapter 6 - Excercise 6.9")
favourite_places = {
    'Patryk' : ['Riga','London','Sevilla'],
    'Adrian' : ['Buenos Aires','Singapore','Rome'],
    'Natalia' : ['Vietnam','Costa Rica','Australia']
}

for person,places in favourite_places.items():
    print(f"{person.title()}\'s favourite places:")
    for place in places:
        print(f"\t{place}")

#Chapter 6 - Excercise 6.10
print("#Chapter 6 - Excercise 6.10")
