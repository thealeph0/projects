def leapyear():
    i = int(input("Do you want to play a game? \n (0=YES, 1=NO)"))
    
    #redundancy to avoid having incorrect choice as input; input validation
    while i!=0 and i!=1:
        i = int(input("Do you want to play a game? \n (0=YES, 1=NO)"))
    
    while i!=1:
        print("Type in a year and the program will determine")
        yr = int(input("if the year is a leap year:"))
        
        if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
            print("LEAP YEAR")
            print("YOU WON THE GAME")
            
        else:
            print ("Not a leap year")
            
        i = int(input("Again? (0=YES, 1=NO)"))

leapyear()
