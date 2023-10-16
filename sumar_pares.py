# Definimos la función 'sumar_pares'.
def sumar_pares():
    # Inicializamos la variable 'suma' a 0 para almacenar la suma total.
    suma = 0
    
    # Usamos un bucle 'for' para iterar sobre los números del 2 al 100, con un paso de 2.
    # De esta forma, solo iteramos sobre los números pares, evitando la necesidad de comprobar si cada número es par.
    for x in range(2, 101, 2):
        # Sumamos el número par actual (x) a la variable 'suma'.
        suma += x
    
    # Imprimimos el resultado en la consola.
    print('La suma de todos los numeros pares de 1 a 100 es de:', suma)
    
    # Devolvemos el resultado para que pueda ser utilizado posteriormente si es necesario.
    return suma

# Llamamos a la función para ejecutarla y obtener el resultado.
sumar_pares()