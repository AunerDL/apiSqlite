from pydantic import BaseModel

class DatoCreate(BaseModel):
    mensaje: str
