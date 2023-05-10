from load_stats import player, team

# Initialize
player.init()
team.init()

# Get all
players = player.get_players()
teams = team.get_teams()

# Get one
player = player.get_player(id=5)
team = team.get_team(id=5)