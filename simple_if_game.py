answer = input("Shall we begin? (yes/no)")

if answer.lower().strip() == "yes":
    answer = input("You reach a crossroad. Would you like to go left or right?").lower().strip()

    if answer == "left":
            answer = input("You run down a dark road and see a witch along the path. Would you like to talk to the witch? (yes/no)").lower().strip()
            if answer == "yes":
                    print("She tells you that you picked the wrong day to approach her. You are turned into a frog and are damned to live out your days in a swamp. Game over!")
                
            elif answer == "no":
                answer = input("You continue down the path, avoiding eye contact and come accross another road. Go left or right? (left/right)").lower().strip()

                if answer == "left":
                        print(" You walk about 5 feet and are fall into a spiked pit. Game over!")
                    
                elif answer =="right":
                        print("If you thought right was right, you were wrong. The only thing you hear is a growl.. Game Over!")
                else:
                    print("You took too long to input a right answer. You feel a tap on the shoulder and then nothingness. Game Over!")

            else: 
                print("You didn't answer the question. The witch sees you and immediately burns you alive. Game over!")

    elif answer == "right":
        print("right is never right. You get jumped by a pack of wolves. Game Over!")

    else:
        print("You failed to input a correct answer. You feel a sharp pain in the back and nothingness. Game Over!")

elif answer == "no":
    print("Thats to bad!")

else:
    print("Well, you didn't select yes or no. So, we assume no, you don't wish to place. Game Over!")