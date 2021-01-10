# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:23:40 2021

@author: turgut
"""


import random

""" We have 75 animal name in our 'animals.txt' file so find random number to
to find out specific animal name"""
random = random.randint(0,75)

# English letter list

def hangman():
    
    # Open file which contain animals name
    with open("animals.txt", "r+", encoding="utf-8") as file:
        # Choose random animal name in "animal.txt"
        word = file.readlines()[random]
        
        validletters = "abcdefghijklmnopqrstuvwxyz"
        turns = 10 
        guessmade =''
       
        while len(word) > 0:
            
            main =''
            missed = 0
            # We using 'word[:-1]' string slicing because when we get animal
            # name in txt file its coming with space end of it name.
            for letter in word[:-1]:
                if  letter in guessmade:
                    main = main + letter
                    
                else:
                    main = main + "_" + " "
           
            if main == word[:-1]:
                print(main)
                print("You win")
                break

            print("Guess the word: " , main)
            guess = input()
                
            if guess in validletters:
                guessmade = guessmade + guess
                
            else:
                print("Please Enter valid character")
                guess = input()
                
            if guess not in word:
                turns -= 1
                if turns == 9:
                    print("9 turns left")
                    print("  --------  ")
                if turns == 8:
                    print("8 turns left")
                    print("  --------  ")
                    print("     O      ")
                if turns == 7:
                    print("7 turns left")
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                if turns == 6:
                    print("6 turns left")
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                    print("    /       ")
                if turns == 5:
                    print("5 turns left")
                    print("  --------  ")
                    print("     O      ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 4:
                    print("4 turns left")
                    print("  --------  ")
                    print("   \ O      ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 3:
                    print("3 turns left")
                    print("  --------  ")
                    print("   \ O /    ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 2:
                    print("2 turns left")
                    print("  --------  ")
                    print("   \ O /|   ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 1:
                    print("1 turns left")
                    print("Last breaths counting, Take care!")
                    print("  --------  ")
                    print("   \ O_|/   ")
                    print("     |      ")
                    print("    / \     ")
                if turns == 0:
                    print("You loose")
                    print("  --------  ")
                    print("     O_|    ")
                    print("    /|\     ")
                    print("    / \     ")
                    break
        
            
            
            
            
print("""****************************
      HANGMAN GAME
    
****************************""")

name = input("Please Enter Your Name ")

print("########################\n" +
      "WELCOME "  +  name.upper() 
    
+"\n########################") 
# Starting main function to play game
hangman()
   
        