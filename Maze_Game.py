#! usr/bin/env python3

import time

def maze():
    print("You have been put into a seemingly endless ")
    print("You can see an exit in the far distnace")
    print("Who knows what lies between")
    print()
    print("Let's begin...")
    print()
    print("You take a step forward")
    time.sleep(2) # time.sleep is just used to build up the suspense!
    print("You reach the first turn")
    print()
    time.sleep(2)
    print("You can go left (L) or right (R)")
    answer = input("Make your choice ... ")
    print("You chose",answer,"... what will happen? ...")
    time.sleep(2)
    print("You turn the corner...")
    time.sleep(2)
    print("You walk forward a few steps...")
    time.sleep(2)
    if answer == "R":
        print("You fall quite a way and are impaled by fifty spears")
        start_again_q = input("Would you like to start again? (y or n)")
        def restart_maze():
            if start_again_q == "y":
                print("Starting again...")
                maze()
            elif start_again_q == "n":
                print("that wasn't the answer I was looking for, let's try again...")
                restart_maze()
            else:
                print("incorrect input, please try again")
                restart_maze()
    else:
        print("Looks like you've beaten this primitive maze program; well done! Onto the next....")
        maze1()
maze()

def maze1():
    print("Welcome back, good to see you beat the first maze, this wont be so easy, let's begin")
    time.sleep(2)
    answer2 = input("You continue to walk down through the maze, when you see an odd opening in the wall: Do you investigate this opening, bearing in mind that the otherside could be dangerous?")
    def problem0():
        if answer2 == "y":
            print("You turn the corner...")
            time.sleep(2)
            print("When you find that there is a blinding light: and without your sight you have no chance to complete the maze - you've lost")
            def restart_maze1():
                start_again_q = input("Would you like to try again from the beginning of the section or the start of the maze (se for section, st for start)")
                if start_again_q == "se":
                    print("Starting from the section...")
                    maze1()
                elif start_again_q == "st":
                    print("Starting from the beginning...")
                    maze()

                else:
                    print("Incorrect input, please try again...")
                    restart_maze1()
        elif answer2 == "n":
            print("Could be a missed chance to escape, anyway you keep moving...")
            time.sleep(2)
            print("Now you face another problem, you can see three paths in the distance: all three have a differnt outcome, and one will get you out of the maze for good")
            """ answer3 = int(input("Now you reach thre three paths: make your choice (1, 2 or 3)"))
            if answer3 == int(1): # check this with validation"""
        else:
            print("Incorrect input, try again ")
            problem0()
