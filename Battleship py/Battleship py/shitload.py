import random
import time
#---Declaracion de variables globales
    #---Matriz
matVisible = [[1,1,1,1,1,1],
              [1,1,1,1,1,1],
              [1,1,1,1,1,1],
              [1,1,1,1,1,1],
              [1,1,1,1,1,1],
              [1,1,1,1,1,1]]
matMostrar = [['#','#','#','#','#','#'],
              ['#','#','#','#','#','#'],
              ['#','#','#','#','#','#'],
              ['#','#','#','#','#','#'],
              ['#','#','#','#','#','#'],
              ['#','#','#','#','#','#']]
jugadores=[]
    #---Aqui se ejecutara todo el codigo
def main(fila, columna):
    matValores = GenerarMatrizRandom(fila, columna)
    Actualizar(fila,columna,matValores)
    aux = 1
    MasJugadores = 'si'
    while (MasJugadores.upper() == 'SI'):
        print(f"A continuación introdiusca el nombre del jugador #{aux:.0f}: " , end='')
        nombre = input()
        jugadores.append([nombre, 0])
        print("¿Hay más jugadores? ", end='')
        MasJugadores = input()
        aux += 1
    print("Este es el mapa de juego, selecciona la tarjeta que quieras girar")
    paresHechos=aux=0
    while(paresHechos < (fila * columna / 2) ):
        Actualizar(fila, columna, matMostrar)
        print("Es el turno de " + jugadores[aux][0])
        print("Seleccione la tarjeta #1")
        filaTarjeta1, columnaTarjeta1 = PedirTarjeta(fila, columna)
        GirarTarjeta(filaTarjeta1, columnaTarjeta1, matValores, True)
        Actualizar(fila, columna, matMostrar)
        print("Seleccione la tarjeta #2")
        filaTarjeta2, columnaTarjeta2 = PedirTarjeta(fila, columna)
        GirarTarjeta(filaTarjeta2, columnaTarjeta2, matValores, True)
        Actualizar(fila, columna, matMostrar)
        if(matValores[filaTarjeta1][columnaTarjeta1] == matValores[filaTarjeta2][columnaTarjeta2]):
            matMostrar[filaTarjeta1][columnaTarjeta1] = ' '
            matMostrar[filaTarjeta2][columnaTarjeta2] = ' '
            paresHechos += 1
            jugadores[aux][1] += 1
            print("Excelente " + jugadores[aux][0] + " tienes un par más")
            time.sleep(2)
            print("\n"*5)
        else:
            GirarTarjeta(filaTarjeta1, columnaTarjeta1, matValores, False)
            GirarTarjeta(filaTarjeta2, columnaTarjeta2, matValores, False)
            aux = (aux + 1) % len(jugadores)
            print("No has hecho pares, suerte para la proxima")
            time.sleep(2)
            print("\n"*5)
    Ganador()
    return

    #---Asigna los pares a la matriz, ya revueltos
def GenerarMatrizRandom(fila, columna):
    auxMatrizValores = [['','','','','',''], ['','','','','',''], 
                        ['','','','','',''], ['','','','','',''], 
                        ['','','','','',''], ['','','','','','']]
    pmin = 65
    pmax = int(pmin + fila * columna / 2)
    for ascii in range (pmin, pmax):
        valor = chr(ascii)
        for tarjeta in range (0,2):
            FilaTarjeta = random.randint(0, fila-1)
            ColumnaTarjeta = random.randint(0, columna-1)
            
            while (matVisible[FilaTarjeta][ColumnaTarjeta] == 0):
                FilaTarjeta = random.randint(0, fila-1)
                ColumnaTarjeta = random.randint(0, columna-1)

            matVisible[FilaTarjeta][ColumnaTarjeta] = 0
            auxMatrizValores[FilaTarjeta][ColumnaTarjeta] = valor
    return auxMatrizValores

    #---Muestra los valores de la matriz de forma correcta
def Actualizar(fila, columna, matriz):
    ancho = 5
    #---Esquinas
    esi = '╔' #--chr(201)
    esd = '╗' #--chr(187)
    eii = '╚' #--chr(200)
    eid = '╝' #--chr(188)
    #---Rectas
    hor = '═' #--chr(205)
    ver = '║' #--chr(186)
    #---In tersecciones
    hoi = '╦' #--chr(203)
    hos = '╩' #--chr(202)
    ved = '╠' #--chr(204)
    vei = '╣' #--chr(185)
    cen = '╬' #--chr(206)
    #---Parte superior
    print((' ' * 3) + (' ' * int( (ancho + 1) / 2 )) , end = '')
    for aux in range (0, columna):
        print( (str(aux)) + (' '*ancho) , end = '')
    print('\n', end = '')
    print( (' ' * 3 + esi) , end = '')
    for aux in range (0, columna-1):
        print( ( (hor * ancho) + hoi) , end = '')
    print( (hor * ancho) + esd)
     #---Parte del centro
    for auxf in range(0, fila):
        print((' ' + str(auxf)) , end = ' ')
        for aux in matriz[auxf]:
            print((ver + ' ' * int(ancho / 2) + str(aux) + ' ' * int(ancho / 2)) , end = '')
        print((ver + '\n' + ' ' * 3) , end = '')
        if(auxf != (fila - 1)):
            print(ved , end = '')
            for iaux in range(0, columna-1):
                print( ( (hor * ancho) +cen) , end = '')
            print( (hor * ancho) + vei)
    #---Parte inferior
    print(eii, end = '')
    for aux in range (0, columna-1):
        print( (hor * ancho + hos) , end = '')
    print(hor * ancho + eid)
    return

def PedirTarjeta(fila, columna):
    Posicion = []
    #---Fila de la tarjeta
    print("Indique la fila: " , end = '')
    FilaNueva = input()
    #---Comprobar que la Fila sea valida
    while(FilaNueva.isdigit() == False or
          int(FilaNueva) < 0 or 
          int(FilaNueva) >= fila):
        print("Hubo un error, esa fila esta fuera de rango")
        print("Indique la fila: " , end = '')
        FilaNueva = input()
    #---Columna de la tarjeta
    FilaNueva=int(FilaNueva)
    Posicion.append(FilaNueva)
    print("Indique la columna: " , end = '')
    ColumnaNueva = input()
    #---Comprobar que la Columna sea valida
    while(ColumnaNueva.isdigit() == False or
          int(ColumnaNueva) < 0 or 
          int(ColumnaNueva) >= columna):
        print("Hubo un error, esa columna esta fuera de rango")
        print("Indique la columna: " , end = '')
        ColumnaNueva = input()
    ColumnaNueva=int(ColumnaNueva)
    Posicion.append(ColumnaNueva)
    #---Verificar que la TARJETA sea valida
    if(matVisible[FilaNueva][ColumnaNueva] == 1):
        print("La tarjeta que quiere girar no esta disponible, intene una diferente")
        Posicion = PedirTarjeta(fila, columna)
    return Posicion

def GirarTarjeta(filaT, columnaT, valores, visibilidad):
    if(visibilidad == True):
        matMostrar[filaT][columnaT] = valores[filaT][columnaT]
        matVisible[filaT][columnaT] = 1
    else:
        matMostrar[filaT][columnaT] = '#'
        matVisible[filaT][columnaT] = 0
    return

def Ganador():
    puntosMaximos=0
    ganadores = []
    for aux in range (len(jugadores)):
        if(jugadores[aux][1] > puntosMaximos):
            puntosMaximos = jugadores[aux][1]
            ganadores = []
            ganadores.append(jugadores[aux][0])
        elif(jugadores[aux][1] == puntosMaximos):
            ganadores.append(jugadores[aux][0])
    
    if(len(ganadores) > 1):
        print('Hubo un empate entre:')
        for jugador in ganadores:
            print(jugador)
    else:
        print('El ganador absoluto es:')
        print(ganadores[0])
    return

main(6, 6)  #---Comienza la ejecucion del codigo