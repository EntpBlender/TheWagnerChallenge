def script():

    Num = int(input("Enter the number of different cards: "))
    insertnum = 0
    Array = []
    for x in range(2*Num):
        y = x+1
        print(y)
        #insertnum = insertnum + 1
        #Array.append(insertnum)






# CHECKING MAIN
if __name__ == "__main__":
    script()
else:
    print("Wrong file")





def LetterReplacer(Num):
    cardlist = []
    for x in range(Num):
        match x:
            case 0:
                return ("A")
            case 1:
                return ("B")
            case 2:
                return ("C")
            case 3:
                return ("D")
            case 4:
                return ("E")
            case 5:
                return ("F")
            case 6:
                return ("G")
            case 7:
                return ("H")
            case 8:
                return ("I")
            case 9:
                return ("J")

