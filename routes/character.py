from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .api import API_MAIN
from RPJAPI.character import Character

CHARACTER = APIRouter(
  prefix='/api/character',
  tags=['Personaje']
  )

@CHARACTER.get('/')
def getCharacter():
  return True

@CHARACTER.post('/')
def addCharacter(nombre : str):
  nuevoCharacter = Character(nombre=nombre, vida=100)
  return JSONResponse(nuevoCharacter,status_code=200)

@CHARACTER.put('/')
def updateCharacter():
  return True

@CHARACTER.delete('/')
def deleteCharacter():
  return True
