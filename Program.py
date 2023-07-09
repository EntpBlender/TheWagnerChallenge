def script():

    InputNum = (int(input("Enter the number of different types of cards: ")))
    CardNum = InputNum*4
    Finished = False

    D2CardList = []
    While Finished == False:
        for x in range(CardNum):
            TCardList = []
            for y in range(InputNum):
                TCardList.append(LetterReplacer(y))
            for y in range(InputNum):
                TCardList.append(LetterReplacer(y))
            D2CardList.append(TCardList)



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

    


# CHECKING MAIN
if __name__ == "__main__":
    script()
else:
    print("Wrong file")