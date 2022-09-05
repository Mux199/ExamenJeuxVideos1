from pydantic import BaseModel
from CodeRayon import CodeRayon


class ModelJeux(BaseModel):
    console: str
    genre: str
    prix: float
    description: str
    code_rayon: str


