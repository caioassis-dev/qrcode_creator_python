import tkinter as tk
from tkinter import messagebox
import pyqrcode
import png

def create_qr_code():
    nomeQRCODE = nome_qrcode_entry.get()
    url = url_entry.get()
    if url:
        qr_code = pyqrcode.create(url)
        qr_code.png(f'qr_code_{nomeQRCODE}.png', scale=8)
        messagebox.showinfo("QR Code Generator", "QR code criado com sucesso!")
    else:
        messagebox.showerror("QR Code Generator", "Por favor entre com a URL.")

root = tk.Tk()

root.title("QR Code Generator")

# Label para digitar o site
url_label = tk.Label(root, text="Digite o site que você deseja criar o QRCODE:")
url_label.pack(padx=10, pady=5)

# Campo para digitar a URL
url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10, pady=5)

# Label para digitar o nome do QR Code
nome_qrcode = tk.Label(root, text="Qual nome que você deseja para o QRCODE?")
nome_qrcode.pack(padx=10, pady=5)

# Campo para digitar o nome do QR Code
nome_qrcode_entry = tk.Entry(root, width=50)
nome_qrcode_entry.pack(padx=10, pady=5)

# Botão para criar o QR Code
generate_button = tk.Button(root, text="Criar QR Code", command=create_qr_code)
generate_button.pack(padx=10, pady=20)

root.mainloop()