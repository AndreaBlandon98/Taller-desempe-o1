def calcular_nota_final(taller1, taller2, cuestionario1, cuestionario2, proyecto_final):

    notas = [taller1, taller2, cuestionario1, cuestionario2, proyecto_final]
    for nota in notas:
        if nota < 1 or nota > 5:
            return "Error: Las notas deben estar en el rango de 1 a 5."


    notaTaller1 = taller1 * 0.20
    notaTaller2 = taller2 * 0.15
    notaCuestionario1 = cuestionario1 * 0.22
    notaCuestionario2 = cuestionario2 * 0.10
    notaProyectofinal = proyecto_final * 0.33


    nota_final = (notaTaller1 + notaTaller2 +
                  notaCuestionario1 + notaCuestionario2 +
                  notaProyectofinal)

    return nota_final


taller1 = 4
taller2 = 3
cuestionario1 = 5
cuestionario2 = 4
proyecto_final = 4

nota_final = calcular_nota_final(taller1, taller2, cuestionario1, cuestionario2, proyecto_final)
print("La nota final del curso es:", nota_final)