import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid temperature in Celsius.")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit:.2f} Fahrenheit = {celsius:.2f} Celsius")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid temperature in Fahrenheit.")

def on_celsius_entry_return(event):
    celsius_to_fahrenheit()

def on_fahrenheit_entry_return(event):
    fahrenheit_to_celsius()

root = tk.Tk()
root.title("Temperature Converter")

celsius_label = tk.Label(root, text="Celsius:")
celsius_label.pack()

celsius_entry = tk.Entry(root)
celsius_entry.pack()
celsius_entry.bind("<Return>", on_celsius_entry_return)

fahrenheit_label = tk.Label(root, text="Fahrenheit:")
fahrenheit_label.pack()

fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.pack()
fahrenheit_entry.bind("<Return>", on_fahrenheit_entry_return)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
