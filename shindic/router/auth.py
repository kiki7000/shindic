from enum import Enum

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from fastapi.requests import Request

from shindic.api import get_api, API

__all__ = ("router",)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


class OauthTypeEnum(str, Enum):
    google = "google"


@router.route("/callback/{oauth_type}")
async def callback(oauth_type: OauthTypeEnum, request: Request, api: API = Depends(get_api)):
    if oauth_type == OauthTypeEnum.google:
        token = await api.oauth.google.authorize_access_token(request)
        user = await api.oauth.google.parse_id_token(request, token)
        request.session["user"] = dict(user)

    return RedirectResponse(url="/")


@router.get("/login/{oauth_type}")
async def login(oauth_type: OauthTypeEnum, request: Request, api: API = Depends(get_api)):
    if oauth_type == OauthTypeEnum.google:
        return await api.oauth.google\
            .authorize_redirect(request, f"{str(request.url)[: -1 * len(request.url.path)]}/auth/callback/google")
