import matplotlib.pyplot as plt      ##¡¡¡¡INSTALAR LIBRERIA ANTES DE EJECUTAR EL PROGRAMA!!!!!

def operacionAltura(cota, Vpos):
    return cota + Vpos

def operacionCota(alturaInstrumental, Vneg):
    return alturaInstrumental-Vneg


def dibujar(x, y):
    plt.plot(x, y, linewidth=2)
    plt.show()

def main():
    cota = []                   #Coordenadas en y a graficar
    distanciasAcumuladas = []  #Coordenas en x a graficar

    j = 1  #iterador para los puntos visados
    i = 0  #iterador del while, determina las armadas

    programa = int(input("(0) Para metodo de sube y baja \n(1) Para metodo cota y altura instrumental:\n "))

    #...................................METODO hi y COTA ...................................................

    if programa == 1:
        armadas = int(input("¿Cuantas armadas tiene?: "))

        while (i < armadas):

            print("-------------------------------Armada ", i+1 , " --------------------------------------")
            cantidadPM = int(input("¿Cuantos puntos intermedios tiene la armada?: "))

            #Primera cota conocida

            if i==0:
                cota.append(float(input("Ingrese la cota conocida:  ")))
                vpos = float(input("Ingrese V+ "))
                alturaInstrumentalAcumulada = operacionAltura(cota[i], vpos)
                D= float(input("Ingrese la distacia conocid0a:  "))   #Distancia inicial del armado
                dVpos = float(input("Ingrese la distacia dV+: "))
                distanciasAcumuladas.append(D-dVpos)

            #Primer punto visado (No existe en primer armado)

            if i>0:
                print('*********** Punto visado ',j,' ***********')
                print("Cota:",cota[-1])
                print("Distancia:", distanciasAcumuladas[-1])
                vpos = float(input("Ingrese V+ "))
                dVpos = float(input("Ingrese distancia al v+: "))
                alturaInstrumentalAcumulada = operacionAltura(cota[-1], vpos)
                D = distanciasAcumuladas[-1] + dVpos

            #Puntos Intermedios

            for k in range(0, cantidadPM):
                vneg = float(input("Ingrese Vi para el punto intermedio "))
                cota.append(operacionCota(alturaInstrumentalAcumulada, vneg))
                dvneg = float(input("Ingrese la distancia del vi para este punto visado del armado: "))
                op = int(input("(1) Para un punto intermedio adelante del armado \n(0) Para un punto intermedio atras del armado: "))
                if op == 1:
                    distanciasAcumuladas.append(D + dvneg)
                elif op == 0:
                    distanciasAcumuladas.append(D - dvneg)
                else:
                    print("Opcion no valida, por favor reinicie el programa")

            # Segundo punto visado

            print('***********Punto visado ', j+1, ' ***********')
            vneg = float(input("Ingrese V- para este punto visado del armado: "))
            cota.append(operacionCota(alturaInstrumentalAcumulada, vneg))
            dVneg = float(input("Ingrese la distancia (dV-) para este punto visado del armado: "))
            distanciasAcumuladas.append(D + dVneg)

            i+=1

            print("Distancias: ",distanciasAcumuladas)
            print("Cotas: ",cota)

        dibujar(distanciasAcumuladas,cota)  ##Una vez calculadas las cotas y las distancias se mandan al metodo dibujar

    #......................................METODO SUBE Y BAJA..........................................

    elif programa == 0:
        armadas = int(input("¿Cuantas armadas tiene?: "))

        while (i < armadas):

            print("----------------Aramada ",i+1,"-----------------------")

            #Primera iteracion pide cota
            if i==0:
                cota.append(float(input("Ingrese la cota conocida:  ")))

            vpos = float(input("Ingrese V+ "))

            #Siguientes iteraciones toman la cota anterior
            if i >0:
                print("Cota ", cota[-1])
            cantidadPM = int(input("¿Cuantos puntos intermedios tiene la armada?: "))
            for k in range(0, cantidadPM): #Iteracion puntos intermedios
                vneg = float(input("Ingrese Vi para el punto  "))
                sb = vpos - vneg
                if i > 0:
                    if c == False:
                        cotas = cota[-1]
                        print("Cota:",cotas)
                        cota.append(cotas + sb)
                        c = True
                    else:
                        print("Cota:", cotas)
                        cota.append(cotas + sb)
                else:
                    cota.append(cota[0] + sb)

            c = False
            print("***Punto visualizado final***")
            vneg = float(input("Ingrese V- para el punto  "))
            sb = vpos - vneg
            if i > 0:
                cota.append(cotas + sb)
            else:
                cota.append(cota[0] + sb)

            i+=1

            print("Cotas al momento: ",cota)

        print("\nCOTAS TOTALES: ", cota)

if __name__ == '__main__':
    main()