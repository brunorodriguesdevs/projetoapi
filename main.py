from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi_pagination import Page, add_pagination, paginate
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

database = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database)
Base = declarative_base()

app = FastAPI()

class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    centro_treinamento = Column(String)
    categoria = Column(String)

Base.metadata.create_all(bind=database)

@app.get("/atletas/", response_model=Page[dict])
def read_atletas(nome: str = None, cpf: str = None, db: SessionLocal = SessionLocal()):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome == nome)
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    results = query.all()
    return paginate([{"nome": atleta.nome, "centro_treinamento": atleta.centro_treinamento, "categoria": atleta.categoria} for atleta in results])

add_pagination(app)

@app.post("/atletas/")
def create_atleta(nome: str, cpf: str, centro_treinamento: str, categoria: str, db: SessionLocal = SessionLocal()):
    atleta = Atleta(nome=nome, cpf=cpf, centro_treinamento=centro_treinamento, categoria=categoria)
    try:
        db.add(atleta)
        db.commit()
        db.refresh(atleta)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {cpf}")
    return JSONResponse(status_code=201, content={"message": "Atleta criado com sucesso"})
