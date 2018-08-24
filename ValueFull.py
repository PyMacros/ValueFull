def valuefull():
    alpha = raw_input("BLANK") #Enter value to determine here
    def empty():
        if len(alpha) <= 0:
            return False
        else:
            return True
#Code under this is optional
    empty()
    if empty() == False:
        return "Value Empty!"
    elif empty() == True:
        return "Value Full!"
print valuefull()