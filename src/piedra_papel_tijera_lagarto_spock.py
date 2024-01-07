import random
from enum import IntEnum
from collections import Counter

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

Victories = { 
    GameAction.Rock: [GameAction.Paper, GameAction.Spock], 
    GameAction.Paper: [GameAction.Scissors, GameAction.Lizard], 
    GameAction.Scissors: [GameAction.Rock, GameAction.Spock], 
    GameAction.Spock: [GameAction.Paper, GameAction.Lizard], 
    GameAction.Lizard: [GameAction.Rock, GameAction.Scissors]
    }

def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Lizard:
            print("Rock crushes lizard. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock:
            print("Spock vaporizes rock. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Spock:
            print("Paper disproves spock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Lizard:
            print("Lizard eats paper. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat     

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Spock:
            print("Spock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        elif computer_action == GameAction.Lizard:
            print("Scissors decapitates lizard. You won!")
            game_result = GameResult.Victory
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory           
            
    # You picked Spock
    elif user_action == GameAction.Spock:
        if computer_action == GameAction.Rock:
            print("Spock vaporizes rock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Scissors:
            print("Spock smashes scissors. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Paper:
            print("Paper disproves spock. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Lizard poisons spock. You lost!")
            game_result = GameResult.Defeat   

    # You picked Lizard
    elif user_action == GameAction.Lizard:
        if computer_action == GameAction.Spock:
            print("Lizard poisons spock. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Paper:
            print("Lizard eats paper. You won!")
            game_result = GameResult.Victory
        elif computer_action == GameAction.Rock:
            print("Rock crushes lizard. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors decapitates lizard. You lost!")
            game_result = GameResult.Defeat                           

    return game_result


def get_computer_action(lista_acciones_usuario, n):
    if n == 1:
        computer_action = GameAction(0)
    else:
        new_user_action = Counter(lista_acciones_usuario)
        action_final = max(new_user_action, key=lambda x: new_user_action[x])
        computer_action = random.choice(Victories[action_final])

    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def main():
    lista_acciones_usuario = []
    victorias_totales = 0

    n_partidas = int(input('Enter the number of games you want to play: '))

    n = 0
    while n < n_partidas:
        try:
            user_action = get_user_action()
            lista_acciones_usuario.append(user_action)
            n += 1  
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(lista_acciones_usuario, n)
        if assess_game(user_action, computer_action) == GameResult.Victory:
            victorias_totales += 1

    print(f'Wins: {victorias_totales}')

if __name__ == "__main__":
    main()