#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la librería csv respectivamente
#from test import tester
import csv

"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)



"""Fin espacio para programar funciones propias"""

#def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
import pandas as pd
import numpy as np
import statistics
    
archivo = 'BTC-USD.csv'
df = pd.read_csv(archivo)

indice=np.arange(0, len(df))
fecha=df.iloc[:, 0]
entrada=df.iloc[:, 1]
salida=df.iloc[:, 4]
variacion=salida-entrada
descripcion=[]

for i in range(0,len(variacion)):
    if variacion[i]<0:
        descripcion.append('Baja')
    if variacion[i]>0:
        descripcion.append('Sube')
    if variacion[i]==0:
        descripcion.append('Estable')


Titulos=['Indice','Fecha','Open','Close','Variacion_diaria','Descripcion']
documento=np.transpose([indice,fecha,entrada,salida,variacion,descripcion ])
#documento= documento.tolist()
doc= pd.DataFrame(documento)

menor_precio=min(df.iloc[:, 3])

fecha_menor_precio=np.where(df.iloc[:, 3]==menor_precio)
fecha_menor_precio=(df.iloc[fecha_menor_precio[0], 0])
fecha_menor_precio=fecha_menor_precio.to_string()
fecha_menor_precio=fecha_menor_precio[len(fecha_menor_precio)-10:len(fecha_menor_precio):1]

mayor_precio=max(df.iloc[:, 2])

fecha_mayor_precio=np.where(df.iloc[:, 2]==mayor_precio)
fecha_mayor_precio=(df.iloc[fecha_mayor_precio[0], 0])
fecha_mayor_precio=fecha_mayor_precio.to_string()
fecha_mayor_precio=fecha_mayor_precio[len(fecha_mayor_precio)-10:len(fecha_mayor_precio):1]

variacion_diaria_media=statistics.mean(variacion)

doc.to_csv('analisis_bitcoin.csv',sep=';',header=Titulos,index=False)


print('el menor precio registrado fue {} en la fecha {}'.format(menor_precio,fecha_menor_precio))
print('el mayor precio registrado fue {} en la fecha {}\n'.format(mayor_precio,fecha_mayor_precio))

print(fecha_menor_precio, menor_precio, fecha_mayor_precio, mayor_precio, variacion_diaria_media)


    #return df#fecha_menor_precio, menor_precio, fecha_mayor_precio, mayor_precio, variacion_diaria_media

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED DESARROLLE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#df=tester(solucion)
#df=solucion()
