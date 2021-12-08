import simple_cal
import complex_cal

def recal():
    re_cal = input("Do you want to switch calculator modes?(yes/no)\n")
    if re_cal.lower() == 'yes':
        return True
    return False

if __name__ == '__main__':
    while True:
        cal_mode = input("Which calculator mode do you want to use?(simple/complex)\n")
        if cal_mode.lower() == 'simple':
            simple_cal.simple_cal()
            if not recal():
                break
        elif cal_mode.lower() == 'complex':
            complex_cal.complex_cal()
            if not recal():
                break
        else:
            continue

