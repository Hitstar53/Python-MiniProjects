'''
Random Password Generation System
'''
import random
import os

def pass_gen(p_len):
    '''
    gen a pswd
    '''
    ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&_"
    password = ""
    for _ in range(p_len):
        password += random.choice(ref)
    return password

def pass_save(pswd,a_name):
    '''
    save pswd
    '''
    with open(f"{a_name}.txt","a") as p:
        p.write(pswd)
    return "Password has been saved successfully!"

def pass_create():
    '''
    create a pswd, call pass_gen & pass_save
    '''
    pass_len = int(input("Enter length of password to be generated:\n"))
    password = pass_gen(pass_len)
    print(f"Here is your generated password: {password}\nPassword length: ",len(password))
    pws = input("Do you want to save the password?(yes/no)\n")
    if pws.lower() == "yes":
        f_name = input("Enter a file name:\n")
        pass_save(password,f_name)
    else:
        print("Password was not saved!(remember to copy it before closing the program)")

def pass_access():
    '''
    access a saved pswd
    '''
    ac_fname = input("Which password do you want to access?(enter file name)\n")
    with open(f"{ac_fname}.txt","r") as f:
        f.seek(0)
        ac_pswd = f.readline()
    print(f"Saved password is: {ac_pswd}")

def pass_delete():
    '''
    delete a saved password
    '''
    d_fname = input("Which password do you want to delete?(enter file name)\n")
    with open(f"{d_fname}.txt","r") as d:
        d.seek(0)
        d_pswd = d.readline()
    print(f"Saved password is: {d_pswd}")
    dec = input("Are you sure you want to delete this password?(yes/no)\n")
    if dec.lower()=='yes':
        os.remove(f"{d_fname}.txt")
        print("Password deleted successfully!")
    else:
        print("Password not deleted!")

while True:
    opt = input("Do you want to create,access or delete a saved password?(create/access/delete)\n")
    if opt.lower() == "create":
        pass_create()
        replay = input("Do you want to create another password?(yes/no)\n")
        if replay.lower() == "no":
            break
    elif opt.lower() == "access":
        pass_access()
        replay = input("Do you want to access another password?(yes/no)\n")
        if replay.lower() == "no":
            break
    elif opt.lower() == "delete":
        pass_delete()
        replay = input("Do you want to delete another password?(yes/no)\n")
        if replay.lower() == "no":
            break
    else:
        break
