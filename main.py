from fastapi import FastAPI
from routes.character import CHARACTER
import uvicorn
app = FastAPI()
app.include_router(CHARACTER)

@app.get('/')
def main():
  return "Hola RPJAPI"


if __name__ =='__main__':
  uvicorn.run('main:app', reload=True)  