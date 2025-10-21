aprobados_parcial_1 = {"Juan", "Leo", "Pepe"}
aprobados_parcial_2 = {"Leo", "Ana", "Juan"}

ambos_parciales = aprobados_parcial_1.intersection(aprobados_parcial_2)
solo_un_parcial = aprobados_parcial_1.symmetric_difference(aprobados_parcial_2)
al_menos_un_parcial = aprobados_parcial_1.union(aprobados_parcial_2)

print("Aprobaron ambos parciales:", ambos_parciales)
print("Aprobaron solo uno de los dos parciales:", solo_un_parcial)
print("Aprobaron al menos un parcial:", al_menos_un_parcial)