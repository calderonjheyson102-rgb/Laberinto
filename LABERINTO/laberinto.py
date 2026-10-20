

laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]


def imprimir_laberinto(matriz):
    for fila in matriz:
        for celda in fila:
            print(f"{str(celda):>3}", end="")
        print()


print("LABERINTO ORIGINAL:")
imprimir_laberinto(laberinto)

inicio = (8, 0)
final = (0, 0)

movimientos = [
    (-1, 0),  # Arriba
    (0, 1),   # Derecha
    (1, 0),   # Abajo
    (0, -1)   # Izquierda
]

camino = [inicio]
visitadas = {inicio}


def buscar_salida(fila, columna, puntos):
    posicion = (fila, columna)

    # Caso base: llegamos a F
    if posicion == final:
        return puntos >= 23

    # Probar movimientos en orden
    for df, dc in movimientos:
        nf = fila + df
        nc = columna + dc

        # Validar límites
        if not (0 <= nf < 9 and 0 <= nc < 9):
            continue

        # Evitar paredes
        if laberinto[nf][nc] == 0:
            continue

        # Evitar repetir posiciones
        if (nf, nc) in visitadas:
            continue

        # Calcular puntos de la casilla
        valor = laberinto[nf][nc]
        puntos_casilla = 1 if valor == 'F' else valor

        # Avanzar
        visitadas.add((nf, nc))
        camino.append((nf, nc))

        # Buscar desde la nueva posición
        if buscar_salida(
            nf, nc, puntos + puntos_casilla
        ):
            return True

        # Retroceder si no encuentra solución
        camino.pop()
        visitadas.remove((nf, nc))

    return False


solucion = buscar_salida(8, 0, 1)

if solucion:
    print("\n¡SALIDA ENCONTRADA!")
    print("Camino recorrido:")

    for posicion in camino:
        print(posicion, end=" -> ")

    print("\n")

    resultado = [fila[:] for fila in laberinto]

    for fila, columna in camino:
        if (fila, columna) == inicio:
            resultado[fila][columna] = 'I'
        elif (fila, columna) == final:
            resultado[fila][columna] = 'F'
        else:
            resultado[fila][columna] = '*'

    print("LABERINTO CON EL CAMINO:")
    imprimir_laberinto(resultado)

    total = sum(
        1 if laberinto[f][c] in ('I', 'F')
        else laberinto[f][c]
        for f, c in camino
    )

    print("Puntos obtenidos:", total)

else:
    print("\nNo se encontró una salida válida.")
    print("No existe un camino encontrado con 23 puntos o más.")
