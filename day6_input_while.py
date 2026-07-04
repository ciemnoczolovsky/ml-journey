 #Chapter 7 - Input function - WarmUp
message = input("What is your favourite football team? ")
print(f"{message}? Interesting choice!")

#Using variable to use it as a prompt
prompt = "It's your time to shine!"
prompt += "\nWhat is your score prediction for Arsenal vs Chelsea? "
prediction = input(prompt)
print(f"Your prediction for this match is {prediction}")

#int input
transfer_offer = int(input("How much do you offer for Harry Kane? "))
if transfer_offer > 100000000:
    print("Deal done")
elif transfer_offer > 80000000:
    print("Too low. We want 100M!")
else:
    print("Are you joking me?")

#modulo
number = int(input("Give me number, I'll tell you if it's even, or odd."))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#While loop - WarmUp
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

prompt = "Tell me about your favourite football players."
prompt += "\nTo finish program write \'finish\': "
favourite_player = ""
#iterations = 0
#while favourite_player != 'finish':
#    favourite_player = input(prompt)
#    if iterations % 2 == 0 and favourite_player != 'finish':
#        print(f"{favourite_player}? Nice choice!")
#    elif favourite_player != 'finish':
#        print(f"{favourite_player}? Really? He is not that good.")
#    iterations += 1

#Flag variable
favourite_player = ""
iterations = 0
active = True
while active:
    favourite_player = input(prompt)
    if favourite_player == 'finish':
        active = False
    elif iterations % 2 == 0:
        print(f"{favourite_player}? Nice choice!")
    else:
        print(f"{favourite_player}? Really? He is not that good.")
    iterations += 1

#Claude Excercises
#Excercise 7.1 - Yellow Cards
players = []
player_input = ""
prompt_player = "Enter player's name (if you want to finish type \'finish\'): "
prompt_yellow_cards = "Enter number of yellow cards: "
yellow_cards_count = 0
while True:
    player_input = input(prompt_player)
    if player_input == 'finish':
        break
    yellow_cards = input(prompt_yellow_cards)

    if not yellow_cards.isDigit():
        print("You need to provide positive number!")
        continue
    yellow_cards_count += int(yellow_cards)
    player = {
        'name': player_input,
        'yellow_cards': int(yellow_cards)}
    players.append(player)

print(f"Total number of yellow cards in Premier League: {yellow_cards_count}"
      f"\nTotal number of players in database: {len(players)}")

#Excercise 7.2 - Final results list
results = []
quit_flag = True
prompt_home_team = "Please, provide match score (to quit type \'q\')"
prompt_home_team += "\nHow many goals has scored home team? "
prompt_away_team = "How many goals has scored away team? "
match_number = 1
while quit_flag:
    home_team_goals = input(prompt_home_team)
    if home_team_goals != 'q':
        away_team_goals = input(prompt_away_team)
        if away_team_goals != 'q':
            result = {
                'home': int(home_team_goals),
                'away': int(away_team_goals)
            }
            results.append(result)
        else:
            quit_flag = False
    else:
        quit_flag = False

print("\n All results:")
for result in results:
    print(f"Match#{match_number}: {result['home']}:{result['away']}")
    match_number += 1

#Excercise 7.3 - Break / continue
shots_list = []
prompt = "How many shots have been in this match? (Write \'stop\' to quit): "
while True:
    shots_number = input(prompt)
    if shots_number == 'stop':
        break
    elif not shots_number.isdigit():
        print("You need to provide positive number!")
        continue
    else:
        shots_list.append(int(shots_number))
print(shots_list)

#Chapter 7 - moving elements from one list to another
transfer_targets = ['Savinho','Cody Gakpo','Sandro Tonali','Alex Scott',
                    'Andy Robertson','Marcos Senesi','Martin Dubravka']
current_squad = ['Guilermo Vicario', 'Micky Van de Ven','Connor Gallagher',
                 'Dominic Solanke']
prompt = "Have this player been transfered to your team? (y/n) "
while transfer_targets:
    current_player = transfer_targets.pop()
    final_decision = input(f"{current_player}. {prompt}")
    
    if final_decision == 'y':
        current_squad.append(current_player)
        print(f"{current_player} has been added to the current squad.")
    else:
        print(f"Transfer talks for {current_player} failed.")

print("\nUpdated squad:")
for player in current_squad:
    print(player)

#Chapter 7 - removing elements from the list in while loop
current_squad = ['Guilermo Vicario', 'Harry Kane', 'Micky Van de Ven',
                 'Connor Gallagher', 'Harry Kane', 'Dominic Solanke']

while 'Harry Kane' in current_squad:
    current_squad.remove('Harry Kane')
print(current_squad)

#Excercise 7.4 - moving players from bench to first squad or not selected squad
current_squad = ['Harry Kane', 'Heung min-Son','Lucas Moura','Moussa Dembele']
bench = ['Dele Alli','Erik Lamela','Vincent Janssen','Lucas Bergvall']
not_selected_players = []
prompt = "Would you like to have him on the pitch? (y/n)"

print(f"Current squad: {current_squad}")
while bench:
    current_player = bench.pop()
    managers_choice = input(f"{current_player}. {prompt}")
    if managers_choice.lower() == 'y':
        current_squad.append(current_player)
    else:
        not_selected_players.append(current_player)

print(f"Current squad: {current_squad}")
print(f"Not selected players: {not_selected_players}")

#Excercise 7.5 - building ligue table
teams = {}
team_prompt = "What team would you like to add? "
points_prompt = "How many point's they've got? "

while True:
    team = input(team_prompt)
    if team == "":
        break

    points = input(points_prompt)
    if not points.isdigit():
        print("You need to provide positive number!")
    elif team in teams:
        print(f"{team} is already added to the League."
               f" Added {points} points to them.")
        teams[team] += int(points)
    else:
        teams[team] = int(points)

for team,points in teams.items():
    print(f"{team} : {points} pts.")

