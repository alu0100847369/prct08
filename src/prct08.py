#!/usr/bin/python
#!encoding:UTF-8
import sys
import modulo
  
argumentos = sys.argv[1:]
if (len(argumentos) == 8):
  n = int (argumentos[0])
  aproximaciones = int (argumentos[1])
  umbral = []
  for i in range (2,7):
    umbral.append(float(argumentos[i]))
  nombre_fichero = argumentos[7]
else:
  print "Introduzca el número de intervalos (n>0):"
  n = int (raw_input());
  print "Introduzca el número de aproximaciones:"
  aproximaciones = int (raw_input());
  print "Introduzca 5 umbrales de error: "
  umbral = []
  for i in range (5):
    print "Introduzca el umbral", i, ":"
    umbral.append(float (raw_input());
  print "Introduzca el nombre del fichero para almacenar los resultados:"
  nombre_fichero = raw_input();
if (n>0):
  try:
    fichero = open (nombre_fichero, "a")
  except:
    fichero = open (nombre_fichero, "n")
  fichero.write ("Nº de intervalos: %d\n" % (aproximaciones))
  for i in range (5):
    porcentaje = modulo.error (n, aproximaciones, umbral[i])
    fichero.write ("%2.2f%% de fallos para el umbral %2.5f\n" % (porcentaje, umbral[i]))
  fichero.close ()