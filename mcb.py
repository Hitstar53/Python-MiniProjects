def main():
    print("Welcome to Missionary and Cannibals Game!\nRules:\nNo. of Missionaries cannot be less than no. of cannibals at any point on any bank!\n\nLet's Begin!")
    lm = int(input("Enter the number of missionaries: "))
    lc = int(input("Enter the number of cannibals: "))
    b = rm = rc = 0
    print(f"Initial State:\nMissionaries: {lm}\nCannibals: {lc}\nBoat is on left Bank!\n")
    flag = True
    while(flag):
        if lm == 0 and lc == 0:
            print("You Won the Game!\n")
            print(f"Final State on Left:\nMissionaries: {lm}\nCannibals: {lc}\n")
            print(f"Final State on Right:\nMissionaries: {lm}\nCannibals: {lc}\n")
            flag = False
            break
        um, uc = map(int, input("Enter the no. of missionaries and cannibals: ").split())
        if b == 0:
            lm -= um
            lc -= uc
            rm += um
            rc += uc
        else:
            lm += um
            lc += uc
            rm -= um
            rc -= uc
        if (rm < rc and rm != 0) or (lm < lc and lm!= 0):
            print("Missionaries are less than cannibals!\nYou Lost the Game!")
            flag = False
            break
        else:
            print(f"Current State on Right Bank:\nMissionaries: {rm}\nCannibals: {rc}\n")
            print(f"Current State on Left Bank:\nMissionaries: {lm}\nCannibals: {lc}\n")
            if b == 0:
                print("Boat is on left Bank!\n")
                b = 1
            elif b == 1:
                print("Boat is on right Bank!\n")
                b = 0   
    
if __name__ == "__main__":
    main()