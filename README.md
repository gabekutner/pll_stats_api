# Pll Stats API
An api for PLL player and team statistics.

Data from ```https://stats.premierlacrosseleague.com/```

**main.py** - FastAPI api

**api.py** - Shows how to use load_stats package

### Usage
```Python
from load_stats import datastore_player, datastore_team

year = 2022
season = 'regular' #regular season

datastore_player.init(year, season)
datastore_team.init(year)

players = datastore_player.players()
teams = datastore_team.teams()

```
