from tkinter import *

# okno
window = Tk()
window.title("Převod měn z CZK na Eura")
window.minsize(200,200)
window.resizable(False,False)
window.config(bg="#061856")
window.iconbitmap("icons/icon2.ico")

# 1 euro = 24,58
# funkce
def count_currency():
    amount_eur = float(amount_input.get()) / 24.58
    result_label["text"] = round(amount_eur, 2)

# vstup od uživatele
amount_input = Entry(width=10, font=("Helvetica",15))
amount_input.grid(row=0,column=0, padx=10, pady=10)

# label
czk_label = Label(text="CZK", font=("Helvetica", 15), bg="#061856", fg="white")
czk_label.grid(row=0, column=1)

result_label = Label(text="0", font=("Helvetica", 15), bg="#061856", fg="white")
result_label.grid(row=1, column=0)

eur_label = Label(text="Eura", font=("Helvetica", 15), bg="#061856", fg="white")
eur_label.grid(row=1, column=1)

# tlačítko
count_button = Button(text="Převést", font=("Helvetica", 15), command=count_currency)
count_button.grid(row=0, column=2, padx=10, pady=10)


# hlavní cyklus
window.mainloop()