L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
def maximum():
    maxi = L[7]
    for i in L:
        if i >= maxi:
            maxi = i
    print("La valeur max est:",maxi)
maximum()
def minimum():
    min = L[4]
    for i in L:
        if i <= min:
            min = i
    print("La valeur min est:",min)
minimum()