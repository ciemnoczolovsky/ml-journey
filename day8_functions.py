#Functions Warm-up
def greet_user():
    """Printing simple greeting"""
    print("Hello")

greet_user()

def greet_user_with_arg(username):
    """Printing simple greeting with argument"""
    print(f"Hello, {username}!")

greet_user_with_arg('Patryk')

#Function with many arguments
def player_details(name, age, club, foot):
    print("Player detail's:" \
          f"\n\tName: {name}"
          f"\n\tAge: {age}"
          f"\n\tClub: {club}"
          f"\n\tFoot: {foot}")

player_details('Harry Kane',32,'Bayern Munich','Right')
player_details('James Maddison',31,'Tottenham Hotspur','Right')

#Function with defined parameters
player_details(name='Jude Bellingham',club='Real Madrid',age=24,foot='right')

#Function with default value
def player_details_default(name,age,club,foot='right'):
    print("Player detail's:" \
          f"\n\tName: {name}"
          f"\n\tAge: {age}"
          f"\n\tClub: {club}"
          f"\n\tFoot: {foot}")

player_details_default('Zbigniew Boniek',63,'Juventus')

#Return
def get_formatted_name(first_name, last_name):
    """Returns formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

player = get_formatted_name('harry','KaNe')
print(player)

def get_formatted_name_optional(first_name,last_name,middle_name=""):
    """Returns formatted full name with optional middle name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name.title()

player_one = get_formatted_name_optional('Dele','aLLI')
player_two = get_formatted_name_optional('Kroupi','Junior','Eli')

print(f"{player_one}\n{player_two}")

#Returning dictionary
def build_football_team(team_name,founded_date,market_value=None):
    """Returning dictionary of provided arguments"""
    team = {
        'team_name': team_name,
        'founded': founded_date}
    if market_value:
        team['market_value'] = market_value
    return team

football_team = build_football_team('Tottenham Hotspur',1882,3500000000)
print(football_team)

#Using functions and loops
while True:
    print("\nProvide player details below, or write \'q\' to quit.")
    first_name = input("\tFirst name: ")
    if first_name == 'q':
        break
    last_name = input("\tLast name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print(f"{formatted_name} is a decent player!")

#Chapter 8 - Excercise 8.7/8.8
football_teams = []
while True:
    print("Add football team, or type \'q\' to quit.")
    team_name = input("Team name: ")
    if team_name == 'q':
        break

    founded_date = input("Founded date: ")
    if founded_date == 'q':
        break

    market_value = input("Provide market value or write \'s\' to skip: ")
    if market_value == 'q':
        break
    elif market_value != 's':
        football_teams.append(build_football_team(team_name, founded_date, 
                                            market_value))
    else:
        football_teams.append(build_football_team(team_name, founded_date))

print(football_teams)

#List as function argument
def print_watchlist(players):
    """Inform about players on transfer watchlist"""
    for player in players:
        message = f"{player} is on the transfer watchlist."
        print(message)

transfer_watchlist = ['Harry Kane', 'Dele Alli', 'Heung-min Son', 'Lucas']
print_watchlist(transfer_watchlist)

#Modyfing list without function
completed_transfers = []

while transfer_watchlist:
    negotiated_player = transfer_watchlist.pop()
    print(f"Transfer talks for {negotiated_player} are in progress...")
    completed_transfers.append(negotiated_player)

print('Following players have been signed up by Spurs:')
for player in completed_transfers:
    print(f"\t*{player}")

#Modyfing list with function
def negotiate_player(transfer_watchlist,completed_transfers):
    """Simulating transfer talks"""
    while transfer_watchlist:
        negotiated_player = transfer_watchlist.pop()
        print(f"Transfer talks for {negotiated_player} are in progress...")
        completed_transfers.append(negotiated_player)

def show_completed_tranfers(completed_transfers):
    """Presenting completed transfers"""
    print('Following players have been signed up by Spurs:')
    for player in completed_transfers:
        print(f"\t*{player}")

transfer_watchlist = ['Harry Kane', 'Dele Alli', 'Heung-min Son', 'Lucas']
completed_transfers = []

negotiate_player(transfer_watchlist,completed_transfers)
show_completed_tranfers(completed_transfers)

#To pass copy of the list use this argument transfer_watchlist[:]

#Flexible number of arguments inside function
def nominated_players(*players):
    """Printing players nominated to Balon d'Or"""
    print('\nFollowing players have been nominated to the Balon d\'or:')
    for player in players:
        print(f"\t{player}")

nominated_players('Michael Olise','Harry Kane','Kylian Mbappe','Lionel Messi')

#Returning provided arguments as key-value
def build_player(first_name, last_name, **user_info):
    """Build dictionary containing provided informations abour player"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

player_profile = build_player('Vini','Jr',foot='right',team='Real Madrid')
print(player_profile)