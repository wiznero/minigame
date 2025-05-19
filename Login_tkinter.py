import tkinter as tk
import sqlite3
from PIL import Image,ImageTk


# creacion/conexion de la base de datos
conn = sqlite3.connect("jugadores.db")
# creo el cursor
cursor = conn.cursor()

#crear la tabla para almacenar datos

cursor.execute("""
CREATE TABLE IF NOT EXISTS jugadores (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               puntuacion INTEGER DEFAULT 0)
""")

conn.commit()

# lista de preguntas
preguntas = [
    {
        "pregunta": "¿Cual es la capital de Portugal?",
        "opciones": {"A": "Madrid", "B": "Lisboa", "C": "rio de janeiro"},
        "respuesta": "B"
    },
    {
        "pregunta": "¿Cual es la capital de Turquia?",
        "opciones": {"A": "Sevilla", "B": "Estambul", "C": "Ankara"},
        "respuesta": "C"
    },
    {
        "pregunta": "¿Cual es la capital de Croacia?",
        "opciones": {"A": "Zagreb", "B": "Dubrovnik", "C": "Sofia"},
        "respuesta": "A"
    }
]

# PATATAS FRITAS
def comenzar_juego():
    nombre = entrada_nombre.get().strip()
    if nombre:
        cursor.execute("INSERT INTO jugadores (nombre,puntuacion) VALUES (?, ?)",(nombre,0))
        conn.commit()
        root.destroy() # esto oculta la ventana principal
        mostrar_pregunta1(nombre,0)

    else:
        label_mensaje.config(text="Por favor introduce un nombre")

# funcion para mostrar la pregunta 1
def mostrar_pregunta1(nombre_jugador,indice):
    if indice >= len(preguntas):
        print("juego acabado")
        return
    
    datos = preguntas[indice]
    ventana = tk.Tk()
    ventana.title(f"Pregunta {indice + 1}")
    ventana.geometry("400x250")

    def responder(eleccion):
        if eleccion == datos["respuesta"]:
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 100 WHERE nombre = ?", (nombre_jugador,))
            conn.commit()
        ventana.destroy()
        mostrar_pregunta2(nombre_jugador, indice + 1)

    # mostramos la pregunta con sus posibles respuestas
    tk.Label(ventana,text=datos["pregunta"],font=("Arial",14)).pack(pady=20)

    # los botones
    for clave,valor in datos["opciones"].items():
        texto = f"{clave} {valor}"
        tk.Button(ventana,text=texto, command=lambda:responder(clave),width=30).pack(pady=5)

# mostrar pregunta 2
def mostrar_pregunta2(nombre_jugador,indice):
    if indice >= len(preguntas):
        print("juego acabado")
        return
    
    datos = preguntas[indice]
    ventana = tk.Tk()
    ventana.title(f"Pregunta {indice + 1}")
    ventana.geometry("400x250")

    def responder(eleccion):
        if eleccion == datos["respuesta"]:
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 100 WHERE nombre = ?", (nombre_jugador,))
            conn.commit()
        ventana.destroy()
        mostrar_pregunta2(nombre_jugador, indice + 1)

    # mostramos la pregunta con sus posibles respuestas
    tk.Label(ventana,text=datos["pregunta"],font=("Arial",14)).pack(pady=20)

    # los botones
    for clave,valor in datos["opciones"].items():
        texto = f"{clave} {valor}"
        tk.Button(ventana,text=texto, command=lambda:responder(clave),width=30).pack(pady=5)

        






# cracion de la ventana principal
root = tk.Tk()
root.title("Login del juego")
root.geometry("300x300")


# Widgets
label_titulo = tk.Label(root,text="Introduce tu nombre", font=("Minion Pro Med",14))
label_titulo.pack(pady=10)
# cuadro entrada de texto
entrada_nombre = tk.Entry(root,font=("Minion Pro Med",14))
entrada_nombre.pack(pady=10)

#primer boton
boton_comenzar = tk.Button(root,text="COMENZAR",font=("Minion Pro Med",14), command=comenzar_juego)
boton_comenzar.pack(pady=10)

# creo un label para informar de que no se ha introducido un nombre
label_mensaje = tk.Label(root,text="",fg="red", font=("Minion Pro Med",14))
label_mensaje.pack(pady=10)

#mantengo la ventana abierta
root.mainloop()





