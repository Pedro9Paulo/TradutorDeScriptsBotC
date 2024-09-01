from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def findFile(*args):
	filename = filedialog.askopenfilename()
	cenario_ingles.set(filename)

def tradutor(*args):
	filename = cenario_ingles.get()
	arquivo_raw = open(filename, "r", encoding="utf-8")
	arquivo = arquivo_raw.read()
	arquivo = arquivo.replace("á", "a")
	arquivo = arquivo.replace("é", "e")
	arquivo = arquivo.replace("í", "i")
	arquivo = arquivo.replace("ó", "o")
	arquivo = arquivo.replace("ú", "u")
	arquivo = arquivo.replace("â", "a")
	arquivo = arquivo.replace("ê", "e")
	arquivo = arquivo.replace("î", "i")
	arquivo = arquivo.replace("ô", "o")
	arquivo = arquivo.replace("û", "u")
	arquivo = arquivo.replace("à", "a")
	arquivo = arquivo.replace("è", "e")
	arquivo = arquivo.replace("ì", "i")
	arquivo = arquivo.replace("ò", "o")
	arquivo = arquivo.replace("ù", "u")
	arquivo = arquivo.replace("ã", "a")
	arquivo = arquivo.replace("õ", "o")
	arquivo = arquivo.replace("ç", "c")
	arquivo = arquivo.replace("ñ", "n")
	arquivo = arquivo.replace("ª", "a")
	arquivo = arquivo.replace("º", "o")
	arquivo = arquivo.replace("Á", "A")
	arquivo = arquivo.replace("É", "E")
	arquivo = arquivo.replace("Í", "I")
	arquivo = arquivo.replace("Ó", "O")
	arquivo = arquivo.replace("Ú", "U")
	arquivo = arquivo.replace("Â", "A")
	arquivo = arquivo.replace("Ê", "E")
	arquivo = arquivo.replace("Î", "I")
	arquivo = arquivo.replace("Ô", "O")
	arquivo = arquivo.replace("Û", "U")
	arquivo = arquivo.replace("À", "A")
	arquivo = arquivo.replace("È", "E")
	arquivo = arquivo.replace("Ì", "I")
	arquivo = arquivo.replace("Ò", "O")
	arquivo = arquivo.replace("Ù", "U")
	arquivo = arquivo.replace("Ã", "A")
	arquivo = arquivo.replace("Õ", "O")
	arquivo = arquivo.replace("Ç", "C")
	arquivo = arquivo.replace("Ñ", "N")
	arquivo_raw.close()
	cenario_traduzido.set("Pronto")
	filenamePortugues = filedialog.asksaveasfilename(defaultextension=".json", initialfile=filename[filename.rindex('/')+1:])
	f = open(filenamePortugues, "w", encoding="utf-8")
	f.write(arquivo)
	f.close()
		

root = Tk()
root.title("Tradutor de Cenários")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Selecione o Cenário que deseja traduzir:").grid(column=1, row=1, sticky=W)

cenario_ingles = StringVar()
cenario_ingles_entry = ttk.Entry(mainframe, width=64, textvariable=cenario_ingles)
cenario_ingles_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Procure", command=findFile).grid(column=3, row=1, sticky=W)

cenario_traduzido = StringVar()
ttk.Label(mainframe, textvariable=cenario_traduzido).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Remover Acentos", command=tradutor).grid(column=3, row=2, sticky=W)

root.bind("<Return>", tradutor)

root.mainloop()
