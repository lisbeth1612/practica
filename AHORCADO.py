import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

obs = []
palabras = []
pista = []
intentos = 3
import csv 

with open('palabras.txt') as txtfile:
        reader = csv.DictReader(txtfile)
        for row in reader:
            palabras.append(row['palabras'])
            palabras.append(row['pista'])

'''
***********************************************
************ DEFINIENDO FUNCIONES *************
***********************************************      

'''
 
def Palabras_Aleatorias(lista):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(lista) - 1)
    return lista[palabraAleatoria]
 
def disparador_pantalla(AHORCADO, letra_equivocada, letra_Correcta, palabra_secreta):
    print(AHORCADO[len(letra_equivocada)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letra_equivocada:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabra_secreta)
    for i in range(len(palabra_secreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabra_secreta[i] in letra_Correcta:
            espacio = espacio[:i] + palabra_secreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")
 
def elijeLetra(cualquier_letra):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in cualquier_letra:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra
 
def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

'''
***********************************************
*********** BIENVENIDO AL AHORCADO*************
***********************************************      

'''
 
print ('A H O R C A D O')
letra_equivocada = ""
letra_Correcta = ""
palabra_secreta = Palabras_Aleatorias(palabras)
finJuego = False

while True:
    disparador_pantalla(AHORCADO, letra_equivocada, letra_Correcta, palabra_secreta)
    
    # El usuario elije una letra.
    letra = elijeLetra(letra_equivocada + letra_Correcta)
    if letra in palabra_secreta:
        letra_Correcta = letra_Correcta + letra
        # Se fija si el jugador ganó
        letrasEncontradas = True
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letra_Correcta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('¡Muy bien! La palabra secreta es "' + palabra_secreta + '"! ¡Has ganado!')
            finJuego = True
    else:
        letra_equivocada = letra_equivocada + letra
        # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
        if len(letra_equivocada) == len(AHORCADO) - 1:
            disparador_pantalla(AHORCADO, letra_equivocada, letra_Correcta, palabra_secreta)
            print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letra_equivocada)) + ' letras erroneas y ' + str(len(letra_Correcta)) + ' letras correctas, la palabra era "' + palabra_secreta + '"')
            finJuego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if finJuego:
        if empezar():
            letra_equivocada = ""
            letra_Correcta = ""
            finJuego = False
            palabra_secreta = Palabras_Aleatorias(palabras)
        else:
            break