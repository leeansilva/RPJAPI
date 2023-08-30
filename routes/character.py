from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .api import API_MAIN
from RPJAPI.character import Heroe

CHARACTER = APIRouter(
  prefix='/api/character',
  tags=['Personaje']
  )

@CHARACTER.get('/')
def getCharacter():
  pass

@CHARACTER.post('/')
def addCharacter(nombre : str):
  nuevoPersonaje = Heroe(nombre)
  return JSONResponse(nuevoPersonaje.__dict__,status_code=200)

@CHARACTER.put('/')
def updateCharacter():
  pass

@CHARACTER.delete('/')
def deleteCharacter():
  pass
