# pip install "fastapi[all]"
# pip3 install requests --user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    requests.get('https://gocomo.doublemap.com/map/v2/stops')
    return r.json()