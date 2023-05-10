# Pll Stats API
An api for PLL player and team statistics.

Data from [https://stats.premierlacrosseleague.com/](https://stats.premierlacrosseleague.com/)



### Usage
```Python
from load_stats import player, team

year = 2022
season = 'regular' #regular season

player.init(year, season)
team.init(year)

# Get all
players = player.get_players()
teams = team.get_teams()

# Get one
player = player.get_player(id=1)
team = team.get_team(id=1)


```
