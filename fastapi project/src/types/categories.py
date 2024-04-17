from pydantic import Field, PositiveInt

from .base import DTO


class CategoryCreateDTO(DTO):
    name: str = Field(
        max_length=64,
        min_length=2,
    )


class CategoryUpdateDTO(CategoryCreateDTO):
    ...


class CategoryDTO(CategoryCreateDTO):
    id: PositiveInt
