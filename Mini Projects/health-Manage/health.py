def get_date():
    import datetime
    m = ""
    n = str(datetime.datetime.now())
    m = "[" + n + "] "
    return m

while True:
    print("WELCOME TO THE HEALTH MANAGEMENT SYSTEM!")
    a = int(input("Do you want to retrieve or log?\nPress:\n1 to Retrieve\n0 to log\n"))
    b = int(input("Enter name of the person:\nPress:\n0 for Hammad\n1 for Harry\n2 for Rohan\n"))
    c = int(input("Which action should be taken?\nPress:\n0 for food\n1 for Exercise\n"))

    if a:
        if b == 0:
            if c:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\hammad-e.txt") as hame:
                    print(hame.read())
            else:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\hammad-f.txt") as hamf:
                    print(hamf.read())
        elif b == 1:
            if c:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\harry-e.txt") as hare:
                    print(hare.read())
            else:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\harry-f.txt") as harf:
                    print(harf.read())
        elif b == 2:
            if c:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\rohan-e.txt") as rohe:
                    print(rohe.read())
            else:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\rohan-f.txt") as rohf:
                    print(rohf.read())
    else:
        d = input("What do you want to log?\n")
        if b == 0:
            if c:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\hammad-e.txt", "a") as hame:
                    hame.write(get_date())
                    print(hame.write(d))
                    hame.write("\n")
            else:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\hammad-f.txt", "a") as hamf:
                    hamf.write(get_date())
                    print(hamf.write(d))
                    hamf.write("\n")
        elif b == 1:
            if c:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\harry-e.txt", "a") as hare:
                    hare.write(get_date())
                    print(hare.write(d))
                    hare.write("\n")
            else:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\harry-f.txt", "a") as harf:
                    harf.write(get_date())
                    print(harf.write(d))
                    harf.write("\n")
        elif b == 2:
            if c:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\rohan-e.txt", "a") as rohe:
                    rohe.write(get_date())
                    print(rohe.write(d))
                    rohe.write("\n")
            else:
                with open("D:\\Python-MiniProjects\\Mini Projects\\health-Manage\\rohan-f.txt", "a") as rohf:
                    rohf.write(get_date())
                    print(rohf.write(d))
                    rohf.write("\n")

    e = int(input("Press:\n0 to quit\n1 to continue\n"))
    if e == 0:
        print("THANKS FOR USING THE HEALTH MANAGEMENT SYSTEM!")
        break