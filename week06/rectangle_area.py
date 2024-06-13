import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("The Area of a Rectangle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "height"
    lbl_height = Label(frm_main, text="Height:")

    # Create an integer entry box where the user will enter the height.
    ent_height = FloatEntry(frm_main, width=4,lower_bound=0, upper_bound=1000)

    # Create a label that displays "Inches"
    lbl_height_units = Label(frm_main, text="Inches")

    # Create a label that displays "Width:"
    lbl_width = Label(frm_main, text="Width:")
    ent_width = FloatEntry(frm_main, width=4, lower_bound=0, upper_bound=1000)
    lbl_width_units = Label(frm_main, text="Inches")

    # Create labels that will display the results.
    lbl_area = Label(frm_main, text="Area:")
    lbl_rectangle_area= Label(frm_main, width=3)
    lbl_area_units = Label(frm_main, text="Inches^2")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")
    #btn_enter = Button(frm_main, text="Enter")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_height.grid(      row=0, column=0, padx=3, pady=3, sticky="w")
    ent_height.grid(      row=0, column=2, padx=3, pady=3, sticky="w")
    lbl_height_units.grid(row=0, column=3, padx=0, pady=3, sticky="w")

    lbl_width.grid(      row=1, column=0, padx=3, pady=3, sticky="w")
    ent_width.grid(      row=1, column=2, padx=3, pady=3, sticky="w")
    lbl_width_units.grid(row=1, column=3, padx=0, pady=3, sticky="w")
    lbl_area.grid(row=2, column=0, padx=3, pady=3, sticky="w")
    lbl_rectangle_area.grid( row=2, column=1, padx=3, pady=3, sticky="w")
    lbl_area_units.grid(row=2, column=3, padx=0, pady=3, sticky="w")
    
    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=4, sticky="w")
    #btn_enter.grid(row=3, column=3, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's rectangle area.
        """
        try:
            # Get the user's age.
            height = ent_height.get()
            width = ent_width.get()

            # Compute the user's maximum heart rate.
            area = height * width

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            lbl_rectangle_area.config(text=f"{area:.0f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_rectangle_area.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_height.clear()
        ent_width.clear()
        lbl_rectangle_area.config(text="")
        ent_height.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_height.bind("<KeyRelease>", calculate)
    ent_width.bind("<KeyRelease>", calculate)



    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)
    #btn_enter.config(command=calculate())

    # Give the keyboard focus to the age entry box.
    ent_height.focus()

if __name__ == '__main__':
  main()
