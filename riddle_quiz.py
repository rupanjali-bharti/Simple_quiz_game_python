import sys
ans=input("Do you want to play?")

#initialize count as 0 and then add score to it whenever ans is correct
count = 0

# converting the answer of user to lower and then comparing it with yes to play
if ans.lower() != "yes":

    # if user does not want to play , the program will exit using exit()
    sys.exit()
else: 
    # add more quetions here for more fun!
    print("Q1) What do you call a fish without an eye?")  
    ans1=input("your answer:")  
    if ans1.lower() == "fsh":
        count += 1
        print("correct !")
    else:
         print("incorrect !")   

    print("Q2) What do you call a guy with no arms and no legs at your front door?")  
    ans1=input("your answer:")  
    if ans1.lower() == "matt":
        count += 1
        print("correct !")
    else:
         print("incorrect !")      

    print("Q3) What does a snowman prefer for breakfast?")  
    ans1=input("your answer:")  
    if ans1.lower() == "snowflakes":
        count += 1
        print("correct !")
    else:
         print("incorrect !")      

    print("Q4) What is mummy' fav type of music?")  
    ans1=input("your answer:")  
    if ans1.lower() == "wrap":
        count += 1
        print("correct !")
    else:
         print("incorrect !") 

    print("Q5) Who pend the day at the window goe to the table for meals and hides at night?")  
    ans1=input("your answer:")  
    if ans1.lower() == "housefly":
        count += 1
        print("correct !")
    else:
         print("incorrect !")           

# to print our score
print("Your score out of 5yes is: ",count)        