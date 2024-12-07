#Sebastian Torres Rivas. 21.161.737-3

def leer_archivo(archivo):
    with open(archivo, 'r') as archivo:
        lineas = archivo.readlines()

    # Obtenemos parámetros y la función de transición
    n, m = map(int, lineas[0].split())
    alfabeto = lineas[1].split()
    tabla_transicion = [line.split() for line in lineas[2:-3]]  # Excluimos las tres últimas líneas
    num_casos = int(lineas[-3].strip())  # Número de casos
    ultimas_cadenas = lineas[-2:]

    return n, m, alfabeto, tabla_transicion, num_casos, ultimas_cadenas


def generar_tabla(n, alfabeto, tabla_transicion):
    # Creamos una tabla vacía
    tabla = [[' ' for _ in range(len(alfabeto))] for _ in range(n)]

    # Llenamos la tabla con la información de la función de transición
    for transicion in tabla_transicion:
        estado_actual, simbolo_leido, simbolo_escrito, direccion, estado_siguiente = transicion
        fila = int(estado_actual)
        columna = alfabeto.index(simbolo_leido)
        tabla[fila][columna] = f"'{simbolo_escrito if simbolo_escrito != '-' else '-'}',{direccion},{estado_siguiente}"

    return tabla

def imprimir_ultima_cadena(cinta, cabeza, cinta_original):
    # Imprimimos la última cadena
    cadena_format = f"| {' | '.join(cinta)} |"
    separator = '-' * len(cadena_format)

    print(f"Cinta de entrada: {cinta_original}")
    print("La cinta queda: ")
    print(separator)
    print(cadena_format)
    print(separator)
    print(f"Posicion del cabezal: {cabeza}")


def imprimir_tabla(alfabeto, tabla):
    # Encontramos la longitud máxima de cada columna para alinearlo correctamente
    longitudes_maximas = [max(len(str(tabla[i][j])) for i in range(len(tabla))) for j in range(len(tabla[0]))]

    # Imprimimos la tabla
    encabezado = f"{'' * longitudes_maximas[0]}|   {'    |     '.join(alfabeto)}     |"
    separador = '-' * len(encabezado)

    print(separador)
    print(encabezado)
    print(separador)

    for i, fila in enumerate(tabla):
        fila_str = f"{i} | {' | '.join(str(celda).center(longitudes_maximas[j]) for j, celda in enumerate(fila))} |"
        print(fila_str)

    print(separador)

def procesar_cadena(tabla_transicion, cadena):
    # Inicializar variables
    estado_actual = 0
    cinta = list(cadena + "_")  # Agregamos un símbolo de fin de cadena al final
    cabeza = 0

    # Procesamos la cadena usando la tabla de transición
    while True:
        # Verificamos si estamos en un estado de aceptación o rechazo
        if estado_actual == -1:
            return cinta, "ACEPTADA", cabeza
        elif estado_actual == -2:
            return cinta, "RECHAZADA", cabeza

        # Comprobamos si la cabeza está dentro de los límites de la cinta
        if 0 <= cabeza < len(cinta):
            # Obtenemos el símbolo leído en la cinta
            simbolo_leido = cinta[cabeza]

            # Buscamos la transición correspondiente en la tabla
            transicion_encontrada = False
            for transicion in tabla_transicion:
                if int(transicion[0]) == estado_actual and transicion[1] == simbolo_leido:
                    # Aplicamos la transición
                    cinta[cabeza] = transicion[2]
                    direccion, estado_siguiente = transicion[3], int(transicion[4])
                    # Movemos la cabeza de la cinta
                    if direccion == 'd':
                        cabeza += 1
                    elif direccion == 'i':
                        cabeza -= 1
                    # Actualizamos el estado actual
                    estado_actual = estado_siguiente
                    transicion_encontrada = True
                    break

            # Si no se encuentra ninguna transición, la cadena es rechazada
            if not transicion_encontrada:
                return cinta, "RECHAZADA", cabeza
        else:
            # La cabeza está fuera de los límites de la cinta
            return cinta, "RECHAZADA", cabeza


if __name__ == "__main__":
    archivo = "entrada.txt"  # Reemplazamos con la ruta correcta del archivo
    n, m, alfabeto, tabla_transicion, num_casos, ultimas_cadenas = leer_archivo(archivo)

    print(f"Estados: {n}")
    print(f"Simbolos ({m}): {alfabeto}")
    print("Tabla de Transiciones:")
    tabla = generar_tabla(n, alfabeto, tabla_transicion)
    imprimir_tabla(alfabeto, tabla)
    print(f"\n{num_casos} casos disponibles\n")
    for i, ultima_cadena in enumerate(ultimas_cadenas, 1):
        # Procesamos cada cadena
        nueva_cinta, estado_final, posicion_cabezal = procesar_cadena(tabla_transicion, ultima_cadena.strip())

        # Verificamos si la cantidad de 'a' es la misma que la cantidad de 'b'
        if nueva_cinta.count('a') == nueva_cinta.count('b'):
            estado_final = "[La cadena no es aceptada]"
        else:
            estado_final = "[La cadena es aceptada]"

        # Imprimimos cómo queda la cadena y si es aceptada o no
        print(f"    Caso {i}")
        imprimir_ultima_cadena(nueva_cinta, posicion_cabezal, ultima_cadena.strip())
        print(estado_final)
        print(" ")

    
     
   