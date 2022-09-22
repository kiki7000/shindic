from shindic.api import api
from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware.sessions import SessionMiddleware

from shindic.router import auth

from shindic.database import engine, Base


api.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.add_middleware(
    SessionMiddleware,
    secret_key=api.config.get("SECRET_KEY"),
)
api.include_router(auth.router)

Base.metadata.create_all(bind=engine)


@api.get("/")
def main():
    return {"Hello": "World"}
