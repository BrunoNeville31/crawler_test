from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crawler import calculate_khamis_roche

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/calculate")
async def calculate_height(  
  cage: str,
  csex: str,
  cheightmeter: str,
  ckg: str,
  mcheightmeter: str,
  fcheightmeter: str
):
  return calculate_khamis_roche(    
    cage,
    csex,
    cheightmeter,
    ckg,
    mcheightmeter,
    fcheightmeter
  )
