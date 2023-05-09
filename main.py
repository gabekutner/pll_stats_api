import os
from fastapi import FastAPI, HTTPException, status

from load_stats import datastore_player, datastore_team
import utils

app = FastAPI()


@app.get("/players/{year}/{season}")
async def get_all_players(year: int, season: str) -> dict:

    # check if data for year exists

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
async def get_one_player(year: int, season: str, id: int) -> dict:

    # check if data for year exists

    try:
    	datastore_player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    try:
        #check if id exists
        assert 0 <= id <= len(players := datastore_player.players())
    except AssertionError:  
        return {'message': f'Player with ID: {id} does not exist.'}

    player = players[id-1]
    return {'player': player}


@app.get("/players/{year}/{season}/leaders/{stat}")
async def player_stat_leaders(year: int, season: str, stat: str) -> dict:
    
    # check if data for year exists

    try:
        datastore_player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    adjusted_players = []
    for player in (players := datastore_player.players()):
        list = utils.id_stat_list(player, stat)
        adjusted_players.append(list)

    sorted_players = sorted(adjusted_players, key = lambda d: d['stat'], reverse=True)
    return {'players': sorted_players}


@app.get("/teams/{year}")
async def get_all_teams(year: int) -> dict:

    # check if data for year exists

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

    # check if data for year exists

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


@app.get("/teams/{year}/leaders/{stat}")
async def team_stat_leaders(year: int, stat: str) -> dict:

    pass






