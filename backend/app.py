import random
from json import load

from fastapi import FastAPI

app = FastAPI()

data = load(open('faal.json', 'r'))

@app.get('/')
async def index():
    faal = random.choice(data)
    return {"faal":faal}