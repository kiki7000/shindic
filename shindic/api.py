from subprocess import check_output

from fastapi import FastAPI

from starlette.config import Config
from authlib.integrations.starlette_client import OAuth


__all__ = ("API", "api", "get_api")


class API(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = self
        self.config = Config(".env")

        self.oauth = OAuth(self.config)
        self.oauth.register(
            name="google",
            server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
            client_kwargs={"scope": "email"},
        )


version = check_output(["git", "rev-parse", "--short", "HEAD"]).decode("ascii").strip()

api = API(
    title="ShinDic",
    version=version,
    terms_of_service="",
    description="""    
Anyone can create a dictionary on Shindic and add custom words to it.

You can make a secret code and show people how to use, or share a neologism created by someone else.

Or use this to study vocabulary or information.

## Features

* Create custom dictionary  ( _not implemented_ ).
* Quiz for every dictionary  ( _not implemented_ ).
* Follow to get noticed about a new word  ( _not implemented_ ).
    """,

    contact={
        "name": "Woohyun Jung",
        "url": "https://github.com/kiki7000",
        "email": "devkiki7000@gmail.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },

    docs_url="/swagger-docs",
    redoc_url="/docs",
)


def get_api():
    return api
