from win10toast import ToastNotifier
import datetime

Hora=int(input("Ingrese la hora: "))
Minuto=int(input("Ingrese los minutos: "))
Minuto-=5
Formato=input("AM/PM: ")

if Formato=="PM":
    Hora=Hora+12

while True:
    if Hora==datetime.datetime.now().hour and Minuto==datetime.datetime.now().minute:
        toaster = ToastNotifier()
        toaster.show_toast("ALARMA","Despiertaaaaa", icon_path="python_icon.ico", duration=5)