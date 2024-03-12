def nuevo_minimo(salario_minimo_actual):
    incremento = salario_actual * 0.042
    nuevo_minimo = salario_minimo_actual + incremento
    return nuevo_minimo


salario_actual = float(input("Ingrese el salario mínimo actual: "))
nuevo_salario_minimo = nuevo_minimo(salario_actual)
print(f"El nuevo salario mínimo para el próximo año será: {nuevo_salario_minimo:.2f}")