import csv
import pyttsx3

engine = pyttsx3.init()

def add(n):
    nombre = [None]*n
    edad = [None]*n
    dni = [None]*n
    for i in range(0,n):
        engine.say('Ingrese el nombre de la persona')
        engine.runAndWait()
        nombre[i] = input()
        engine.say('Ingrese la edad de la persona')
        engine.runAndWait()
        edad[i] = input()
        engine.say('Ingrese el DNI de la persona')
        engine.runAndWait()
        dni[i] = input()
        print('')
    
    with open('b-datos.csv','a',newline='') as file:
        writer = csv.writer(file, delimiter = ';')
        for i in range(0,n):
            writer.writerow([nombre[i],edad[i],dni[i]])

engine.say('¿Cuántas personas desea registrar?')
engine.runAndWait()
cantidad_de_personas = int(input())

print('')

with open('b-datos.csv','a',newline='') as file:
    writer = csv.writer(file, delimiter = ';')

with open('b-datos.csv','r',newline='') as file:
    reader = csv.reader(file, delimiter = ';')
    for i in reader:
        engine.say('Se sobreescribirán los datos existentes, ¿desea continuar?')
        engine.runAndWait()
        reinicio = input()
        if reinicio == 'si':
            print('')
            break
        elif reinicio == 'no':
            quit()
        else:
            engine.say('Respuesta inválida, se cerrará el programa')
            engine.runAndWait()
            quit()


with open('b-datos.csv','w',newline='') as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(['Nombre','Edad','DNI'])

add(cantidad_de_personas)
print('')

while 1>0:
    engine.say('¿Desea añadir más datos?')
    engine.runAndWait()
    respuesta = input()
    print('')
    if respuesta == 'si':
        engine.say('¿Desea cuántas personas?')
        engine.runAndWait()
        cantidad_de_personas_2 = int(input())
        print('')
        add(cantidad_de_personas_2)
        continue
    elif respuesta == 'no':
        quit()
    else:
        engine.say('Respuesta inválida, se cerrará el programa')
        engine.runAndWait()
        quit()