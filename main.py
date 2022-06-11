import random
def play():
    possible_options = {"R": "Rock", "P": "Paper", "S":"Scissors"}
    possible_choices = ["R", "P", "S"]

    while True:
        user_option = input("Enter R for (R)ock or P for (P)aper or S for (S)cissors: ")
        user_option = user_option.strip().upper()

        if not user_option in possible_choices:
            print("[-] Invalid input!")

        cpu_option = random.choice(possible_choices)

        print(f"Player ({possible_options[user_option]}) : CPU ({possible_options[cpu_option]})")
        
        if cpu_option == user_option:
            print("There was a tie!")
            print()
            continue
        elif user_option == "R" and cpu_option == "S":
            print(f"You win: {possible_options[user_option]} beats {possible_options[cpu_option]}!")
            break
        elif user_option == "P" and cpu_option == "R":
            print(f"You win: {possible_options[user_option]} beats {possible_options[cpu_option]}!")
            break
        elif user_option == "S" and cpu_option == "P":
            print(f"You win: {possible_options[user_option]} beats {possible_options[cpu_option]}!")
            break
        else:
            print(f"You lose: {possible_options[user_option]} beats {possible_options[cpu_option]}!")
        
        print()
        break
play()