L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
somme = len(L)

pair = 0
for i in range (somme) :
     if L[i] %2 == 0 :
          pair = pair + L[i]
print (pair)