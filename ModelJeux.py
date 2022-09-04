from pydantic import BaseModel
import CodeRayon from CodeRayon

class ModelJeux(BaseModel):
    console: str
    genre: str
    prix: float
    description: str
    code_rayon: str

