import random

def rps_game():
    rps_lst = ['Rock', 'Paper', 'Scissors']
    cpu_int = random.randint(0,2)
    player = input("Rock, Paper, Scissors?")
    if input == "Rock" or "Paper" or "Scissors":
        player_int = rps_lst.index(player)
        cpu_shoot = (rps_lst[cpu_int])
        if cpu_int == player_int:
            print("We both played " + rps_lst[player_int])
    
        elif cpu_int == 0 and player_int == 2:
            print("I played " + rps_lst[0] + ". You win!")
        elif cpu_int == 2 and player_int == 0:
            print("I played " + rps_lst[2] + ". You lose!")
        elif int(cpu_int) > int(player_int):
            print("I played " + cpu_shoot + ". You lose!")
        else:
            print("I played " + cpu_shoot + ". You win!")

    else:
        print("That's not an option!")

rps_game()

