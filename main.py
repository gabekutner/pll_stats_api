from fastapi import FastAPI, APIRouter, HTTPException, status
from load_stats import datastore_player, datastore_team
import utilities


app = FastAPI()


@app.get("/players/{year}/{season}")
async def get_all_players(year: int, season: str) -> dict:

    try:
    	datastore_player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    players = datastore_player.players()
    return {'players': players}


@app.get("/players/{year}/{season}/{id}")
async def get_one_player(year:int, season: str, id: int) -> dict:
    
    try:
    	datastore_player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    players = datastore_player.players()

    try:
        #check if id exists
        assert 0 <= id <= len(players)
    except AssertionError:  
        return {'message': f'Player with ID: {id} does not exist.'}


    player = players[id-1]
    return {'player': player}


@app.get("/players/{year}/{season}/leaders/{stat}")
async def stat_leaders(year: int, season: str, stat: str) -> dict:
    
    try:
        datastore_player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    players = datastore_player.players()

    p=[]
    for player in players:
        list = utilities.id_stat_list(player, stat)
        p.append(list)

    x = sorted(p, key = lambda d: d['stat'], reverse=True)
    return {'players': x}


@app.get("/teams/{year}")
async def get_all_teams(year: int) -> dict:

    try:
        datastore_team.init(year)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    teams = datastore_team.teams()
    return {'teams': teams}

@app.get("/teams/{year}/{id}")
async def get_one_team(year: int, id: int) -> dict:

    try:
        datastore_team.init(year)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    teams = datastore_team.teams()

    try:
        #check if id exists
        assert 0 <= id <= len(teams)
    except AssertionError:  
        return {'message': f'Team with ID: {id} does not exist.'}


    team = teams[id-1]
    return {'team': team}





