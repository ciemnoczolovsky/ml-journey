def nominated_players(*players):
    """Printing players nominated to Balon d'Or"""
    print('\nFollowing players have been nominated to the Balon d\'or:')
    for player in players:
        print(f"\t{player}")

def calculate_match_points(home_goals, away_goals):
    """Calculating match points returning 3,1, or 0"""
    if home_goals > away_goals:
        return 3
    elif home_goals < away_goals:
        return 0
    else:
        return 1
    
def build_team_stats(team_name, matches):
    """Builiding team stats based on provided data: points, goals for,
    goals against, goals ratio."""
    points = 0
    goals_for = 0
    goals_against = 0
    for match in matches:
        if match.get('home_team') == team_name:
            team_goals = match.get('home_goals')
            oponent_goals = match.get('away_goals')
        else:
            team_goals = match.get('away_goals')
            oponent_goals = match.get('home_goals')
        points += calculate_match_points(team_goals,oponent_goals)
        goals_for += team_goals
        goals_against += oponent_goals
    goals_ratio = f"{goals_for}:{goals_against}"
    team_details = {
        'team_name': team_name,
        'points': points,
        'goals_for': goals_for,
        'goals_against': goals_against,
        'goals_ratio': goals_ratio
    }

    return team_details