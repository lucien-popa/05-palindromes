"""module permettant de vérifier si une chaine de caractère est un palindrome sans tenir compte 
de la ponctuations et des accents"""
def ispalindrome(p):
    """
    vérifie si une chaine de caractère est un palindrome sans tenir compte 
    de la ponctuations et des accents
    """
    p= p.lower()
    intab= "àâäéèêëîïôöùûüÿç.,;:!?'-/_"
    outtab= "aaaeeeeiioouuuyc          "
    tab= str.maketrans(intab,outtab)
    txt= p.translate(tab)
    txt= txt.replace(" ","")
    return txt == txt[::-1]
#### Fonction principale
def main():
    """appels à la fonction secondaire ici"""
    # vos appels à la fonction secondaire ici
    print("édà",ispalindrome("édà"))
    print("àdâ",ispalindrome("àdâ"))
    print("àdà",ispalindrome("àdà"))
    print("oiture",ispalindrome("oiture"))
    print("azertreza",ispalindrome("azer    treza"))
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
if __name__ == "__main__":
    main()
