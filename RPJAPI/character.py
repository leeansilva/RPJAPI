from abc import ABC, abstractmethod,ABCMeta
import json
class Personaje(metaclass=ABCMeta):

  nombre : str
  
  vida : int = 50
  agilidad : int = 50
  aguante : int = 50
  fuerza : int = 50
  destreza : int = 50
  magia : int = 50

  ataque : int = 50
  defensa : int = 50

  nivel : int = 1
  experiencia : int = 0

  @abstractmethod
  def esquivar(self):
    print(f'{self.nombre} a esquivado')

  @abstractmethod
  def atacar(self):
    print(f'{self.nombre} a atacado')

  @abstractmethod
  def defender(self):
    print(f'{self.nombre} se a defendido')

  @abstractmethod
  def curarse(self):
    print(f'{self.nombre} se a curado')

  @abstractmethod
  def investigar(self):
    print(f'{self.nombre} a investigado')


class Heroe(Personaje):
  def __init__(self, nombre):
    self.nombre = nombre
    self.vida : int = 70
    self.agilidad : int = 40
    self.aguante : int = 50
    self.fuerza : int = 70
    self.destreza : int = 50
    self.magia : int = 20

    self.ataque : int = 60
    self.defensa : int = 50

    self.nivel : int = 1
    self.experiencia : int = 0

  def esquivar(self):
    return super().esquivar()

  def atacar(self):
    return super().atacar()

  def defender(self):
    return super().defender()

  def curarse(self):
    return super().curarse()

  def investigar(self):
    return super().investigar()

class Bandido(Personaje):
  def __init__(self):
    print(self.vida)

  def esquivar(self):
    pass

  def atacar(self):
    pass

  def defender(self):
    pass

  def curarse(self):
    pass

  def investigar(self):
    pass

class Mago(Personaje):
  def __init__(self):
    print(self.vida)

  def esquivar(self):
    pass

  def atacar(self):
    pass

  def defender(self):
    pass

  def curarse(self):
    pass

  def investigar(self):
    pass    

class Guerrero(Personaje):
  def __init__(self):
    print(self.vida)

  def esquivar(self):
    return super().esquivar()

  def atacar(self):
    return super().atacar()

  def defender(self):
    pass

  def curarse(self):
    pass

  def investigar(self):
    pass   


