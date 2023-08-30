from fastapi import APIRouter

API_MAIN = APIRouter(
  prefix='/api',
  tags=['API']
  )

@API_MAIN.get('/')
def getAPIMain():
  pass