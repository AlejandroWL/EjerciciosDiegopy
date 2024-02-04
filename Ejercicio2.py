def es_par(numero):
  """
  Esta función determina si un número es par o impar.

  Parámetros:
    numero: El número que se desea evaluar.

  Retorno:
    True si el número es par, False si es impar.
  """

  resto = numero % 2
  return resto == 0

numero = int(input("Ingresee un número: "))

if es_par(numero):
  print("El número", numero, "es par.")
else:
  print("El número", numero, "es impar.")
