import tkinter as tk
from tkinter import IntVar

def calculate_tax(income, filing_status):
    if filing_status == 1:  # Single option
        tax_rate = 0.2
    elif filing_status == 2:  # Married option
        tax_rate = 0.15
    elif filing_status == 3:  # Divorced option
        tax_rate = 0.1
    else:  # Default to Single option
        tax_rate = 0.2

    tax_amount = income * tax_rate
    return tax_amount

def calculate_button_clicked():
    income = float(income_entry.get())
    filing_status = filing_status_var.get()
    tax_amount = calculate_tax(income, filing_status)
    result_label.config(text=f"Tax amount: ${tax_amount:.2f}")

root = tk.Tk()
root.title("Tax Calculator")

income_label = tk.Label(root, text="Enter your income:")
income_label.pack()

income_entry = tk.Entry(root)
income_entry.pack()

filing_status_label = tk.Label(root, text="Select your filing status:")
filing_status_label.pack()

filing_status_var = IntVar()
filing_status_var.set(1)  # Default to Single option

single_radio = tk.Radiobutton(root, text="Single", variable=filing_status_var, value=1)
married_radio = tk.Radiobutton(root, text="Married", variable=filing_status_var, value=2)
divorced_radio = tk.Radiobutton(root, text="Divorced", variable=filing_status_var, value=3)

single_radio.pack()
married_radio.pack()
divorced_radio.pack()

calculate_button = tk.Button(root, text="Calculate Tax", command=calculate_button_clicked)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
