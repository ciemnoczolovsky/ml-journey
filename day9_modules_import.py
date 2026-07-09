#import football_modules // general import
#from football_modules import nominated_players // import of function
from football_modules import *
#alias for function ^ alias for whole module: import function as smth
#import of all functions: from football_modules import *

#Claude excercise 1
match_points = calculate_match_points(3,2)
print(match_points)

match_points = calculate_match_points(0,2)
print(match_points)

match_points = calculate_match_points(2,2)
print(match_points)

#Claude excercise 2
matches = [
    {
        'home_team': 'Tottenham',
        'away_team': 'Arsenal',
        'home_goals': 3,
        'away_goals': 1
    },
    {
        'home_team': 'Newcastle',
        'away_team': 'Tottenham',
        'home_goals': 1,
        'away_goals': 2
    },
    {
        'home_team': 'Tottenham',
        'away_team': 'Leeds',
        'home_goals': 4,
        'away_goals': 1
    },
    {
        'home_team': 'Chelsea',
        'away_team': 'Tottenham',
        'home_goals': 3,
        'away_goals': 4
    },
]
team_stats = build_team_stats("Tottenham",matches)
print(team_stats)