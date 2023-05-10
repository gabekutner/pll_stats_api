import os
from fastapi import FastAPI, HTTPException, status

from load_stats import datastore_player, datastore_team
from utils import id_stat_list

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
    if not players:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')

    return {'players': players}


@app.get("/players/{year}/{season}/{id}")
async def get_one_player(year: int, season: str, id: int) -> dict:

    try:
    	datastore_player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    players = datastore_player.players()

    if not players:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')

    try:
        #check if id exists
        assert 0 <= id <= len(players)
    except AssertionError:  
        return {'message': f'Player with ID: {id} does not exist.'}

    

    player = players[id-1]
    return {'player': player}


@app.get("/players/{year}/{season}/leaders/{stat}")
async def player_stat_leaders(year: int, season: str, stat: str) -> dict:

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
        list = id_stat_list(player=player, stat=stat)
        adjusted_players.append(list)

    if not players:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')

    sorted_players = sorted(adjusted_players, key = lambda d: d['stat'], reverse=True)
    return {'players': sorted_players}


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

    if not teams:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')

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

    if not teams:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')

    try:
        #check if id exists
        assert 0 <= id <= len(teams)
    except AssertionError:  
        return {'message': f'Team with ID: {id} does not exist.'}

    team = teams[id-1]
    return {'team': team}


@app.get("/teams/{year}/leaders/{stat}")
async def team_stat_leaders(year: int, stat: str) -> dict:

    try: 
        datastore_team.init(year)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    adjusted_teams = []
    for team in (teams := datastore_teams.teams()):

        # this is not working, adjust _get_model and id_stat_list for it to work


        list = id_stat_list(team, stat)
        adjusted_teams.append(list)

    if not teams:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')


    sorted_teams = sorted(adjusted_teams, key = lambda d: d['stat'], reverse=True)
    return {'teams': sorted_teams}




