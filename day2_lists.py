#Warmup
print("#Warmup")
managers = ['Jose Mourinho', 'Pep Guardiola', 'Jurgen Klopp', 'Carlo Ancelotti']
print(f"The best manager in the history is {managers[0]}.")
print(f"{managers[-1]} is a decent manager.")

#Chapter 3 - Excercise 3.1
print("\n#Excercise3.1")
friends = ['Gruby','Kefir','Hencel','Larson']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

#Chapter 3 - Excercise 3.2
print("\n#Excercise3.2")
print(f"Hello, {friends[0]}!")
print(f"Hello, {friends[1]}!")
print(f"Hello, {friends[2]}!")
print(f"Hello, {friends[3]}!")

#Chapter 3 - Excercise 3.3
print("\n#Excercise3.3")
vehicles = ['Car','Motorbike','Bicycle']
print(f"{vehicles[0]} is very convienient vehicle. I have Mazda CX3, and I'm very happy about this car.")
print(f"{vehicles[1]} is not my cup of tea. I'm too afraid about any accidents.")
print(f"{vehicles[2]} is my favourite vehicle in the city. It's good for my health and sometimes you would get faster to the point, that with car.")

#Chapter 3 - Excercise 3.4
print("\n#Excercise3.4")
guests_list = ["Harry Kane","John Paul II","Marek Cybulski"]
print(f"Hello, {guests_list[0]}, I would like to invite you to my party!")
print(f"Sup, {guests_list[1]}, get ready to the party, You are invited!")
print(f"Oi, {guests_list[2]}, party. Friday. You have to be there!")

#Chapter 3 - Excercise 3.5
print("\n#Excercise3.5")
print(f"Invited guests: {guests_list}")
print(f"Unfortunately, {guests_list[1]} is unavailable.")
guests_list[1]="Michał Kubaczyk"
print(f"Hello, {guests_list[0]}, I would like to iinvite you to my party!")
print(f"Sup, {guests_list[1]}, get ready to the party, You are invited!")
print(f"Oi, {guests_list[2]}, party. Friday. You have to be there!")

#Chapter 3 - Excercise 3.6
print("\n#Excercise3.6")
print("There is bigger room in the restaurant. Let's invite more people.")
guests_list.insert(0,"Johnny Bravo")
guests_list.insert(2, "Neil Armstrong")
guests_list.append("Bill Gates")
print(f"Updated guests list: {guests_list}")

#Chapter 3 - Excercise 3.7
print("\n#Excercise3.7")
print("Oooopsie. There is table just for 2 guests. We need to reduce list.")
removed_guest=guests_list.pop()
print(f"Hey, {removed_guest}. Unfortunately, restaurant made mistake and there is no table for us. Let's meet another time. Thanks for understanding!")
removed_guest=guests_list.pop()
print(f"Hey, {removed_guest}. Unfortunately, restaurant made mistake and there is no table for us. Let's meet another time. Thanks for understanding!")
removed_guest=guests_list.pop()
print(f"Hey, {removed_guest}. Unfortunately, restaurant made mistake and there is no table for us. Let's meet another time. Thanks for understanding!")
removed_guest=guests_list.pop()
print(f"Hey, {removed_guest}. Unfortunately, restaurant made mistake and there is no table for us. Let's meet another time. Thanks for understanding!")
print(f"Hey, {guests_list[0]}, due to restaurant mistake, we have table just for 3 people. We will meet with {guests_list[1]}. See ya!")
print(f"Sup, {guests_list[1]}, restaurant messed up with tables and we have table just for 3 people. See you with {guests_list[0]}.")
del guests_list[0]
del guests_list[0]
print(f"Current guests list: {guests_list}")

#Chapter 3 - Warmup 2
print("\n#Warmup 2")
guests_list = ["Harry Kane","John Paul II","Marek Cybulski"]
print(guests_list)
guests_list.sort()
print(guests_list)
guests_list.sort(reverse=True)
print(guests_list)

#Chapter 3 - Excercise 3.8
print("\n#Excercise3.8")
dream_places = ["Argentina", "Vietnam", "Costa Rica", "USA", "Australia"]
print(f"Dream places: {dream_places}")
print(f"Dream places (temporary A-Z sort): {sorted(dream_places)}")
print(f"Dream places: {dream_places}")
dream_places.reverse()
print(f"Dream places (reversed): {dream_places}")
dream_places.reverse()
print(f"Dream places (reversed again): {dream_places}")
dream_places.sort()
print(f"Dream places (sorted A-Z): {dream_places}")
dream_places.sort(reverse=True)
print(f"Dream places (sorted Z-A): {dream_places}")

#Chapter 3 - Excercise 3.9
print("\n#Excercise3.9")
guests_list = ["Harry Kane","John Paul II","Marek Cybulski"]
print(f"Number of guests: {len(guests_list)}")


