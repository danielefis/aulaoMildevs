valorA = float(input("Valor 1: "))
valorB = float(input("Valor 2: "))
somar = input("+, -, / ou *")
if somar == "+":
    print(valorA+valorB)
elif somar == "-":
    print(valorA-valorB)
elif somar == "*":
    print(valorA*valorB)
else:
    print(valorA/valorB)
