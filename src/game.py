import random
import time

COMPUTER_NAME = 'Bob The AI'

MOVE_TO_NAME = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors'
}

INDEX_TO_MOVE = {
    1: 'R',
    2: 'P',
    3: 'S'
}

WINNING_DIALOGUE = [
    'Muahahaha I have defeated you foe!',
    'Next time you shall come prepared foe, but this time I shall let you live.',
    'Before you begin your pathetic struggle to survive, I should warn you. Your chance of winning is nonexistent.',
    'You lose! Don''t be glum. You should actually be flattered. I''ve never had to summon this much of my power to '
    'defeat someone. Fifty percent of my maximum.',
    'Do you know the definition of insanity?'
]

LOSING_DIALOGUE = [
    'Ahhhh how were you able to defeat?!?!',
    'You may have won but I shall defeat you the time next!',
    'IMPOSSIBLE! I have lost?',
    'Oh dear, what is this? It appears I have lost!',
    'Never confuse a single defeat with a final defeat. One more game?'
]


def print_move_menu():
    print(' ')
    print('=== Move Menu ===')
    print('* R = Rock')
    print('* P = Paper')
    print('* S = Scissors')
    print('=== Move Menu ===')
    print(' ')


def get_winner(a_name, a_move, b_name, b_move):
    # Rock checks
    if a_move == 'R' and b_move == 'P':
        return b_name
    if a_move == 'R' and b_move == 'S':
        return a_name

    # Paper checks
    if a_move == 'P' and b_move == 'R':
        return a_name
    if a_move == 'P' and b_move == 'S':
        return b_name

    # Scissors checks
    if a_move == 'S' and b_move == 'R':
        return b_name
    if a_move == 'S' and b_move == 'P':
        return a_name

    return 'Draw'


def print_battle_dialogue(winner):
    print('Narrator: The battle ended in a bloody war...')
    if winner == 'Draw':
        print('Narrator: Sadly there was no winner. The war was ended in a draw!')
    else:
        print('Narrator: However, there can be only one winner...')
        if winner == 'Computer':
            print(COMPUTER_NAME + ': ' + WINNING_DIALOGUE[random.randint(0, len(WINNING_DIALOGUE) - 1)])
        elif winner == 'Player':
            print(COMPUTER_NAME + ': ' + LOSING_DIALOGUE[random.randint(0, len(LOSING_DIALOGUE) - 1)])


def rps():
    game_running = False
    game_over = False
    player_name = ''

    print('Welcome to Rock Paper Scissors!')

    while True:
        play_question = str(input('Would you like to play? Y/N ')).upper()

        if play_question == 'Y':
            game_running = True
            print('Alright!, let''s play!')
            player_name = str(input('Alright! now what shall I call you? '))
            break
        elif play_question == 'N':
            game_running = False
            print('That''s fine, well then bye bye!')
            break
        else:
            print('Sorry that is an invalid input!')
            continue

    while game_running:
        while not game_over:
            computer_move_index = random.randint(1, 3)
            computer_move = INDEX_TO_MOVE[computer_move_index]

            while True:
                print_move_menu()
                player_move = str(
                    input('Based on the move menu, pick a move to battle against ' + COMPUTER_NAME + '! ')).upper()

                if player_move == 'R' or player_move == 'P' or player_move == 'S':
                    break
                else:
                    continue

            winner = get_winner(a_name='Computer', a_move=computer_move, b_name='Player', b_move=player_move)

            print(' ')
            print('=== Battle ===')
            print(' ')
            print('[Battle Move]')
            print(COMPUTER_NAME + ' have picked the move ' + MOVE_TO_NAME[computer_move] + '!')
            print(player_name + ' have picked the move ' + MOVE_TO_NAME[player_move] + '!')
            print(' ')
            print('[Battle Dialogue]')
            print_battle_dialogue(winner=winner)
            print(' ')
            print('=== Battle ===')
            print(' ')

            game_over = True

        while True:
            play_again = str(input('Would you like to play again? Y/N ')).upper()

            if play_again == 'Y':
                print('Alright then lets play again!')
                game_over = False
                break
            elif play_again == 'N':
                print('Thanks for playing and cya!')
                time.sleep(0.25)  # so the console does not close instantly
                game_running = False
                break
            else:
                print('Sorry that is an invalid input!')
                continue


if __name__ == '__main__':
    rps()
