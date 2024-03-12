def convertir_pesos_a_dolares(pesos, tasa_de_cambio):
    dolares = pesos / tasa_de_cambio
    return dolares


pesos_colombianos = float(input("Ingrese la cantidad de pesos colombianos a convertir: "))
tasa_de_cambio = float(input("Ingrese la tasa de cambio entre pesos colombianos y dólares: "))
resultado = convertir_pesos_a_dolares(pesos_colombianos, tasa_de_cambio)
print(f"{pesos_colombianos:.2f} pesos colombianos equivalen a {resultado:.2f} dólares.")