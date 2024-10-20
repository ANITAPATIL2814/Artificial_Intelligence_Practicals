j1=int(input("capacity of jug1:"))
j2=int(input("capacity of jug2:"))
g=int(input("Amount of water to be measured:"))
def apply_rule(ch, x, y):
    #Rule 1: Fill jug 1
    if ch == 1:
        if x<j1:
            return j1,y
        else:
            print("rule cannot be applied")
            return x,y
    #Rule 2:Fill jug 2
    elif ch == 2:
            if y<j2:
                return x,j2
            else:
                print("rule cannot be applied")
                return x,y
    #Rule 3:Transfer all water from jug1 to jug2
    if ch == 3:
                if x > 0 and x+y <= j2:
                    return 0,x+y
                else:
                    print("Rule cannot be applied")
                    return x,y
    #Rule 4:Transfer all water from jug2 to jug1
    if ch == 4:
                    if y > 0 and x+y <= j1:
                        return x+y,0
                    else:
                        print("Rule cannot be applied")
                        return x,y

    #Rule 5:Transfer some water from jug1 to jug2 until jug2 is full
    if ch == 5:
                        if x > 0 and x+y >= j2:
                            return x-(j2-y),j2
                        else:
                            print("Rule cannot applied")
                            return x,y
    #Rule 6:Transfer some water from jug2 to jug1 until jug1 is full
    if ch == 6:
                            if y > 0 and x+y >= j1:
                                return j1,x-(j1-x)
                            else:
                                print("Rule cannot applied")
                                return x,y
    #Rule 7:Empty jug1
    if ch == 7:
                            if x > 0:
                                return 0,y
                            else:
                                print("Rule cannot applied")
                                return x,y
    #Rule 8:Empty jug2
    if ch == 8:
        if y > 0:
            return x,0
        else:
            print("Rule cnanot applied")
            return x,y
    #invalid choice
    else:
        print("INVALID CHOICE")

#intialize capacity of both jugs as 0
x = y = 0
while(True):
        if (x==g) or (y==g):
            print("GOAL ACHIEVE")
            break
        else:
            print("--------RULES--------")
            print("Rule1: fill jug 1")
            print("Rule2: fill jug2")
            print("Rule3:transfer all water from jug1 to jug2")
            print("Rule4:transfer all water from jug2 to jug1")
            print("Rule5:transfer some water from jug1 to jug2 until jug1 is full")
            print("Rule6:transfer some water from jug2 to jug1 until jug2 is full")
            print("Rule7:empty jug1")
            print("Rule8:empty jug2")
            ch=int(input("Enter rule to apllied:"))
            x, y = apply_rule(ch, x, y)
            print("------------STATUS--------")
            print("CURRENT SATE:", end=" ")
            print(x, y)
