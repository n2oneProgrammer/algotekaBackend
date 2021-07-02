from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .router import router_code,router_language,router_algorithm
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Algoteka", description="", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_code)
app.include_router(router_language)
app.include_router(router_algorithm)

@app.get("/")
async def root():
    response = RedirectResponse(url="/docs")
    return response
