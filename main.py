from fastapi import FastAPI, APIRouter, HTTPException, status
import datastorage, utils

app = FastAPI()


@app.get("/players/{year}/{season}")
async def get_all_players(year: int, season: str) -> dict:

    try:
        datastorage.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    players = datastorage.players()
    return {'players': players}


@app.get("/players/{year}/{season}/{id}")
async def get_one_player(year:int, season: str, id: int) -> dict:
    
    try:
        datastorage.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    players = datastorage.players()

    try:
        #check if id exists
        assert 0 <= id <= len(players)
    except AssertionError:  
        return {'message': f'ID with {id} does not exist.'}


    player = players[id-1]
    return {'player': player}


@app.get("/players/{year}/{season}/leaders/{stat}")
async def stat_leaders(year: int, season: str, stat: str) -> dict:
    
    try:
        datastorage.init(year, season)

    except UnboundLocalError:
        return {
            'message': 'url configuration error',
            'correct url config': '/players/year/season',
            'ex': '/players/2022/regular'
        }

    players = datastorage.players()

    p=[]
    for player in players:
        list = utils.id_stat_list(player, stat)
        p.append(list)

    x = sorted(p, key = lambda d: d['stat'], reverse=True)

    return {'players': x}







