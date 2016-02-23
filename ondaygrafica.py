##Importamos librerias necesarias para que el programa genere la grafica y audio, y archivemos el mismo.
##Ivan Herrera,Ximena Medina,Diego Lozano

import math
import matplotlib.pylab as plt


##Se crea una clase y un arreglo vacio por cada tipo de onda.

##Creamos la clase para el tipo de onda seno
class Seno:

##Creamos un arreglo vacio para la clase seno, el cual se llenara con los datos correspondientes
	wavearray = []

##Definimos el metodo constructor de la clase con los argumentos de entrada correspondientes
	def __init__(self, frecuencia, muestreo, bits, duracion):
            self.frecmuestreo = muestreo
            self.profundidadbits = bits
            self.frecuencia = frecuencia
            self.numerosamples = muestreo * duracion
            self.amplitud = (2**bits)/2
            self.pi=math.pi
##metodo correspondiente para generar el audio
	def Generarseno(self):

            for i in range(0, self.numerosamples):
                muestra = self.amplitud*math.sin((2*self.pi*self.frecuencia*i)/self.frecmuestreo)
                Seno.wavearray.append(muestra)

            return Seno.wavearray
##metodo correspondiente para graficar el audio
	def Graficar(self,array):
            plt.plot(array,color="blue",linewidth=1.0, linestyle="-")
            plt.show()


##Creamos la clase para el tipo de onda cuadrada
class Square:

##Creamos un arreglo vacio para la clase cuadrada , el cual se llenara con los datos correspondientes
        wavearray=[]

##Definimos el metodo constructor de la clase con los argumentos de entrada correspondientes
	def __init__(self, frecuencia, muestreo, bits, duracion):
            self.frecmuestreo = muestreo
            self.profundidadbits = bits
            self.frecuencia = frecuencia
            self.numerosamples = muestreo * duracion
            self.amplitud = (2**bits)/2
            self.pi = math.pi
##metodo correspondiente para generar el audio
	def Generarsquare(self):
            for i in range(0, self.numerosamples):
                muestra = self.amplitud*math.sin((2*self.pi*self.frecuencia*i)/self.frecmuestreo)
                if muestra<0:
                        muestra=(-(2**self.profundidadbits)/2)
                if muestra>0:
                        muestra=((2**self.profundidadbits)/2)
                Square.wavearray.append(muestra)

            return Square.wavearray
##metodo correspondiente para graficar el audio
	def Graficar(self,array):
            plt.plot(array,color="red",linewidth=1.0, linestyle="-")
            plt.show()

##Creamos la clase para el tipo de onda triangular
class Triangle:

##Creamos un arreglo vacio para la clase triangular, el cual se llenara con los datos correspondientes
        wavearray=[]

##Definimos el metodo constructor de la clase con los argumentos de entrada correspondientes
	def __init__(self, frecuencia, muestreo, bits, duracion):
            self.frecmuestreo = muestreo
            self.profundidadbits = bits
            self.frecuencia = frecuencia
            self.numerosamples = muestreo * duracion
            self.amplitud = (2**bits)/2
            self.pi = math.pi

##metodo correspondiente para generar el audio
	def Generartriangle(self):
            m=2*self.frecuencia*(2**self.profundidadbits)
            a=((2**self.profundidadbits)/2)
            s=0
            for i in range(0, self.numerosamples):
                muestra = self.amplitud*math.sin((2*self.pi*self.frecuencia*i)/self.frecmuestreo)
                s=s+m
                Triangle.wavearray.append(s)
                if (abs(muestra)==a):
                    m=-1*m

            return Triangle.wavearray

##metodo correspondiente para graficar el audio
	def Graficar(self):
            plt.plot(Triangle.wavearray,color="black",linewidth=1.0, linestyle="-")
            plt.show()

##Creamos la clase para el tipo de onda diente de sierra
class DienteSierra():

##Creamos un arreglo vacio para la clase diente de sierra, el cual se llenara con los datos correspondientes
        wavearray=[]

##Definimos el metodo constructor de la clase con los argumentos de entrada correspondientes
	def __init__(self, frecuencia, muestreo, bits, duracion):
            self.frecmuestreo = muestreo
            self.profundidadbits = bits
            self.frecuencia = frecuencia
            self.numerosamples = duracion * muestreo
            self.amplitud = (2**bits)/2
            self.pi = math.pi

##metodo correspondiente para generar el audio
	def Generardiente(self):
            m=self.frecuencia*(2**self.profundidadbits)
	    a=((2**self.profundidadbits)/2)
	    s=0
            for i in range(0, self.numerosamples):
                muestra = self.amplitud*math.sin((2*self.pi*self.frecuencia*i)/self.frecmuestreo)

		s=s+m
                DienteSierra.wavearray.append(s)
		if (muestra==a):
			s=(-(2**self.profundidadbits)/2)

            return DienteSierra.wavearray

##metodo correspondiente para graficar el audio
	def Graficar(self):
		plt.plot(DienteSierra.wavearray,color="green",linewidth=1.0, linestyle="-")
		plt.show()