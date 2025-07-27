# %% [markdown]
# ### El siguiente script es el que usé para generar los enunciados en markdown. Está aquí solo como referencia, no es necesario ejecutarlo.

# %%
#import nbformat as nbf

# Leer el archivo de texto
    #with open("enunciados.txt", "r", encoding="utf-8") as f:
    #    lines = f.read().splitlines()

# Crear un nuevo notebook
    #nb = nbf.v4.new_notebook()

# Añadir cada línea como una celda Markdown
    #for i, line in enumerate(lines, start=1):
    #    if line.strip():  # si no está vacía
    #        nb.cells.append(nbf.v4.new_markdown_cell(f"### Enunciado {i}\n{line}"))

# Guardar como .ipynb
    #with open("Data_project_Python.ipynb", "w", encoding="utf-8") as f:
    #    nbf.write(nb, f)

# %% [markdown]
# ### Enunciado 1
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

# %%
#Pedimos cadena al usuario
cadena = (input("Ingrese texto: "))

#Definimos funcion
def frecuencias_letras(cadena):

    #Creamos diccionario vacio
    frecuencias = {}

    for letra in cadena:
        if letra != ' ':
            if letra not in frecuencias :
                frecuencias[letra] = 1
            else:
                frecuencias[letra] += 1
    return frecuencias

#Mostramos resultado
print(frecuencias_letras(cadena))

# %% [markdown]
# ### Enunciado 2
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

# %%
dada = input("Entra lista nums separada por comas: ")

lista_numeros = [int(x) for x in dada.split(',')] #Recorremos el input y creamos la lista tenieno en cuenta la coma

def doblar_valor(nums):

    return nums*2
    
map(doblar_valor, lista_numeros)
lista_resultado = list(map(doblar_valor, lista_numeros)) #Convertimos en lista el resultado de la función

print(f"Los dobles de la lista son: {lista_resultado} ")

# %% [markdown]
# ### Enunciado 3
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# %%
recibido = input("Entra texto: ")
objetivo = input("Entra objetivo: ")

lista = recibido.split() #La funcion split. ya crea una lista, no hace falta []

def comparacion_listas(rec, obj): 

    listaComparada = []

    for palabra in rec: #Por cada palabra buscar si el objetivo se encuentra dentro o no, si es asi
                        #añadirla a la nueva lista
        if obj in palabra:
            listaComparada.append(palabra)

    return listaComparada

listaFinal = comparacion_listas(lista,objetivo) 

print(listaFinal)



            





# %% [markdown]
# ### Enunciado 4
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

# %%
lista1=[11,22,13,14,15]
lista2=[45,34,58,66,16]

def diferencia(num1,num2): #Generemos la función de resta
    
    r = num2-num1

    return r

resultaDIF = list(map(diferencia, lista1, lista2)) #Realizamos la funció map para hacer la diferencia y convertir a lista

print(resultaDIF)

# %% [markdown]
# ### Enunciado 5
# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

# %%
notas=[5,6,4,3,7]

def notasClase (numeros,nota_aprobado=5): #Definimos funcion con dos parametros y uno configurado por defecto

    media = sum(numeros)/len(numeros)
    
    if media >= nota_aprobado:
        final = "aprobado"
    else:
        final = "suspendido"
    
    return (media, final) #Devolvemos la tupla 

calificacion = notasClase(notas) #Solo pasamos un parámetro ya que el otro es por defecto
print(calificacion)



# %% [markdown]
# ### Enunciado 6
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

# %%
def factorial(n):
    if n == 0 or n == 1:  # Caso base: factorial de 0 o 1 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Ejemplo:
print(factorial(5))  # Salida: 120


# %% [markdown]
# ### Enunciado 7 (CORREGIDO)
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

# %%
lista_tuplas = [("word1", "word2", "Word7"),("word3", "word4"),("word5",),("Word8",)]

# Función que une los elementos de la tupla en un solo string
def conversion(tupla):
    return " ".join(tupla)

# Aplicamos map para convertir cada tupla en un string
lista_strings = list(map(conversion, lista_tuplas))

print(lista_strings)


# %% [markdown]
# ### Enunciado 8
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

# %%


def es_entero(num):  #Creamos funcion para saber si se pueden convertir a floats lo recibido
        try:
            float(num)
            return True
        except ValueError:
            return False

num1 = (input("Entre primer numero: "))
num2 = (input("Entre numero para dividir: "))   

if not es_entero(num1) and not es_entero(num2):     #Imprimimos en el caso de que tengamos valuError en las entradas
        print("Ambos argumentos tiene un valor inapropiado.")
elif not es_entero(num1):
        print("El primer argumento tiene un valor inapropiado.")
elif not es_entero(num2):
        print("El segundo argumento tiene un valor inapropiado.")
else:    
    try:      #Si las entradas son numericas procedemos excepto cuando tenemos una division entre 0. informamos del resultado
        numero1 = float(num1)
        numero2 = float(num2)
        resultado = numero1/numero2
        print("El resultado de la división es: ", resultado)

    except ZeroDivisionError:
     print("No es posible dividir entre 0.")

        

    

# %% [markdown]
# ### Enunciado 9
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva listaexcluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

# %%
lista_mascotas = ["Perro", "Gato", "Tigre", "Hamster", "Cocodrilo", "Loro"]
lista_prohibida = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]



def no_prohibida (lista): #Definimos funcion que devuelva un true si la mascota no esta en la lista
    return lista not in lista_prohibida

resultado = list(filter(no_prohibida,lista_mascotas)) #Construimos lista filtrada
print(resultado)

# %% [markdown]
# ### Enunciado 10
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# %%
entrada = input("Ingresa lista separada por comas: ")

lista_numeros = [float(x) for x in entrada.split(',')] #Convertimos los datos entrados en numeros para evitar errores al hacer operaciones

class lista_vacia(Exception):
    pass

def promedio(elementos):
    if not elementos:
        raise lista_vacia("La lista enviada está vacía.")
    return sum(elementos) / len(elementos)
    
try:
    resultado = promedio(lista_numeros)
    print("El promedio es: ", resultado)
except lista_vacia as error:
    print(error)



# %% [markdown]
# ### Enunciado 11
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# %%


class not_in_range(Exception):
    pass

try:
    edad = input("Entre edad: ")
    edad = int(edad)  # Intentamos convertir a int el numero entrado

    if edad not in range(0,120): #levantamos excepcion creada fuera de rsango
            raise not_in_range("Edad fuera del rango 0-120.")
    
    print("Edad: ", edad, "año/s")

except ValueError:
    print("El argumento tiene un valor inapropiado.")
except not_in_range as error:
    print(error)



# %% [markdown]
# ### Enunciado 12 (CORREGIDO)
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

# %%
frase = input("Escribe una frase: ")
frase_dividida  = frase.split(" ") #Separamos la frase en palabras, utilizando los espacios de separador
print(frase)

# Función que devuelve la longitud de cada palabra
def longitudes(palabra):
    return len(palabra)

# Aplicamos map para obtener lista de enteros
resultado = list(map(longitudes, frase_dividida))

print(resultado)

# %% [markdown]
# ### Enunciado 13
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

# %%
caracteres = 'adriii'

def convertir(letra):
    return (letra.lower(), letra.upper())

def quitar_repetidos(cadena): #Quitamos duplicados manteniendo el orden
                    
    resultado = []
    for elemento in cadena: #Creamos una lista donde iremos guardando los elementos e ignorando si se repite uno de ellos
        if elemento not in  resultado:
            resultado.append(elemento)
    return resultado

caracteres = quitar_repetidos(caracteres)
lista_final = list(map(convertir, caracteres))
print(lista_final)


# %% [markdown]
# ### Enunciado 14 (CORREGIDO)
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

# %%
lista = ["zorro","pollo","manzana","zanahoria","pera"]

def comienzo (palabra):

    return palabra.startswith("z")

resultado = list(filter(comienzo,lista)) 

print(resultado)

# %% [markdown]
# ### Enunciado 15
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

# %%
lista = [5,4,3,2,1,-5]
"""Utilizamos una comprensión para hacer más compacta la función ya que utilizamos una lambda
como primer elemento escogemos la funcion aplicada a cada elemento de la lista que le daremos"""

listanueva = [(lambda x: x + 3)(x) for x in lista] 

print(list(listanueva))


# %% [markdown]
# ### Enunciado 16
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

# %%
cadena = "Hola soy Adrian y tengo 29 años"
n = int(4)

def palabras_largas (cadena,entero):
    """ -Creamos una funcion con dos paramentros
        -convertimes en lista la cadena de texto entregada para trabajar las palabras por separado
        -mediante filter, y una funcion lambda, filtramos que los elementos tengan mas largada que el 2do parametro
        -convertimos en lista los elementos filtrados
    """
    lista= cadena.split() #Convertim en una lista de palabras de la cadena

    filtrado = filter(lambda elemento: len(elemento) > entero ,lista)

    return list(filtrado)

resultado = palabras_largas(cadena,n)
print(resultado)


# %% [markdown]
# ### Enunciado 17
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

# %%
from functools import reduce

lista = [5,7,2,4]
""" Primero creamos una funcion siguiendo el modelo que aplica el reduce, es decir, aplica funcion a los dos primers
    y luego al resultado y el sigueinte elemento, entonces reducimos con la funcion con nuestro iterable """
def num_devuelto (x, y):
    
    return x * 10 + y

respuesta = reduce(num_devuelto,lista)
print (respuesta)

# %% [markdown]
# ### Enunciado 18
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

# %%
diccionario1 = dict(nombre='juan',edad=15, calificacion=90)
diccionario2 = dict(nombre='juana',edad=16, calificacion=45)
diccionario3 = dict(nombre='joan',edad=17, calificacion=23)

lista = [diccionario1,diccionario2,diccionario3]

def calificacion_mayor (diccionario):
    return diccionario["calificacion"] >= 90

excelentes = list(filter(calificacion_mayor, lista))

for diccionario in excelentes:
    print("Alumno excelente: ", diccionario)



# %% [markdown]
# ### Enunciado 19
# 19. Crea una función lambda que filtre los números impares de una lista dada.

# %%
lista = [2,3,5,4,6,7,9,10,9]
""" Generamos una funcion lambda para comprobar que el producto de la division de los parametros 
de la lista entre 2 sea diferente de 0, es decir, será impar, luego filtramos en el iterable que queramos"""
filtro = list(filter(lambda elemento: elemento % 2 != 0, lista))

print(filtro)

# %% [markdown]
# ### Enunciado 20
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

# %%
lista = ["hola",5,"noches",2,"buenas"]

def valor_int (lista):

    return isinstance(lista, int) #Comprobamos el tipo de valor que tiene el elemento de la lista, en este caso integer
                                    #Devuelve true o false
resultado = filter(valor_int, lista) #Filtramos los elemenetos de la lista que cumplan el isintance
print(list(resultado))


# %% [markdown]
# ### Enunciado 21
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

# %%
numero = 5

cubo = lambda x: x**3

resultado = cubo(numero)

print ("El cubo de: ", numero, "es", resultado)

# %% [markdown]
# ### Enunciado 22
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

# %%
from functools import reduce

lista = [1,2,3]

def producto(x,y):    
    return x * y

resultado = reduce(producto, lista)
print(resultado)


# %% [markdown]
# ### Enunciado 23
# 23. Concatena una lista de palabras.Usa la función reduce() .

# %%
lista = ["amor","odio","indiferencia"]

def concatenar (x,y):               #dentro de la funcion de dos variables le sumamos el espacio ya
                                    #que no se nos da este en la lista
      return x + " " + y

resultado = (reduce(concatenar,lista))
print(resultado)

# %% [markdown]
# ### Enunciado 24
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

# %%
# Lista de números
numeros = [10, 5, 7]

# Usamos reduce para restar todos los elementos en orden
diferencia_total = reduce(lambda x, y: x - y, numeros)

print(f"Diferencia total: {diferencia_total}")

# %% [markdown]
# ### Enunciado 25
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada. 

# %%
def contar_sin_espacios(cadena):
    contador = 0
    for caracter in cadena:
        if caracter != " ":
            contador += 1
    return contador

# Ejemplo
texto = "Hola me llamo Adrian"
print(contar_sin_espacios(texto))

# %% [markdown]
# ### Enunciado 26
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# %%
resto = lambda x, y: x % y

print(resto(5,3))

# %% [markdown]
# ### Enunciado 27 (CORREGIDO)
# 27. Crea una función que calcule el promedio de una lista de números.

# %%
from functools import reduce

lista = [1, 2, 3, 4, 5]


promedio = (reduce(lambda x, y: x + y, lista)) / len(lista)


print(f"El promedio es: {promedio}")

# %% [markdown]
# ### Enunciado 28 (CORREGIDO)
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# %%
lista = [1,2,3,4,"hola",3]

def duplicado(listado):

    for elemento in listado:
        if listado.count(elemento) > 1:
            return elemento

    return None

resultado = duplicado(lista)   
print(resultado if resultado is not None else "No hay duplicados")

# %% [markdown]
# ### Enunciado 29
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

# %%
variable1= "Asdfgh"
variable2= 12345643455

def convertidor(variable):

    cadena = str(variable)

    if len(cadena) <= 4:
        return cadena
    else:
        return "#" * (len(cadena) - 4) + cadena[-4:] #Utilizamos la inexacion de strings para coger rangos, 
     
                                                    #y empezamos el recuento de posicion por detrás
print(convertidor(variable2))

# %% [markdown]
# ### Enunciado 30
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

# %%
palabra1 = "ingenieRia"
palabra2 = "Geinrianie"

def anagrama (num1,num2):
                                #Creem una funció para comparar les paraules que ordenarem
                                # i ho posarem a minuscules i així veure 
                                #Si son iguals o no en les mateixes condicions
    a = sorted(num1.lower())
    b = sorted(num2.lower())
    if a == b:
        return "Es un anagrama"
    else:
        return "No es un anagrama"

print(anagrama(palabra1,palabra2))

# %% [markdown]
# ### Enunciado 31
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

# %%
lista = input("Ingrese lista separada por espacios: ").split(" ") #Amb split convertim en una llista per cada espai que posem
nombre = input("Ingrese nombre buscado: ")

class not_found(Exception):
    pass


try: 
    encontrado = False
    for elementos in lista:
        if elementos == nombre: #Recorremos todo el bucle, sin el brake el primer elemento que no coincidiese ya haria saltar la excepción pero sin revisar toda la lista.
           print("El nombre ",elementos, "ha sido encontrado")
           encontrado =True
           break
        
    if not encontrado:
        raise not_found("El nombre no ha sido encontrado.")

except not_found as error:
    print(error)

# %% [markdown]
# ### Enunciado 32
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

# %%



class Empleado:

    def __init__(self, nombre, apellido, posicion):
        self.nombre = nombre
        self.apellido = apellido
        self.posicion = posicion
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Empresa:
    
    def __init__(self, empleados):
        self.empleados = empleados

    def buscar_puesto(self, nombre_completo):
        for empleado in self.empleados:
            if empleado.nombre_completo() == nombre_completo:
                return f"{nombre_completo} trabaja como {empleado.posicion}."
        return f"{nombre_completo} no trabaja aquí."
    
empleados = [Empleado("Juan", "Rodriguez", "Mecanico"), Empleado("Juana", "Sanchez", "Ingeniera"), Empleado("Joan", "Mata", "Manager")]
empresa = Empresa(empleados)

    

print(empresa.buscar_puesto("Juan Rodriguez"))


print(empresa.buscar_puesto("Pedro Perez"))



# %% [markdown]
# ### Enunciado 33
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# %%
"""Utilizamos la funcion zip la cual combinaremos los elementos de las dos listas con el mismo indice"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

suma_listas = lambda lista1, lista2: [a + b for a, b in zip(lista1, lista2)]

resultado = suma_listas(lista1, lista2)
print(resultado)

# %% [markdown]
# ### Enunciado 34
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol. 
#     1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#     2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#     3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#     4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#     5. Implementar el método quitar_rama para eliminar una rama en una posición específica.

# %%
class Arbol:
    def __init__(self):
        # 1. Inicializar tronco con longitud 1 y lista vacía de ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # 2. Aumentar la longitud del tronco en 1
        self.tronco += 1

    def nueva_rama(self):
        # 3. Agregar una nueva rama de longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # 4. Aumentar en 1 la longitud de todas las ramas
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        # 5. Eliminar la rama en la posición dada si es válida
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida para quitar rama.")

    def info_arbol(self):
        # 6. Devolver información del árbol
        return (f"Longitud del tronco: {self.tronco}\n"
                f"Número de ramas: {len(self.ramas)}\n"
                f"Longitudes de las ramas: {self.ramas}")


# Caso de uso

arbol = Arbol()             # 1. Crear árbol
arbol.crecer_tronco()       # 2. Hacer crecer tronco una unidad
arbol.nueva_rama()          # 3. Añadir una nueva rama
arbol.crecer_ramas()        # 4. Hacer crecer todas las ramas una unidad
arbol.nueva_rama()          # 5. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.quitar_rama(2)        # 6. Retirar la rama en la posición 2
print(arbol.info_arbol())   # 7. Obtener información sobre el árbol




# %% [markdown]
# ### Enunciado 36
# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

# %%
class UsuarioBanco: 

                    #Recordar meter todos los metodos dentro de la clase. 

    def __init__(self, nombre, saldo, c_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.c_corriente = c_corriente

    def retirar_dinero(self, cantidad_restada):
        
        if cantidad_restada > self.saldo:
            raise Exception(f"{self.nombre} no tiene suficiente dinero para retirar.")
        
        self.saldo -= cantidad_restada

        print(f"{self.nombre} ha retirado {cantidad_restada}. El saldo actual es: {self.saldo}")    

    def transferir_dinero(self, cantidad_donada, persona):
        
        if cantidad_donada > self.saldo:
            raise Exception(f"{self.nombre} no tiene suficiente dinero para transferir.")
        elif persona.c_corriente == False:
            raise Exception(f"{persona.nombre} no tiene cuenta corriente. Por lo tanto {self.nombre} no puede transferir dinero.")
        
        self.saldo -= cantidad_donada
        persona.saldo += cantidad_donada    #Recordar poner el objeto instanciado pero también el atributo!

        print(f"{self.nombre} ha donado {cantidad_donada} a {persona.nombre}. Su saldo actual es: {self.saldo}")
        print(f"El saldo actual de {persona.nombre} será de {persona.saldo}")

    def agregar_dinero(self, cantidad_sumada):
    
        self.saldo += cantidad_sumada

        print(f"{self.nombre} ha ingresado {cantidad_sumada}. El saldo actual es: {self.saldo}") 

#Paso 1:
Alicia = UsuarioBanco("Alicia", 100, True)
Bob = UsuarioBanco("Bob", 50, True)

#Paso 2:
Bob.agregar_dinero(20)

#Paso 3:
Bob.transferir_dinero(80,Alicia)

#Paso 4:
Alicia.retirar_dinero(50)



"""
Probando código y todas sus posibilidades:

#Instanciamos los objetos, en este caso las personas
Adrian = UsuarioBanco("Adrian", 10000, True)
Mireia = UsuarioBanco("Mireia", 15000, True)
Ainhoa = UsuarioBanco("Ainhoa", 10000, False)
   
#Para envitar todo el traceback del error que saltará con la Exception, creamos el try:
try:
    Mireia.transferir_dinero(15000, Ainhoa)
except Exception as mensaje_error:
    print(mensaje_error) """

# %% [markdown]
# ### Enunciado 37
# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
#     1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
#     que devolver un diccionario.
#     2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
#     que devolver el texto con el remplazo de palabras.
#     3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
#     eliminada.
#     4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
#     número de argumentos variable según la opción indicada.

# %%
class ProcesadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palabras(self): #Dividimos el texto utilizando split (espacios por fdefectos) y guardamos junto con sus repeticiones
        palabras = self.texto.split()
        contador = {}
        for palabra in palabras:
            contador[palabra] = contador.get(palabra, 0) + 1
        return contador

    def reemplazar_palabras(self, palabra_original, palabra_nueva):
        return self.texto.replace(palabra_original, palabra_nueva)

    def eliminar_palabras(self, palabra_eliminar):
        palabras = self.texto.split()

        # Creamos una nueva lista con todas las palabras excepto la que queremos eliminar


        palabras_filtradas = [p for p in palabras if p != palabra_eliminar]

        # Unimos la lista en un nuevo texto sin la palabra eliminada

        return ' '.join(palabras_filtradas)

    def procesar_texto(self, opcion, *args):
        if opcion == "contar":
            return self.contar_palabras()

        # Si la opción es "reemplazar", revisa que se pasen 2 argumentos y llama a reemplazar_palabras()

        elif opcion == "reemplazar":
            if len(args) != 2:
                raise ValueError("Para 'reemplazar' se necesitan 2 argumentos: palabra_original y palabra_nueva.")
            return self.reemplazar_palabras(args[0], args[1])

        # Si la opción es "eliminar", revisa que se pase 1 argumento y llama a eliminar_palabras()
      

        elif opcion == "eliminar":
            if len(args) != 1:
                raise ValueError("Para 'eliminar' se necesita 1 argumento: palabra_a_eliminar.")
            return self.eliminar_palabras(args[0])

        else:
            raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

texto = "hola soy adrian, soy de girona y trabajo en riells en la provincia de girona"

procesador = ProcesadorTexto(texto)

# Contar palabras
print(procesador.procesar_texto("contar"))

# Reemplazar palabra
print(procesador.procesar_texto("reemplazar", "girona", "barcelona"))

# Eliminar palabra
print(procesador.procesar_texto("eliminar", "hola"))


# %% [markdown]
# ### Enunciado 38
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

# %%

def determinar_momento_del_dia(hora):
    if 6 <= hora < 12:
        return "Es de día (mañana)."
    elif 12 <= hora < 18:
        return "Es de tarde."
    elif 18 <= hora < 24:
        return "Es de noche."
    elif 0 <= hora < 6:
        return "Es de noche."
    else:
        return "Hora inválida."

try:
    hora_usuario = int(input("Introduce la hora en formato 24h (0-23): "))
    resultado = determinar_momento_del_dia(hora_usuario)
    print(resultado)
except ValueError:
    print("Por favor, introduce un número entero válido para la hora.")



# %% [markdown]
# ### Enunciado 39
# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:

# %%
def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Calificación inválida"

try:
    nota = int(input("Introduce la calificación del alumno (0-100): "))
    resultado = calificacion_texto(nota)
    print(f"La calificación es: {resultado}")
except ValueError:
    print("Por favor, introduce un número válido.")

# %% [markdown]
# ### Enunciado 40
# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

# %%
import math

def calcular_area(figura, datos):
    figura = figura.lower()
    if figura == "rectangulo":
        # datos = (base, altura)
        if len(datos) != 2:
            return "Datos insuficientes para rectángulo"
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        # datos = (radio,)
        if len(datos) != 1:
            return "Datos insuficientes para círculo"
        radio = datos[0]
        return math.pi * (radio ** 2)
    elif figura == "triangulo":
        # datos = (base, altura)
        if len(datos) != 2:
            return "Datos insuficientes para triángulo"
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no soportada"

# Ejemplos de uso
print(calcular_area("rectangulo", (5, 3)))   
print(calcular_area("circulo", (4,)))        
print(calcular_area("triangulo", (6, 2)))    


# %% [markdown]
# ### Enunciado 41
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
#     1. Solicita al usuario que ingrese el precio original de un artículo.
#     2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#     3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#     4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
#     5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#     6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
#     programa de Python.

# %%
def pedir_numero(cantidad):
    while True:
        try:
            return float(input(cantidad))
        except ValueError:
            print("Ingrese un número válido.")

def pedir_cupon(descuento):
    while True:
        respuesta = input(descuento)
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Responda con 'si' o 'no'.")

#Pedimos el precio con validación
precio_original = pedir_numero("Ingrese el precio original del artículo (€): ")

#Preguntamos si tiene cupón (con flexibilidad)
cupon_descuento = pedir_cupon("Tiene cupón de descuento? (si/no): ")

#Si tiene cupón, pedimos el valor y comprobamos
if cupon_descuento:
    valor_cupon = pedir_numero("Ingrese el valor del cupón (€): ")

    if valor_cupon > 0:
        precio_rebajado = precio_original - valor_cupon
        print(f"El precio final con descuento es: {precio_rebajado}€")
    else:
        print("El cupón no es válido (debe ser mayor que 0).")
else:
    print(f"No dispone de descuento. El precio sigue siendo: {precio_original:}€")




