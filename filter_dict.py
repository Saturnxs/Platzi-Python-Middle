matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

# Filtering the matches list and returning a list of matches where the home team won.
winner_home_teams = list(filter(lambda match: match['home_team_result'] == 'Win', matches))

print(list(winner_home_teams))
# [
#     {
#         'home_team': 'Bolivia',
#         'away_team': 'Uruguay',
#         'home_team_score': 3,
#         'away_team_score': 1,
#         'home_team_result': 'Win'
#     },
#     {
#         'home_team': 'Ecuador',
#         'away_team': 'Venezuela',
#         'home_team_score': 5,
#         'away_team_score': 0,
#         'home_team_result': 'Win'
#     }
# ]