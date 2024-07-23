import random
item_list = ["Rock" ,"Paper" ,"Scissor"]
user_choice = input("Enter your move = Rock ,Paper ,Scissor :")
computer_choice = random.choice(item_list)

print(f"user_choice : {user_choice} ,computer_choice : {computer_choice} ")
 
if user_choice == computer_choice:
    print(" Both choice same = Match is Tie")
    
    
elif user_choice == "Rock":
    if computer_choice == "Paper":
     print("Paper cover the Rock = Computer win")
    else:
        print("Rock samashes Scissor = You Win")
        
        
elif user_choice == "Paper":
    if computer_choice == "Rock":
     print("Paper cover the Rock = You win")
    else:
        print("Scissor cut the Paper = Computer Win")
        
        
elif user_choice == "Scissor":
    if computer_choice == "Paper":
     print("Scissor cut the Paper  = You win")
    else:
        print("Rock samashes Scissor = Computer Win")

    