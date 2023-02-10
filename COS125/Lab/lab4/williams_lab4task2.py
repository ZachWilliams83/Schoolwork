def GetDirection():
    direction = " "
    while direction not in ['Q', 'N', 'E', 'S', 'W']:
        direction = input("Please enter Q, N, E, S, or W.")
    return(direction)
def ParseInput(direction):
    true_direction = ' '
    if direction == 'N':
        true_direction = 'North'
    elif direction == 'E':
        true_direction = 'East'
    elif direction == 'S':
        true_direction = 'South'
    elif direction == 'W':
        true_direction = 'West'
    elif direction == 'Q':
        return
    print(f"The player moves {true_direction}")
def GameLoop():
    userinput = ' '
    while userinput != 'Q':
        userinput = GetDirection()
        ParseInput(userinput)
        if userinput == 'N':
            print("Youre on the right track")
            if userinput == 'E':
                print("youre on the right track")
                if userinput == 'S':
                    print("youre on the right track")
                    if userinput == 'W':
                        print("you win")
GameLoop()
