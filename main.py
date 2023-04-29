from fastapi import FastAPI, APIRouter, HTTPException, status
import datastorage

app = FastAPI()


@app.get("/{year}/{season}/players")
async def get_all_players(year: int, season: str) -> dict:
    """ Get all players
    """
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


@app.get("/{year}/{season}/players/{id}")
async def get_one_player(year:int, season: str, id: int) -> dict:
    """ 
    """
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
        assert 0 <= id <= len(players)
    except AssertionError:  
        return {'message': f'ID with {id} does not exist.'}

    player = players[id-1]
    return {'player': player}

