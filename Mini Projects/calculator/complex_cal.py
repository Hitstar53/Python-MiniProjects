import math

def choose_cal(cal):
    while True:
        if cal == 'a':
            print([ m for m in dir(math) if not m.startswith('__')])
            choose = input("Choose one of the above options:\n")

def complex_cal():
    print("This is the Complex Mode:")
    while True:
        cal = input("Select an option:\nTrigonometry -> t\nLogarithms -> l\nAngles -> a\nFunctions -> f\nExit -> e\n")
        
        if cal.lower() == 'e':
            break
        elif cal.lower() in ['a','f','l','t']:
            choose_cal(cal.lower())
            continue
        elif cal.lower() not in ['a','f','l','t','e']:
            print("Invalid choice!")
            continue
        fir,sec = input("Enter 2 numbers:\n").split()
        fir,sec = float(fir),float(sec)
        recal = input("Do you want to calculate again?(yes/no)\n")
        if recal.lower() == "yes":
            continue
        else:
            break

if __name__ == '__main__':
    complex_cal()