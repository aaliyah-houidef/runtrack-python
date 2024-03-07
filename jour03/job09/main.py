def moyenne(note1,note2,note3):
    return (note1 + note2 + note3) / 3

note1 = float(input("Rentrez votre note1 : "))
note2 = float(input("Rentrez votre note2 : "))
note3 = float(input("Rentrez votre note3 : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
    print("Très bon élève")
elif moyenne_etudiant >= 11 and moyenne_etudiant <= 14:
    print("Bon élève")
elif moyenne_etudiant >= 8 and moyenne_etudiant <= 10:
    print("Élève moyen")
elif moyenne_etudiant >= 0 and moyenne_etudiant <= 7:
    print("Eleve devant faire des efforts")
    