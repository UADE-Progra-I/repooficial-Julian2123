'''riz1=[[1,4,6,3,2],[4,7,2,2,1],[1,2,3,4,5]]
matriz2=[[2,3,4,5,6],[1,2,3,4,5],[6,5,4,3,2]]
filas=len(matriz1)
columnas=len(matriz1[0])
x=[
 [matriz1[fil][col] * matriz2[fil][col] for col in range(columnas)] for fil in range(filas)
]
print(x)'''

"""Dada la lista de temperaturas en °C, obtené una nueva lista
con las temperaturas en °F, redondeadas a 1 decimal.

Clue: fórmula → F = C * 9/5 + 32 y usá round(valor, 1).
"""
def conversortemp(gradosc):
    x = gradosc * 9/5 + 32
    return x
y=int(input("Ingrese grados Celsius: "))
z=conversortemp(y)
print(z)