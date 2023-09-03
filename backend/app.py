import random
from json import load

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]# your origins
data = load(open("faal.json", "r"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/faal/")
async def get_faal():
    faal = random.choice(data)
    return {"faal": faal}

