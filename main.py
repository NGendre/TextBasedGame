import inquirer

import create
import play

question = [
    inquirer.List(
        'mainMenu',
        message="Menu",
        choices=[('Play a game','play'),('Create game','create')],
    ),
]
answer = inquirer.prompt(question)

match answer.get('mainMenu'):
    case 'play':
        play.play()
    case 'create':
        create.createMenu()
