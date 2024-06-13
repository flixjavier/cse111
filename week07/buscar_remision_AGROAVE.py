import csv
import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, Entry, ttk
#import json

REMISION_DATA = "agroaveRemisiones.csv"
KEY_COLUMN_INDEX = 1
INDICES = [1,2,4,5,8,13,7]

def main():
  # Create the main window
  root = tk.Tk()
  frm_main = Frame(root)
  frm_main.master.title("Buscar AGROAVE")
  frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1) #this manage all the layout using frm_main

  #Size of window 
  #frm_main.master.geometry("1000x1000")

  #populate main Window
  populate_main_window(frm_main)

  root.mainloop()

def populate_main_window(frm_main):

  # get the dictionary
  remisiones_dict = read_dictionary(REMISION_DATA, KEY_COLUMN_INDEX)

  # Add a title inside the window
  title_label = Label(frm_main, text="Buscar Remisiones AGROAVE", font=("Helvetica", 24))

  #labels and entry widgets for bins calculator
  label_remision_number = Label(frm_main, text="Numero de remisión:")
  entry_remision_number = Entry(frm_main)

  label_remision = Label(frm_main, text="Remisión:")
  label_remision_display = Label(frm_main)

  #Display info
  columns = ["rem", "clt", "prod", "desc", "chf", "plac", "flet"]
  tree = ttk.Treeview(frm_main, columns= columns, show= "headings")
  tree.heading('rem',text='Remisión')
  tree.heading('clt',text='Cliente')
  tree.heading('prod',text='Producto')
  tree.heading('desc',text='Descripción')
  tree.heading('chf',text='Chofer')
  tree.heading('plac',text='Placas')
  tree.heading('flet',text='Fletera')

  #create search button
  buscar_button = Button(frm_main, text="Buscar")

  #create clear button
  borrar_button = Button(frm_main, text="Borrar")

  #layout 
  title_label.grid(               row=0, column=0, columnspan=4, pady=10)
  label_remision_number.grid(     row=1, column=0, padx=10, pady=5)
  entry_remision_number.grid(     row=1, column=1, padx=10, pady=5)
  label_remision.grid(            row=2, column=0, padx=10, pady=5)
  label_remision_display.grid(    row=2, column=1, padx=10, pady=50)
  label_remision_display.columnconfigure (1, weight=1)
  tree.grid(row=5, column=0,columnspan=6, padx=20, pady=10)

  buscar_button.grid(             row=3, column=0)
  borrar_button.grid(             row=3, column=1)

  # Function to print a specific key in JSON format
  """ def print_key_to_json():
    try:
      key = entry_remision_number.get()
      invoice_item = print_specific_values_from_key(remisiones_dict, key, INDICES)
      key_value_json = json.dumps({key: remisiones_dict[key]}, indent=4)
      label_remision_display.config(text=key_value_json)
      #return key_value_json
      tree.insert('',0, values=invoice_item)
    except Exception as exc:
      label_remision_display.config(text="REMISION NO ENCONTRADA") """
  
  # Function to print specific values from a dictionary  using a key
  def display_key():
    try:
      key_values_list = []
      key = entry_remision_number.get()
      if key in remisiones_dict:
        values = remisiones_dict[key]
        for index in INDICES:
          if index < len(values):
            key_values_list.append(values[index])
        label_remision_display.config(text=f'Remisión Encontrada: {key}')
        tree.insert('',0, values=key_values_list)
      else:
        label_remision_display.config(text="REMISIÓN NO ENCONTRADA")
      
    except Exception as exc:
      label_remision_display.config(text="REMISIÓN NO ENCONTRADA")  

  def clear_entries():
    entry_remision_number.delete(0, tk.END)
    label_remision_display.config(text="")
    entry_remision_number.focus()

  buscar_button.config(command=display_key)
  borrar_button.config(command=clear_entries)

def read_dictionary(filename, key_colum_index): 
  try:
    dictionay = {}
    with open(filename, 'rt') as csv_file:
      # Comment: 
      reader = csv.reader(csv_file)

      next(reader)

      for row_line in reader: 
        if len(row_line) != 0:
          key = row_line[key_colum_index]
          dictionay[key] = row_line
    # end open file
    return dictionay
  except Exception as e:
    messagebox.showerror("Error", f"Se ha producido un error: {e}")

# Function to print specific values from a dictionary key
def specific_values_from_key(dictionary, key, indices):
  key_values_list = []
  if key in dictionary:
      values = dictionary[key]
      for index in indices:
          if index < len(values):
              key_values_list.append(values[index])
          else:
              print(f"Index {index} is out of range for the values in '{key}'")
  else:
      print(f"Key '{key}' not found in the dictionary")
  return key_values_list

if __name__ == "__main__":
  main()