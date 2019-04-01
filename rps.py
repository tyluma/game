while True:
  var = input("suuuuup?").lower()
  
  print("you chose: " + var)
  
  import random
  choice = random.choice(["rock","paper", "scissors"])
  
  if var == "rock" or var == "paper" or var == "scissors":
    print("we pick: " + choice)
    if var == choice:
      print("draw")
    elif var =="rock" and choice =="scissors":
      print("you win")
    elif var == "paper" and choice =="rock":
      print("you win")
    elif var == "scissors" and choice == "paper":
      print("you win")
    else:
      print("you loooooooseee")
  else:
    print("f you")
    
