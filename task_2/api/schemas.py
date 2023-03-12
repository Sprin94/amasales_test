from pydantic import BaseModel


class Goods(BaseModel):
    article: str
    brand: str
    title: str
