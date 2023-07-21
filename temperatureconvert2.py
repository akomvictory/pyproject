import tkinter as tk

def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_label.config(text=f"Fahrenheit: {fahrenheit:.2f}")

def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5/9
    celsius_label.config(text=f"Celsius: {celsius:.2f}")

root = tk.Tk()
root.title("Temperature Converter")

celsius_label = tk.Label(root, text="Enter Celsius:")
celsius_label.pack()

celsius_entry = tk.Entry(root)
celsius_entry.pack()

celsius_entry.bind("<Return>", lambda event: celsius_to_fahrenheit())

fahrenheit_label = tk.Label(root, text="")
fahrenheit_label.pack()

fahrenheit_label = tk.Label(root, text="Enter Fahrenheit:")
fahrenheit_label.pack()

fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.pack()

fahrenheit_entry.bind("<Return>", lambda event: fahrenheit_to_celsius())

celsius_label = tk.Label(root, text="")
celsius_label.pack()

root.mainloop()
