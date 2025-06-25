from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/datos/")
def crear_dato(dato: schemas.DatoCreate, db: Session = Depends(get_db)):
    nuevo_dato = models.Dato(mensaje=dato.mensaje)
    db.add(nuevo_dato)
    db.commit()
    db.refresh(nuevo_dato)
    return {"id": nuevo_dato.id, "mensaje": nuevo_dato.mensaje}