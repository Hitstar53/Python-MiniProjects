'''
Simple Calculator
'''
def add(n,m):
    return n+m

def sub(n,m):
    return n-m

def mul(n,m):
    return n*m

def div(n,m):
    return n/m

def power(n,m):
    return n**m

def root(n,m):
    return n**(1/m)

def perc(n,m):
    return (n/m)*100

def calculate(fir,sec,cal):
    '''
    Implement operation
    '''
    if cal == "+":
        print(f"{fir} + {sec} = {add(fir,sec)}")
    elif cal == "-":
        print(f"{fir} - {sec} = {sub(fir,sec)}")
    elif cal == "*":
        print(f"{fir} * {sec} = {mul(fir,sec)}")
    elif cal == "/":
        print(f"{fir} / {sec} = {div(fir,sec)}")
    elif cal == "^":
        print(f"{fir} ^ {sec} = {power(fir,sec)}")
    elif cal == "^/":
        print(f"{fir} ^ {1/sec} = {root(fir,sec)}")
    elif cal == "%":
        print(f"{fir} % {sec} = {perc(fir,sec)} %")

def simple_cal():
    print("This is the Simple Mode:")
    while True:
        cal = input("Select an option:\nAdd -> + , Sub -> -\nMul -> * , Div -> /\nPow -> ^ , Rt -> ^/\nPerc -> % , Exit -> e\n")
        if cal not in ['+','-','*','/','%','^','^/','e']:
            print("Invalid choice!")
            continue
        if cal.lower() == 'e':
            break
        fir,sec = input("Enter 2 numbers:\n").split()
        fir,sec = float(fir),float(sec)
        calculate(fir,sec,cal)
        recal = input("Do you want to calculate again?(yes/no)\n")
        if recal.lower() == "yes":
            continue
        else:
            break

if __name__ == '__main__':
    simple_cal()
