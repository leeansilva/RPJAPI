from pydantic import BaseModel
from random import randint,random, choice
import time
class Character(BaseModel):
  nombre : str
  vida : int = 100
  ataque : int = 50
  defensa : int = 20
  resistencia : int = 50
  experiencia : int = 0

  posicionDefensiva : int = 0

  @property
  def vida(self):
    self.vida

  @vida.setter
  def vida(self,nuevaVida):
    self.vida = nuevaVida
    print(f'Se ha cambiado los puntos de vida : {self.vida}')

  def atacar(self,enemigo):
    self.posicionDefensiva = 0
    ataqueMax = self.ataque + 10
    ataqueMin = self.ataque - 10
    ataquerandom = randint(ataqueMin,ataqueMax)
    enemigo.vida = enemigo.vida - (ataquerandom - enemigo.posicionDefensiva)
    print(f'{self.nombre} (+{ataquerandom} Atk) ha atacado a {enemigo.nombre} (+{enemigo.posicionDefensiva} Def), atacado con: -{ataquerandom - enemigo.posicionDefensiva}, vida restante: {enemigo.vida}') 
        
  def defenderse(self):
    defMax = self.defensa + 5
    defMin = self.defensa - 10
    self.posicionDefensiva = randint(defMin,defMax)
    print(f'{self.nombre} se puso en posicion defensiva: +{self.posicionDefensiva} Def')

  def esquivar(self):
    return "Esquivando.."

  def explorar(self):
    xpWin = randint(50, 500)
    self.experiencia += xpWin
    return f"""¡Ganaste +{xpWin} xp! /n
              Puntos actuales de experiencia: {self.experiencia}"""

class Fight(BaseModel):
  player1 : Character
  player2 : Character

  def intencion(self,turnoPlayer, enemigo):
    intenciones = {
      'atacar': turnoPlayer.atacar,
      'defender': turnoPlayer.defenderse
      }

    print(choice(list(intenciones.values())))
    accion, metodo = choice(list())
    if accion == 'atacar':
      metodo(enemigo)
    else :
      metodo()

  
  def pelear(self):
    
    self.intencion(self.player1, self.player2)
    self.intencion(self.player2, self.player1)
    time.sleep(3)
    
    self.intencion(self.player1, self.player2)
    self.intencion(self.player2, self.player1)
    time.sleep(3)
    
    self.intencion(self.player1, self.player2)
    self.intencion(self.player2, self.player1)
    time.sleep(3)
    
    self.intencion(self.player1, self.player2)
    self.intencion(self.player2, self.player1)
    time.sleep(3)
    



luchador = Character(nombre="Leandro",vida= 100)
guerrero = Character(nombre="Waskas",vida= 100)

pelea1 = Fight(player1=luchador, player2=guerrero)
pelea1.pelear()