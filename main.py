from fastapi import FastAPI, APIRouter, HTTPException, status
import datastorage

app = FastAPI()


# get all players
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

# get player by id
@app.get("/players/{id}")
async def get_one_player(id: int) -> dict:
    pass


# get the stat description / definition
@app.get("/stats/definition/{stat}")
async def get_one_player(stat: str) -> dict:
    pass

