"""convert Baht to Euro, Won and Yen"""

baht = float(input("Thai Baht: "))
euro = baht * 0.029
won = baht * 37.64
yen = baht * 3.47
print(f"{baht:.2f} Baht is {euro:.2f} Euro, {yen:.2f} Yen and {won:.2f} Won.")