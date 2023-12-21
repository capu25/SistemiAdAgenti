def parseDetection(index, list):
    if index == 0:
        list.append("A")
    elif index == 1:
        list.append("B")
    elif index == 2:
        list.append("C")
    elif index == 3:
        list.append("D")
    elif index == 4:
        list.append("E")
    elif index == 5:
        list.append("F")
    elif index == 6:
        list.append("I")
    elif index == 7:
        list.append("L")
    elif index == 8:
        list.append("M")

    # toDo - other letters

    frase = ''.join(list)
    return frase
