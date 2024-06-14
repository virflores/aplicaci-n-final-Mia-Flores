import tkinter as tk
from tkinter import ttk
 
 #aplicacion
exchange_rates = {
    "USD": 1,
    "ARG": 900,
    "BRL": 5,
    "EUR": 0.95,
    "GBP": 0.72, #libra esterlina 
    "JPY": 109.61, #yen japones
    "AUD": 1.32, #dolar australiano
    "CAD": 1.23, #dolar canadiense 
    "CHF": 0.92, #franco suizo
    "CNY": 6.35, #yuan
    "HKD": 7.76, #dolar de hong kong
}
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            result_label.config(text="Error: Moneda no válida")
            return

        from_rate = exchange_rates[from_currency]
        to_rate = exchange_rates[to_currency]
        converted_amount = (amount / from_rate) * to_rate

        result_label.config(text=f"Resultado: {round(converted_amount, 2)}")
    except ValueError:
        result_label.config(text="Error: Ingrese un valor numérico válido")


#diseño de la aplicacion 
root = tk.Tk()
root.title("Conversor de Moneda")

amount_label = ttk.Label(root, text="Cantidad:")
amount_entry = ttk.Entry(root)

from_currency_label = ttk.Label(root, text="De:")
from_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
from_currency_combobox.current(0)

to_currency_label = ttk.Label(root, text="A:")
to_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
to_currency_combobox.current(1)

convert_button = ttk.Button(root, text="Convertir", command=convert_currency)

result_label = ttk.Label(root, text="")

amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

to_currency_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()