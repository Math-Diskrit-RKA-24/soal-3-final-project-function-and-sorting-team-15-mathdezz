def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name, damage = 0, defensePower = 0):
    player = dict(
        name = name,
        score = 0,
        damage = damage,
        health = 100,
        defensePower = defensePower,
        defense = False
    )
    return player

def addPlayer(player):
   PlayerList.append(player)

def removePlayer(name):
    # If PlayerList contains name
    for i in PlayerList:
        if i["name"] == name:
            PlayerList.remove(i)
            return
    # Else:
    print("There is no player with that name!")

def setPlayer(player, key, value):
    player[key] = value
    return player

def attackPlayer(attacker:dict, target:dict):
    if target['defense']:
        damage_done = attacker['damage'] - target['defensePower']
        if damage_done < 0:
            damage_done = 0
        score_increase = round(1 - 1 / target["defensePower"],2)
    else:
        damage_done = attacker['damage']
        score_increase = 1

    new_score = attacker['score'] + score_increase
    setPlayer(attacker, 'score', new_score)

    new_health = target['health'] - damage_done
    if new_health < 0:
        removePlayer(target)
    setPlayer(target, 'health', new_health)
    setPlayer(target, 'defense', False)

def displayMatchResult():
    sorted_players = sorted(PlayerList, key=lambda p: (-p['score'], -p['health']))
    rank = 1
    for player in sorted_players:
        print(f"Rank {rank}: {player['name']} | Score: {player['score']} | Health: {player['health']}")
        rank += 1

initPlayers()
addPlayer(createNewPlayer("Zoro", 20, 10))
addPlayer(createNewPlayer("Luffy", 50, 20))
addPlayer(createNewPlayer("Pitty", 10, 5))
print(f"Players that entered the game: {PlayerList}")

attackPlayer(PlayerList[0], PlayerList[1]) # Zoro -> Luffy
removePlayer("Pitty")
addPlayer(setPlayer(createNewPlayer("Pitty", 10, 5),"defense", True))
attackPlayer(PlayerList[1], PlayerList[2]) # Luffy -> Pitty
displayMatchResult()
