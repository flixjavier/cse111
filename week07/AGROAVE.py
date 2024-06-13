import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, Entry, Text
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
import csv
from datetime import datetime
import random
import qrcode
import json
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm

CSV_FILE = "agroaveRemisiones.csv"

RANDOM_AVERAGE_ONIONS_WEIGTH = random.uniform(424, 430)

CLIENTS_LIST = ["Rio Fresh Inc", "JF Palmer and Sons Produce", "Diego Romero", "AgroFlores", "Abraham Gonzalez", "Pedro Salmerón"]

DESTINO_LIST = ["205 W Express Way 84, Donna Tx", "900 West Highway, San Juan Tx", "6ta #340 Int. 59, Centrom Tijuana B.C.", "Ejido Emiliano Carranza Km 65, Llera de Canales, Tamaulipas", "2501 W Military Hwy C-25, McAllen Tx"]

ONIONS_LIST = ["Cebolla Blanca", "Cebolla Amarilla", "Cebolla Morada"]

def main():
  # Create the main window
  root = tk.Tk()
  frm_main = Frame(root)
  frm_main.master.title("AGRO AVE")
  frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1) #this manage all the layout using frm_main

  #Size of window 
  #frm_main.master.geometry("1000x1000")

  #populate main Window
  populate_main_window(frm_main)

  # Run the application
  root.mainloop()

#function used to test if every entry is empty
def is_empty(value):
    return value == ''

#get the current date to be appended to the document
def get_formatted_date():
    return datetime.now().strftime('%d/%m/%Y')

#fucntion used in the bins weigth calculator
def calculate_weigth(bins, onions_weigth):
  weigth = onions_weigth * bins
  return weigth

#Check if a key is in csv

def check_key_in_csv(file_path, key):
  try:  
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if key in row:
                return True
    return False
  except Exception as exc:
    messagebox.showerror("Error", f"Se produjo un Error: {exc}")


#create the window with all the entries and labels using Tkinder
def populate_main_window(frm_main):
  
  # Add a title inside the window
  title_label = Label(frm_main, text="Remisiones AGROAVE", font=("Helvetica", 24))

  #labels and entry widgets for bins calculator
  label_numero_bins = Label(frm_main, text="Número de Bins:")
  entry_numero_bins = Entry(frm_main)

  label_resultado_peso = Label(frm_main, text="Peso (Kg):")
  label_resultado_peso_display = Label(frm_main)

  #create calculate button
  calculate_button = Button(frm_main, text="Calcular")

  #create Label and entry file name

  label_file_name = Label(frm_main, text="Nombre de archivo QR:")
  entry_file_name = Entry(frm_main)
  
  # Create labels and entry widgets
  label_remision_numero = Label(frm_main, text="Remisión (REMXXXX):")
  entry_remision_numero = Entry(frm_main)

  label_nombre_cliente = Label(frm_main, text="Cliente:")
  entry_nombre_cliente = Combobox(frm_main, values= CLIENTS_LIST)

  label_destino = Label(frm_main, text="Destino:")
  entry_destino = Combobox(frm_main, values= DESTINO_LIST)

  label_producto = Label(frm_main, text="Producto:")
  entry_producto = Combobox(frm_main, values= ONIONS_LIST)

  label_producto_descripcion = Label(frm_main, text="Descripción:")
  entry_producto_descripcion = Text(frm_main, height=4, width=40)

  label_total = Label(frm_main, text="Total:")
  entry_total_producto = Entry(frm_main)

  label_fletera = Label(frm_main, text="Fletera:")
  entry_fletera = Entry(frm_main)

  label_conductor = Label(frm_main, text="Conductor:")
  entry_conductor = Entry(frm_main)

  label_telefono_conductor = Label(frm_main, text="Teléfono:")
  entry_telefono_conductor = Entry(frm_main)

  label_fecha_embarque = Label(frm_main, text="Fecha embarque:")
  entry_fecha_embarque = DateEntry(frm_main, width=12, background='white',foreground='darkblue', borderwidth=2, date_pattern='dd/MM/yyyy')

  label_fecha_entrega = Label(frm_main, text="Fecha entrega:")
  entry_fecha_entrega = DateEntry(frm_main, width=12, background='white',foreground='darkblue', borderwidth=2, date_pattern='dd/MM/yyyy')

  label_marca_camion = Label(frm_main, text="Marca camión:")
  entry_marca_camion = Entry(frm_main)

  label_placas_tractor = Label(frm_main, text="Placas tractor:")
  entry_placas_tractor = Entry(frm_main)

  label_placas_cajas = Label(frm_main, text="Placas cajas:")
  entry_placas_cajas = Entry(frm_main)

  label_modelo_camion = Label(frm_main, text="Modelo:")
  entry_modelo_camion = Entry(frm_main)

  label_color_camion = Label(frm_main, text="Color:")
  entry_color_camion = Entry(frm_main)

  label_numero_economico = Label(frm_main, text="Número Economico:")
  entry_numero_economico = Entry(frm_main)

  label_longitud = Label(frm_main, text="Longitud:")
  entry_longitud = Entry(frm_main)

  label_flete = Label(frm_main, text="Flete: $")
  entry_flete = Entry(frm_main)

  label_cuota_tonelada = Label(frm_main, text="Cuota tonelada: $")
  entry_cuota_tonelada = Entry(frm_main)

  label_peso = Label(frm_main, text="Peso (Kg):")
  entry_peso = Entry(frm_main)

  label_precio = Label(frm_main, text="Precio: $")
  entry_precio = Entry(frm_main)

  label_codigo_alfa = Label(frm_main, text="Codigo ALFA:")
  entry_codigo_alfa = Entry(frm_main)

  label_codigo_caat = Label(frm_main, text="Codigo CAAT:")
  entry_codigo_caat = Entry(frm_main)

  label_firma = Label(frm_main, text="Firma:")
  entry_firma = Entry(frm_main)

  # Create a submit button
  submit_button = Button(frm_main, text="Guardar")

  #Layout  Weight calculator 
  title_label.grid(               row=0, column=0, columnspan=4, pady=10)
  label_remision_numero.grid(     row=1, column=0, padx=10, pady=5)
  entry_remision_numero.grid(     row=1, column=1, padx=10, pady=5)
  label_numero_bins.grid(         row=1, column=2, padx=10, pady=5)
  entry_numero_bins.grid(         row=1, column=3, padx=10, pady=5)
  label_resultado_peso.grid(      row=2, column=2, padx=10, pady=5)
  label_resultado_peso_display.grid(row=2, column= 3, padx=10, pady=5)
  label_file_name.grid(           row=4, column=2, padx=10, pady=5)
  entry_file_name.grid(           row=4, column=3, padx=10, pady=5)

  #layout of the rest of the form
  label_nombre_cliente.grid(      row=2, column=0, padx=10, pady=5)
  entry_nombre_cliente.grid(      row=2, column=1, padx=10, pady=5)

  label_destino.grid(             row=3, column=0, padx=10, pady=5)
  entry_destino.grid(             row=3, column=1, padx=10, pady=5)
  label_producto.grid(            row=4, column=0, padx=10, pady=5)
  entry_producto.grid(            row=4, column=1, padx=10, pady=5)
  label_producto_descripcion.grid(row=5, column=0, padx=10, pady=5)
  entry_producto_descripcion.grid(row=5, column=1, padx=10, pady=5)
  label_total.grid(               row=6, column=0, padx=10, pady=5)
  entry_total_producto.grid(      row=6, column=1, padx=10, pady=5)
  label_fletera.grid(             row=6, column=2, padx=10, pady=5)
  entry_fletera.grid(             row=6, column=3, padx=10, pady=5)
  label_conductor.grid(           row=7, column=0, padx=10, pady=5)
  entry_conductor.grid(           row=7, column=1, padx=10, pady=5)
  label_telefono_conductor.grid(  row=7, column=2, padx=10, pady=5)
  entry_telefono_conductor.grid(  row=7, column=3, padx=10, pady=5)
  label_fecha_embarque.grid(      row=8, column=0, padx=10, pady=5)
  entry_fecha_embarque.grid(      row=8, column=1, padx=10, pady=5)
  label_fecha_entrega.grid(       row=8, column=2, padx=10, pady=5)
  entry_fecha_entrega.grid(       row=8, column=3, padx=10, pady=5)
  label_marca_camion.grid(        row=9, column=0, padx=10, pady=5)
  entry_marca_camion.grid(        row=9, column=1, padx=10, pady=5)
  label_placas_tractor.grid(      row=10, column=0, padx=10, pady=5)
  entry_placas_tractor.grid(      row=10, column=1, padx=10, pady=5)
  label_placas_cajas.grid(        row=11, column=0, padx=10, pady=5)
  entry_placas_cajas.grid(        row=11, column=1, padx=10, pady=5)
  label_modelo_camion.grid(       row=12, column=0, padx=10, pady=5)
  entry_modelo_camion.grid(       row=12, column=1, padx=10, pady=5)
  label_color_camion.grid(        row=13, column=0, padx=10, pady=5)
  entry_color_camion.grid(        row=13, column=1, padx=10, pady=5)
  label_numero_economico.grid(    row=14, column=0, padx=10, pady=5)
  entry_numero_economico.grid(    row=14, column=1, padx=10, pady=5)
  label_longitud.grid(            row=15, column=0, padx=10, pady=5)
  entry_longitud.grid(            row=15, column=1, padx=10, pady=5)
  label_flete.grid(               row=9, column=2, padx=10, pady=5)
  entry_flete.grid(               row=9, column=3, padx=10, pady=5)
  label_cuota_tonelada.grid(      row=11, column=2, padx=10, pady=5)
  entry_cuota_tonelada.grid(      row=11, column=3, padx=10, pady=5)
  label_peso.grid(                row=12, column=2, padx=10, pady=5)
  entry_peso.grid(                row=12, column=3, padx=10, pady=5)
  label_precio.grid(              row=13, column=2, padx=10, pady=5)
  entry_precio.grid(              row=13, column=3, padx=10, pady=5)
  label_codigo_alfa.grid(         row=14, column=2, padx=10, pady=5)
  entry_codigo_alfa.grid(         row=14, column=3, padx=10, pady=5)
  label_codigo_caat.grid(         row=15, column=2, padx=10, pady=5)
  entry_codigo_caat.grid(         row=15, column=3, padx=10, pady=5)
  label_firma.grid(               row=16, column=0, padx=10, pady=5)
  entry_firma.grid(               row=16, column=1, padx=10, pady=5)
  submit_button.grid(             row=16, column= 2, columnspan=6, pady=10)
  calculate_button.grid(          row=3, column=2, columnspan=6, pady=10)

  #function to submit the information into the CSV file
  def submit_info():
    formatted_date = get_formatted_date()

    #variables para remision
    remision_numero = entry_remision_numero.get()
    nombre_cliente = entry_nombre_cliente.get()
    destino = entry_destino.get()
    producto = entry_producto.get()
    producto_descripcion = entry_producto_descripcion.get("1.0", tk.END).strip()
    total_producto = entry_total_producto.get()
    fletera = entry_fletera.get()
    conductor = entry_conductor.get()
    telefono_conductor = entry_telefono_conductor.get()
    fecha_embarque = entry_fecha_embarque.get()
    fecha_entrega = entry_fecha_entrega.get()
    marca_camion = entry_marca_camion.get()
    placas_tractor = entry_placas_tractor.get()
    placas_cajas = entry_placas_cajas.get()
    modelo_camion = entry_modelo_camion.get()
    color_camion = entry_color_camion.get()
    numero_economico = entry_numero_economico.get()
    longitud_camion = entry_longitud.get()
    costo_flete = entry_flete.get()
    cuota_tonelada = entry_cuota_tonelada.get()
    peso_carga = entry_peso.get()
    precio_carga = entry_precio.get()
    codigo_alfa = entry_codigo_alfa.get()
    codigo_caat = entry_codigo_caat.get()
    nombre_firma = entry_firma.get()

    #This variable is used to focus into an entry if is empty 
    variables_dict = {
      'remision_numero': (remision_numero, entry_remision_numero),
      'nombre_cliente': (nombre_cliente, entry_nombre_cliente),
      'destino': (destino, entry_destino),
      'producto': (producto, entry_producto),
      'producto_descripcion': (producto_descripcion, entry_producto_descripcion),
      'total_producto': (total_producto, entry_total_producto),
      'fletera': (fletera,entry_fletera),
      'conductor': (conductor, entry_conductor),
      'telefono_conductor': (telefono_conductor, entry_telefono_conductor),
      'fecha_embarque': (fecha_embarque, entry_fecha_embarque),
      'fecha_entrega': (fecha_entrega, entry_fecha_entrega),
      'marca_camion': (marca_camion, entry_marca_camion),
      'placas_tractor': (placas_tractor, entry_placas_tractor),
      'placas_cajas': (placas_cajas, entry_placas_cajas),
      'modelo_camion': (modelo_camion, entry_modelo_camion),
      'color_camion': (color_camion, entry_color_camion),
      'numero_economico': (numero_economico, entry_numero_economico),
      'longitud_camion': (longitud_camion, entry_longitud),
      'costo_flete': (costo_flete, entry_flete),
      'cuota_tonelada': (cuota_tonelada, entry_cuota_tonelada),
      'peso_carga': (peso_carga, entry_peso),
      'precio_carga': (precio_carga, entry_precio),
      'codigo_alfa': (codigo_alfa, entry_codigo_alfa),
      'codigo_caat': (codigo_caat, entry_codigo_caat),
      'nombre_firma': (nombre_firma, entry_firma)
    } 

    #data used to create the QR image
    qr_code_data = {
      'remision_numero': remision_numero,
      'nombre_cliente': nombre_cliente,
      'destino': destino,
      'producto': producto,
      'producto_descripcion': producto_descripcion,
      'total_producto': total_producto,
      'fletera': fletera,
      'conductor': conductor,
      'telefono_conductor': telefono_conductor,
      'fecha_embarque': fecha_embarque,
      'fecha_entrega': fecha_entrega,
      'marca_camion': marca_camion,
      'placas_tractor': placas_tractor,
      'placas_cajas': placas_cajas,
      'modelo_camion': modelo_camion,
      'color_camion': color_camion,
      'numero_economico': numero_economico,
      'longitud_camion': longitud_camion,
      'costo_flete': costo_flete,
      'cuota_tonelada': cuota_tonelada,
      'peso_carga': peso_carga,
      'precio_carga': precio_carga,
      'codigo_alfa': codigo_alfa,
      'codigo_caat': codigo_caat,
      'nombre_firma': nombre_firma,
    } 
  
    #for loop to check if a entry is empty
    for key, (value, entry) in variables_dict.items():
      if is_empty(value):
        messagebox.showerror("Error", "Por favor, complete todos los campos")
        entry.focus()
        return
      
    if check_key_in_csv(CSV_FILE, remision_numero):
      messagebox.showinfo("Error", "Número de Remisión ya ingresado. Ingresar un folio Distinto")
      entry_remision_numero.focus()

    else:
      confirmation_message = f'Número Remisión: {"REM" + remision_numero}, Cliente: {nombre_cliente}\n Destino: {destino}\nProducto: {producto}\n Descripción: {producto_descripcion}\nTotal: {total_producto}\n Fletera: {fletera}\n Conductor: {conductor}\n Teléfono conductor: {telefono_conductor}\n Fecha embarque: {fecha_embarque}\n Fecha entrega: {fecha_entrega}\n Marca Camión: {marca_camion}\n Color camión: {color_camion}\n Número económico: {numero_economico}\n Longitud camión: {longitud_camion}\n Costo flete: {costo_flete}\n Cuota tonelada: {cuota_tonelada}\n Peso carga: {peso_carga}\n Precio carga: {precio_carga}\n Codigo ALFA: {codigo_alfa}\n Codigo CAAT: {codigo_caat}\n Firma: {nombre_firma}\n Es esta información correcta?'

      if messagebox.askokcancel("Confirmación de Informacion", confirmation_message):
        try: 
          # Convert dictionary to JSON string
          data_json = json.dumps(qr_code_data)

          #file name
          file_name = entry_file_name.get()

          qr_code(data_json, file_name)

          # Append to CSV file
          with open(CSV_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([formatted_date, remision_numero, nombre_cliente, destino, producto, producto_descripcion, total_producto, fletera, conductor, telefono_conductor, fecha_embarque, fecha_entrega, marca_camion, placas_tractor, placas_cajas, modelo_camion, color_camion, numero_economico, longitud_camion, costo_flete, cuota_tonelada, peso_carga, precio_carga, codigo_alfa, codigo_caat, nombre_firma])
          messagebox.showinfo("Exito", "Su información a sido guardado exitosamente!")
          clear_entries()

          #This code add the info to a doc file and save a file with a new name

          doc = DocxTemplate("remisiones.docx")
          img_QR = InlineImage(doc, f"{file_name}.png", width=Mm(70))

          doc.render({"remision":remision_numero, "fecha": formatted_date, "cliente": nombre_cliente, "destino":destino, "producto": producto, "descripcion": producto_descripcion, "total": total_producto, "fletera": fletera, "conductor": conductor, "telefono": telefono_conductor, "fecha_embarque": fecha_embarque, "fecha_entrega": fecha_entrega, "marca_camion": marca_camion, "placas_tractor": placas_tractor, "placas_caja": placas_cajas, "modelo": modelo_camion, "color": color_camion, "numero_economico": numero_economico, "longitud": longitud_camion, "flete":costo_flete, "cuota_tonelada": cuota_tonelada, "peso":peso_carga,"precio": precio_carga, "codigo_alfa": codigo_alfa, "codigo_caat": codigo_caat, "img":img_QR})

          doc.save(f"remision_{remision_numero}.docx")

        except Exception as exc:
          messagebox.showerror("Error", f"Se ha producido un error al guardar la información: {exc}")

  #delete all the info from the entries
  def clear_entries():
    entry_remision_numero.delete(0, tk.END)
    entry_nombre_cliente.delete(0, tk.END)
    entry_destino.delete(0, tk.END)
    entry_producto.delete(0, tk.END)
    entry_producto_descripcion.delete("1.0", tk.END)
    entry_total_producto.delete(0, tk.END)
    entry_fletera.delete(0, tk.END)
    entry_conductor.delete(0, tk.END)
    entry_telefono_conductor.delete(0, tk.END)
    entry_fecha_embarque.delete(0, tk.END)
    entry_fecha_entrega.delete(0, tk.END)
    entry_marca_camion.delete(0, tk.END)
    entry_placas_tractor.delete(0, tk.END)
    entry_placas_cajas.delete(0, tk.END)
    entry_modelo_camion.delete(0, tk.END)
    entry_color_camion.delete(0, tk.END)
    entry_numero_economico.delete(0, tk.END)
    entry_longitud.delete(0, tk.END)
    entry_flete.delete(0, tk.END)
    entry_cuota_tonelada.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_codigo_alfa.delete(0, tk.END)
    entry_codigo_caat.delete(0, tk.END)
    entry_firma.delete(0, tk.END)
    entry_numero_bins.delete(0, tk.END)
    label_resultado_peso_display.config(text="")
    entry_file_name.delete(0, tk.END)
    entry_remision_numero.focus()

  #function to calculate the weigth in the bins and disply the result. 
  def onions_weigth_bins():
    try:
      bins = int(entry_numero_bins.get())
      weigth = calculate_weigth(bins, RANDOM_AVERAGE_ONIONS_WEIGTH)
      label_resultado_peso_display.config(text=f"{weigth:.2f}")
    
    except ValueError:
      label_resultado_peso_display.config(text="Error! Ingrese solo números!")
    
  submit_button.config(command=submit_info)
  calculate_button.config(command=onions_weigth_bins)

#create a QRcode Image. Chat GPT helps me
def qr_code(json, file_name):
  try: 
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction used for the QR code
        box_size=10,  # Controls how many pixels each “box” of the QR code is
        border=4,  # Controls how many boxes thick the border should be
    )

    # Add JSON data to the QR code
    qr.add_data(json)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='white', back_color='black')

    if file_name == "":
      file_name = "qr_code.png"
      img.save(file_name)
      # Save the image
    else:
      img.save(file_name + ".png")

    messagebox.showinfo("Exito", "Su Codigo QR a sido creado correctamente!")
    return img
  except Exception as exc:
    messagebox.showerror("Error", f"Se produjo un Error: {exc}")

if __name__ == "__main__":
  main()
