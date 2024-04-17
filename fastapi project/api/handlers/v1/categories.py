from fastapi import APIRouter
from starlette.status import HTTP_200_OK
from src.types import CategoryDTO

router = APIRouter(tags=["Category"])


@router.get(
    path="/categories",
    response_model=list[CategoryDTO],
    status_code=HTTP_200_OK,
    response_description="List of categories",
    summary="Getting a list of categories",
    name="Category-list"
)
async def category_list():
    return [CategoryDTO(id=1, name="Sport"), CategoryDTO(id=2, name="Music")]


@router.post(
    path="/categories",
    response_model=CategoryDTO,
    status_code=HTTP_200_OK,
    response_description="Detail category",
)
async def v1():
    ...