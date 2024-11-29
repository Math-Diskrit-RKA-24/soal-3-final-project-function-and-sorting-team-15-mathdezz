def initPlayers():
  global PlayerList
  PlayerList = []

def createNewPlayer(name, damage = 0, defensePower = 0):
  Player = dict(name = name,
              score = 0,
              damage = damage,
              health = 100,
              defensePower = defensePower,
              defense = False)
  return Player

def addPlayer(player):
  PlayerList.append(player)


def removePlayer(name):


def setPlayer(player, key, value):


def attackPlayer(attacker:dict, target:dict):


def displayMatchResult():

