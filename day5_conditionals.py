#Chapter 5 - Conditionals WarmUp
player = 'Kane'
print(f"player == \'Kane\' -> {player == 'Kane'}")
print(f"player == \'kane\' -> {player == 'kane'}")
print(f"player.lower() == \'kane\' -> {player.lower() == 'kane'}\n")

referee = 'Michael Oliver'
if referee.lower() != 'howard webb':
    print("Howard Web was supposed to be a referee"
          f" in this match, not {referee.title()}.\n")
    
goals_record = 42
players_goals = {
    'Harry Kane': 35,
    'Erling Haaland': 43,
    'Mohamed Salah': 42,
    'Eden Hazard': 25
}

for player, goals in players_goals.items():
    if goals > goals_record:
        print(f"{player} has beaten Premier League goals record "
              f"with {goals} goals!")
    elif goals == goals_record:
        print(f"{player} has equaled Premier League goals record "
              f"with {goals} goals!")
    else:
        print(f"{player} hasn\'t beaten Premier League goals record "
              f"with {goals} goals!")

print("\n")
players_dict = {
    'Harry Kane':{
        'age': 34,
        'played_in_pl_u21': True,
    },
    'Estevao':{
        'age': 17,
        'played_in_pl_u21': True,
    },
    'Archie Gray':{
        'age': 21,
        'played_in_pl_u21': True,
    },
    'Martin Dubravka':{
        'age': 32,
        'played_in_pl_u21': False,
    }
}

for player, player_info in players_dict.items():
    if player_info['age'] <= 21 and player_info['played_in_pl_u21']:
        print(f"{player} is currently on homegrown status")
    elif player_info['age'] <= 21 or player_info['played_in_pl_u21']:
        print(f"{player} used to have homegrown status.")
    else:
        print(f"{player} never had homegrown status.")


if 'Eden Hazard' in players_dict.keys():
    print("\nEden Hazard is present in players dictionary")
else:
    print("\nEden Hazard is not present in players dictionary")

if 'Harry Kane' in players_dict.keys():
    print("Harry Kane is present in players dictionary")
else:
    print("Harry Kane is not present in players dictionary")

#Claude excercises
#Excercise 5.1 - check who win
#Scenario 1
home_team = {
    'name': 'Manchester United',
    'goals': 2
}

away_team = {
    'name': 'Manchester City',
    'goals': 3
}
print("\n")
if home_team['goals'] > away_team['goals']:
    print(f"{home_team['name']} won the match {home_team['goals']}:"
          f"{away_team['goals']}!")
elif away_team['goals'] > home_team['goals']:
    print(f"{away_team['name']} won the match {away_team['goals']}:"
          f"{home_team['goals']}!")
else:
    print(f"It's a {home_team['goals']}:{away_team['goals']} tie between"
          f"{home_team['name']} and {away_team['name']}.")
#Scenario 2
home_team = {
    'name': 'Manchester United',
    'goals': 3
}

away_team = {
    'name': 'Manchester City',
    'goals': 2
}
print("\n")
if home_team['goals'] > away_team['goals']:
    print(f"{home_team['name']} won the match {home_team['goals']}:"
          f"{away_team['goals']}!")
elif away_team['goals'] > home_team['goals']:
    print(f"{away_team['name']} won the match {away_team['goals']}:"
          f"{home_team['goals']}!")
else:
    print(f"It's a {home_team['goals']}:{away_team['goals']} tie between"
          f"{home_team['name']} and {away_team['name']}.")
#Scenario 3
home_team = {
    'name': 'Manchester United',
    'goals': 2
}

away_team = {
    'name': 'Manchester City',
    'goals': 2
}
print("\n")
if home_team['goals'] > away_team['goals']:
    print(f"{home_team['name']} won the match {home_team['goals']}:"
          f"{away_team['goals']}!")
elif away_team['goals'] > home_team['goals']:
    print(f"{away_team['name']} won the match {away_team['goals']}:"
          f"{home_team['goals']}!")
else:
    print(f"It's a {home_team['goals']}:{away_team['goals']} tie between"
          f"{home_team['name']} and {away_team['name']}.")
    
#Excercise 5.2 - check cards
players_cards = {
    'Moises Caicedo': 2,
    'Casemiro': 1,
    'Erling Haaland': 0,
    'Ngolo Kante': 1
}
print("\n")
for player,cards in players_cards.items():
    if cards >= 2:
        print(f"{player} got red card!")
    elif cards == 1:
        print(f"{player} need to be careful. He's just got yellow card!")
    else:
        print(f"{player} is completely safe. He hasn't got any cards so far.")

#Excercise 5.3 - check point zones
team_points = {
    'Tottenham': 38,
    'Arsenal': 82,
    'Machester City': 102,
    'Liverpool': 58,
    'Cheslea': 67,
    'Bournemouth': 45,
    'Newcastle': 55,
    'West Ham': 22
}
print("\n")
for team,points in team_points.items():
    if points >= 80:
        print(f"{team.title()} is in champions zone")
    elif points >= 65:
        print(f"{team.title()} is in european leagues battle zone")
    elif points >= 40:
        print(f"{team.title()} is in mid table zone")
    else:
        print(f"{team.title()} is in relegation battle zone")

#Excercise 5.4 - match squad
squad_list = ['Hugo Lloris','Danny Rose','Toby Alderweireld','Jan Vertonghen',
              'Kyle Walker','Moussa Dembele','Victor Wanyama',
              'Christian Eriksen','Dele Alli','Heung Son-min','Harry Kane']
players_to_be_checked = ['Harry Kane', 'Dominic Solanke', 'Erik Lamela', 
                         'Kyle Walker']
print("\n")
for player in players_to_be_checked:
    if player not in squad_list:
        print(f"{player} is not in the match squad.")
    else:
        print(f"{player} is in the match squad.")