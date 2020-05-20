def print_options():
    print " 'p' print options"
    print " 'c' csa"
    print " 't' tsa"
    print " 'v' volume"
    print " 'q'quit"

def csa():
    return (22 / 7 * ( r1 + r2 ) * l + 22 / 7 * r2 ** 2)

def tsa():
    return (22 / 7 * (( r1 + r2 ) * l + ( r1 ** 2 + r2 ** 2)))
def volume():
    return (1 / 3 * 22 / 7 * h * ( r1 ** 2 + r2 ** 2 + r1 * r2 ))

choice = "p"
while choice != "q":
    if choice == "c":

        r1 = input("r1: ")
        r2 = input("r2: ")
        l = input ("l: ")
        print "csa:",csa()
    elif choice == "t":
        r1 = input("r1: ")
        r2 = input("r2: ")
        l = input ("l: ")
        print "tsa:", tsa()
    elif choice == "v":
        r1 = input("r1: ")
        r2 = input("r2: ")
        l = input ("l: ")
        h = input ("h: ")
        print "volume:", volume()
    elif choice != "q":
        print_options()
    choice = raw_input("option: ")
print "thank u"
