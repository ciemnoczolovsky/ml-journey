def nominated_players(*players):
    """Printing players nominated to Balon d'Or"""
    print('\nFollowing players have been nominated to the Balon d\'or:')
    for player in players:
        print(f"\t{player}")

def calculate_match_points(scored, conceded):
    """Calculating match points returning 3, 1, or 0"""
    if scored > conceded:
        return 3
    elif scored < conceded:
        return 0
    else:
        return 1
    
def build_team_stats(team_name, matches):
    """Building team stats based on provided data: points, goals for,
    goals against, goals ratio."""
    points = 0
    goals_for = 0
    goals_against = 0
    for match in matches:
        if match.get('home_team') == team_name:
            team_goals = match.get('home_goals')
            opponent_goals = match.get('away_goals')
        else:
            team_goals = match.get('away_goals')
            opponent_goals = match.get('home_goals')
        points += calculate_match_points(team_goals, opponent_goals)
        goals_for += team_goals
        goals_against += opponent_goals
    team_details = {
        'team_name': team_name,
        'points': points,
        'goals_for': goals_for,
        'goals_against': goals_against,
        'goal_difference': goals_for - goals_against
    }

    return team_details