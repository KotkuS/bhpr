from typing import Literal, Annotated

from fastapi import FastAPI, Path, Query, Header, APIRouter
from starlette.requests import Request


OrderQuery = Annotated[
    Literal["asc", "desc"],
    Query()
]

app = FastAPI()
router = APIRouter()


@router.get(path="/")
async def index():
    return "Hello World!"


@router.get(path="/{id}")
async def index(pk: int = Path(alias="id", ge=1)):
    return pk


@router.get(path="/categories")
async def index(
        request: Request,
        order_by: Literal["id", "name"] = Query(default="id", alias="orderBy"),
        order: OrderQuery = "asc",
        authorization: str = Header(alias="Authorization")
):
    return order_by, order, authorization, request


app.include_router(router=router, prefix="/blog")


if __name__ == '__main__':
    from uvicorn import run
    run(app=app)
