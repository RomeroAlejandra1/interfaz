import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def inicio():
    area_dinamica_limpia()
    
    tk.Label(area_dinamica, text="mensaje de bienvenida", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida", command=lambda: messagebox.showinfo("Bienvenida", "Hola, bienvenido al programa")).pack()
def alumno():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Aquí coloca un letrero o label que identifique al alumno", font=("Arial", 14)).pack(pady=10)
    tk.Label(area_dinamica, text="identificacion para el alumno alumno", font=("Arial", 14)).pack(pady=10)
    tk.Label(area_dinamica, text="Nombre del alumno:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Selección A:").pack()
    
    opcion_elegida = tk.StringVar(value="Masculino")
    tk.Radiobutton(area_dinamica, text="Masculino", variable=opcion_elegida, value="Masculino").pack()
    tk.Radiobutton(area_dinamica, text="Femenino", variable=opcion_elegida, value="Femenino").pack()
    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Uno", "Dos", "Tres"])
    tk.Label(area_dinamica, text="Semestre:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Primero", "Segundo", "Tercero", "Cuarto", "Quinto", "Sexto" ])
    combo.pack()
    combo.current(0)

    def accion_guardar():
  
        valor = campo_texto_uno.get()
        messagebox.showinfo("Revisión", f"Texto: {valor}\nSelección: {opcion_elegida.get()}\nLista: {combo.get()}")
        messagebox.showinfo("Revisión", f"Alumno: {valor}\nGenero: {opcion_elegida.get()}\nSemestre: {combo.get()}")
    tk.Button(area_dinamica, text="Botón 2", command=accion_guardar).pack(pady=10)
   

def color():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Cambio de color", font=("Arial", 14)).pack(pady=10)
    tk.Label(area_dinamica, text="aqui cambia el color", font=("Arial", 14)).pack(pady=10)
    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    colores = ["lightblue", "lightgreen", "lightyellow", "lightpink"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def cuestionario():
    area_dinamica_limpia()
    tk.Label(area_dinamica, text="Texto de ayuda que el alumno debe mejorar", font=("Arial", 14)).pack(pady=10)
    tk.Label(area_dinamica, text="Cuestionario para el alummo",font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def area_dinamica_limpia():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para prácticas")
ventana_principal.geometry("600x500")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="plum", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Inicio", command=inicio, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Datos del alumno", command=alumno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Cambiar color", command=color, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Visualizar cuestionario", command=cuestionario, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salida", command=ventana_principal.destroy, width=15).pack(pady=30)

inicio()
ventana_principal.mainloop()

