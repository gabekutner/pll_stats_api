from load_stats import datastore_player, datastore_team

datastore_player.init()
datastore_team.init()

players = datastore_player.players()
teams = datastore_team.teams()