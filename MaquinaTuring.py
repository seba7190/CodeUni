def turing_palindrome(cadena):
  #Simula una Máquina de Turing que reconoce palíndromos.

  cadena = cadena.lower().replace(" ", "")  # Eliminar espacios y convertir a minúsculas
  cinta = list(cadena) + [" "]  # Agregar un espacio en blanco al final
  cabezal = 0
  estado = "q0" # Estado Inicial

 # Ciclo principal que simula el funcionamiento de la Máquina de Turing.
 # Este no termina hasta tener uno de los dos estados.
  while estado != "q_aceptar" and estado != "q_rechazar":

    if estado == "q0":
      
      if cinta[cabezal] == " ":
        estado = "q_aceptar"
      else:
        simbolo = cinta[cabezal]
        cinta[cabezal] = " "
        cabezal = len(cinta) - 2
        estado = "q1_" + simbolo
    elif estado.startswith("q1_"):
      if cinta[cabezal] == estado[3:]:
        cinta[cabezal] = " "
        cabezal -= 1
        estado = "q2"
      else:
        estado = "q_rechazar"
    elif estado == "q2":
      if cinta[cabezal] == " ":
        cabezal = 0
        estado = "q0"
      else:
        cabezal -= 1

  return estado == "q_aceptar"

#Cadena para saber si es palindromo
cadena = "Amo la paloma"
if turing_palindrome(cadena):
  print(f"'{cadena}' es un palíndromo.")
else:
  print(f"'{cadena}' no es un palíndromo.")