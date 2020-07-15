import random

def rps_game():
    rps_lst = ['Rock', 'Paper', 'Scissors']
    cpu_int = random.randint(0,2)
    player = input("Rock, Paper, Scissors?")
    if input == "Rock" or "Paper" or "Scissors":
        player_int = rps_lst.index(player)
        cpu_shoot = (rps_lst[cpu_int])
        if cpu_int == player_int:
            print("We both played " + rps_lst[player])
    
        if cpu_int == 1 and player_int == 3:
            print("I played " + rps_lst[1] + ". You lose!")
        elif cpu_int == 3 and player_int == 1:
            print("I played " + rps_lst[3] + ". You win!")
        elif int(cpu_int) > int(player_int):
            print("I played " + cpu_shoot + ". You lose!")
        else:
            print("I played " + cpu_shoot + ". You win!")

    else:
        print("That's not an option!")

rps_game()

