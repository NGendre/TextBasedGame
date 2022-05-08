import inquirer
import manipulateJsonObject as jsObj


def createMenu():
    createMenuChoices = findExistitingGames();  ## TODO a ajouter au menu
    createMenuChoices.insert(0, ('Create new game', 'new'))
    question = [
        inquirer.List(
            'createMenu',
            message="creation Menu",
            choices=createMenuChoices,
        ),
    ]
    answer = inquirer.prompt(question)
    if answer.get('createMenu') == 'new':
        newGame()
def findExistitingGames():
    return []  # TODO detecter les jeux existants
def defineStats():
    choices = []
    for i in range(1,11):
        choices.append((str(i),str(i)))
    question = [
        inquirer.List(
            'amountOfStats',
            message="Amount of stats",
            choices=choices,
        ),
    ]
    answer = inquirer.prompt(question)
    statsArray = []
    for i in range(0, int(answer.get('amountOfStats'))):
        answer = input("Enter a name for stat number " + str(i + 1) + ": ")
        statsArray.append(answer)
    return statsArray


def newGame():
    questions = [
        inquirer.Text('gameName',
                      message="What is the name of your game?"),
        inquirer.Text('characterType',
                      message="What type of character will the player incarnate?"),
        inquirer.Confirm('nameChoicePlayer',
                         message="Can the player choose his name?",default=True),
        inquirer.Confirm('ageRestriction',
                         message="does the player have to be 18 and older?",default=True)

    ]
    stats = defineStats()
    answers = inquirer.prompt(questions)


    jsObj.createGameJson(answers.get('gameName'),answers.get('characterType'),
                         answers.get('nameChoicePlayer'),answers.get('ageRestriction'),stats)





createMenu()  # TODO remowe when done
