import wikipedia as wk
import pyttsx3

wk.set_lang('es')

engine = pyttsx3.init()

def say(n):
    #dicta algo
    engine.say(n)
    engine.runAndWait()

def tema(n):
    #ingresa un tema, dicta una lista de 5 resultados y devuelve el resultado seleccionado
    temas = wk.search(n, results = 5)
    say('Los resultados son: ')
    for i in range(0,5):
        say(f'Resultado {i+1}')
        say(temas[i])
    say('¿Cuál de los 5 resultados desea? Mencione su elección escribiendo un número del 1 al 5')
    m = int(input(''))
    return temas[m-1]

def busca(n):
    #ingresa un término y devuelve su definición
    respuesta = wk.summary(n,sentences = 3)
    say(respuesta)

say('¿Qué desea buscar?')

try:
    busca(tema(input('')))
except:
    say('Ha ingresado un número inválido, vuelva a intentarlo')






