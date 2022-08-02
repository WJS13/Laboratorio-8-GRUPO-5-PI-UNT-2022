import csv

archivo=input("ingrese el nombre del archivo csv que desea que sea mostrado por el programa: ")
archivo+=".csv"

cuenta_columnas=open(archivo,"r")

primeralinea=cuenta_columnas.readline()
ncomas=int(primeralinea.count(","))
ncolumnas=ncomas+1

cuenta_columnas.close()


with open(archivo, "r") as file:
  reader = csv.reader(file, delimiter=',')

  listamain=[]
  for row in reader:
    listamain.append(row)


  Tabla = """{}"""

  if ncolumnas==1:
    Tabla = (Tabla.format('\n'.join("|| {:>15} ||".format(*fila) for fila in listamain)))
  elif ncolumnas==2:
    Tabla = (Tabla.format('\n'.join("|| {:>15} || {:>15} ||".format(*fila) for fila in listamain)))
  elif ncolumnas==3:
    Tabla = (Tabla.format('\n'.join("|| {:>15} ||{:>15} || {:>15} ||".format(*fila) for fila in listamain)))
  elif ncolumnas==4:
    Tabla = (Tabla.format('\n'.join("|| {:>15} ||{:>15} || {:>15} || {:>15} ||".format(*fila) for fila in listamain)))
  elif ncolumnas==5:
    Tabla = (Tabla.format('\n'.join("|| {:>15} ||{:>15} || {:>15} || {:>15} || {:>15} ||".format(*fila) for fila in listamain)))
  elif ncolumnas==6:
    Tabla = (Tabla.format('\n'.join("|| {:>15} ||{:>15} || {:>15} || {:>15} || {:>15} || {:>15} ||".format(*fila) for fila in listamain)))
  print(" ")
  print(Tabla)
  