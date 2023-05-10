import os
from fastapi import FastAPI, HTTPException, status

from load_stats import player, team
from utils import id_stat_list

app = FastAPI()


@app.get("/players/{year}/{season}")
async def get_all_players(year: int, season: str) -> dict:

    try:
    	player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    players = player.get_players()
    if not players:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')

    return {'players': players}


@app.get("/players/{year}/{season}/{id}")
async def get_one_player(year: int, season: str, id: int) -> dict:

    try:
    	player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    one_player = player.get_player(id=id)

    if not one_player:
        raise HTTPException(status_code=404, detail=f'Player with id: {id} does not exist.')

    return {'player': one_player}


@app.get("/players/{year}/{season}/leaders/{stat}")
async def player_stat_leaders(year: int, season: str, stat: str) -> dict:

    try:
        player.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    adjusted_players = []
    for one_player in (players := player.get_players()):
        list = id_stat_list(player=one_player, stat=stat)
        adjusted_players.append(list)

    if not players:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')

    sorted_players = sorted(adjusted_players, key = lambda d: d['stat'], reverse=True)
    return {'players': sorted_players}


@app.get("/teams/{year}")
async def get_all_teams(year: int) -> dict:

    try:
        team.init(year)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    teams = team.get_teams()

    if not teams:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')

    return {'teams': teams}


@app.get("/teams/{year}/{id}")
async def get_one_team(year: int, id: int) -> dict:

    try:
        team.init(year)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    one_team = team.get_team(id=id)

    if not one_team:
        raise HTTPException(status_code=404, detail=f'The team with id: {id} does not exist..')

    return {'team': one_team}


@app.get("/teams/{year}/leaders/{stat}")
async def team_stat_leaders(year: int, stat: str) -> dict:

    try: 
        team.init(year)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    adjusted_teams = []
    for one_team in (teams := team.get_teams()):

        # this is not working, adjust _get_model and id_stat_list for it to work


        list = id_stat_list(one_team, stat)
        adjusted_teams.append(list)

    if not teams:
        raise HTTPException(status_code=404, detail=f'Stats for {year} does not exist.')


    sorted_teams = sorted(adjusted_teams, key = lambda d: d['stat'], reverse=True)
    return {'teams': sorted_teams}




