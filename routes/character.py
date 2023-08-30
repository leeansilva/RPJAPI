from fastapi import APIRouter
from api import API_MAIN

CHARACTER = APIRouter(
  prefix='/character',
  tags=['Personaje']
  )

@CHARACTER.get('/')
def getCharacter():
  pass

API_MAIN.include_router(CHARACTER)
