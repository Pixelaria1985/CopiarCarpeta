import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Ruta de origen y destino
carpeta_origen = os.path.abspath("pepe")  # Se asume que está en la misma carpeta del script
ruta_destino = r"C:\xampp\htdocs\pepe"

def copiar_carpeta():
    if not os.path.exists(carpeta_origen):
        messagebox.showerror("Error", f"La carpeta de origen no existe:\n{carpeta_origen}")
        return

    if os.path.exists(ruta_destino):
        respuesta = messagebox.askyesno("Carpeta ya existe",
                                        "La carpeta ya existe en el destino.\n¿Deseas reemplazarla?")
        if respuesta:
            try:
                shutil.rmtree(ruta_destino)
                shutil.copytree(carpeta_origen, ruta_destino)
                messagebox.showinfo("Éxito", "La carpeta fue reemplazada con éxito.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo reemplazar la carpeta:\n{e}")
        else:
            messagebox.showinfo("Cancelado", "Operación cancelada por el usuario.")
    else:
        try:
            shutil.copytree(carpeta_origen, ruta_destino)
            messagebox.showinfo("Éxito", "La carpeta fue copiada con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo copiar la carpeta:\n{e}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Copiar Carpeta Pepe")
ventana.geometry("300x150")

# Botón para copiar la carpeta
boton_copiar = tk.Button(ventana, text="Copiar carpeta 'pepe'", command=copiar_carpeta, width=25, height=2)
boton_copiar.pack(pady=40)

# Ejecutar aplicación
ventana.mainloop()
