# pip install "fastapi[all]"
# pip3 install requests --user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests 
from fastapi.responses import HTMLResponse, FileResponse


origins =["*"]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/routes")
async def root():
    r = requests.get('https://gocomo.doublemap.com/map/v2/routes')
    return r.json()


@app.get("/buses")
async def root():
    r = requests.get('https://gocomo.doublemap.com/map/v2/buses')
    return r.json()

#return STATIC html
@app.get("/", response_class=HTMLResponse)
async def read_items():
    f = open("index.html", "r")
    fileContent = f.read()
    f.close()
    return fileContent


@app.get("/audio", response_class=FileResponse)
async def main():
    return "audio.mp3"