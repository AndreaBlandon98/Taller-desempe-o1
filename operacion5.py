def convertir(metros):
    millas = metros / 1609.34
    return millas


metros = float(input("Ingrese la cantidad de metros a convertir: "))
resultado = convertir(metros)
print(f"{metros} metros equivalen a {resultado:.2f} millas.")