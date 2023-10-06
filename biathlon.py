from random import randint


def splash():
    print ("")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("         Biathlon")
    print ("")
    print ("    a hit or miss game")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    return None

open = 0
closed = 1

def is_open(value):
    if value == open:
        return True
    else:
        return False

    
def is_closed(value):
    return not(is_open(value)) 
    
    
def new_targets():
    targets = [open for x in range(5)]
    return targets


def close_target(targets, position):
    targets[position] = closed
    return targets
    
def points(targets):
    score = 0
    for x in range(5):
        if targets[x]==closed:
            score += 1
    return score

def targets_to_string(targets):
    output = ""    
    for x in targets:
        if x == open:
            output += '0 '
        elif x == closed:
            output += '* '
    return output

def view_targets(targets):
    output = "" + "\n" + "  "
    for x in range(5):
        output += str(x+1) + " "
    output += "\n" + "\n" + "  " + targets_to_string(targets) + "\n"
    print(output)

def random_hit():
    return randint(0,1) == 1

def shoot(targets, position):
    if random_hit():
        if is_open(targets[position]):
            close_target(targets, position)
            return "Hit on open target"
        else:
            return "Hit on closed target"
    else:
        return "Miss"

def parse_target(string):
    if 0<int(string)<6:
        return int(string)-1
    else:
        return None

def won_game(targets):
    for x in targets:
        if x == 0:
            return False
    return True
    
def game(rounds):
    splash()
    
    targets = new_targets() 
    
    totalshots = rounds
    
    currentshot = 1
    
    while totalshots > 0:
        view_targets(targets)
        target_position = input("Shot nr " + str(currentshot) + " at: ")
        while target_position == "":
            target_position = input("Shot nr " + str(currentshot) + " at: ")
        print ("")

        target_position = parse_target(target_position)
        
        if target_position is not None:
            result = shoot(targets, target_position)
            print(result)
            totalshots -= 1
            currentshot += 1
        else:
            print("Please choose a nummer between 1 and 5.")
            
        if won_game(targets):
            print ("\n" + "  Lucky Win!!!")
            totalshots = 0
            rounds = currentshot -1
    
    view_targets(targets)
    percent = int((points(targets)/rounds)*100)
    print("You hit " + str(points(targets)) + " of " + str(rounds) + " shots which means you hit " + str(percent) + "% of the time" + "\n")
    nyttspel = input("If you want to try again write 'yes': ")
    if nyttspel == "yes":
        print("")
        game(int(input("How many shots do you want? "))) 

