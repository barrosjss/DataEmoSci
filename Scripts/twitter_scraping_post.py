import re
from colorama import Fore
import requests

verde = Fore.GREEN
rojo = Fore.RED

web_site = "https://www.vulnhub.com"
resultado = requests.get(web_site)
contenido = resultado.text

patron = r"/entry/[\w-]*"

# re librería para expresiones regulares
maquina_repetida = re.findall(patron, str(contenido))
sin_duplicados = list(set(maquina_repetida))

maquina_final = []

for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "")
    maquina_final.append(nombre_maquinas)
    print(nombre_maquinas)

maquina_noob = "noob-1"
existe_noob = False

for a in maquina_final:
    if a == maquina_noob:
        existe_noob = True
        break

if existe_noob == True:
    print("\n" + verde + "No hay maquina nueva")
else:
    print("\n" + rojo + "Maquina nueva")
