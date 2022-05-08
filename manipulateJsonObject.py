import json
import random

def createGameJson(gameName,characterType,nameChoicePlayer,ageRestriction,stats):
    jsonGame = {}
    jsonGame['id'] = str(random.randint(0,10000)) # TODO remplacer apres par id fetched online
    jsonGame['gameName'] = gameName
    jsonGame['characterType'] = characterType
    jsonGame['nameChoicePlayer'] = nameChoicePlayer
    jsonGame['ageRestriction'] = ageRestriction
    jsonGame['stats'] = stats

    with open("data/game/"+jsonGame['id']+jsonGame['gameName']+'.json','w',encoding='utf-8') as file:
        json.dump(jsonGame,file,ensure_ascii=False,indent=4)

