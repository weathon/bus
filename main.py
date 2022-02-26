# pip install "fastapi[all]"
# pip3 install requests --user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests 

origins =["*"]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    r = requests.get('https://gocomo.doublemap.com/map/v2/routes')
    return r.json()