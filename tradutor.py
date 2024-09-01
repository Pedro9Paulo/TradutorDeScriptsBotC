from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
import os

def removeAcento(texto):
	texto = texto.replace("á", "a")
	texto = texto.replace("é", "e")
	texto = texto.replace("í", "i")
	texto = texto.replace("ó", "o")
	texto = texto.replace("ú", "u")
	texto = texto.replace("â", "a")
	texto = texto.replace("ê", "e")
	texto = texto.replace("î", "i")
	texto = texto.replace("ô", "o")
	texto = texto.replace("û", "u")
	texto = texto.replace("à", "a")
	texto = texto.replace("è", "e")
	texto = texto.replace("ì", "i")
	texto = texto.replace("ò", "o")
	texto = texto.replace("ù", "u")
	texto = texto.replace("ä", "a")
	texto = texto.replace("ë", "e")
	texto = texto.replace("ï", "i")
	texto = texto.replace("ö", "o")
	texto = texto.replace("ü", "u")
	texto = texto.replace("ã", "a")
	texto = texto.replace("õ", "o")
	texto = texto.replace("ç", "c")
	texto = texto.replace("ñ", "n")
	texto = texto.replace("ª", "a")
	texto = texto.replace("º", "o")
	texto = texto.replace("Á", "A")
	texto = texto.replace("É", "E")
	texto = texto.replace("Í", "I")
	texto = texto.replace("Ó", "O")
	texto = texto.replace("Ú", "U")
	texto = texto.replace("Â", "A")
	texto = texto.replace("Ê", "E")
	texto = texto.replace("Î", "I")
	texto = texto.replace("Ô", "O")
	texto = texto.replace("Û", "U")
	texto = texto.replace("À", "A")
	texto = texto.replace("È", "E")
	texto = texto.replace("Ì", "I")
	texto = texto.replace("Ò", "O")
	texto = texto.replace("Ù", "U")
	texto = texto.replace("Ä", "A")
	texto = texto.replace("Ë", "E")
	texto = texto.replace("Ï", "I")
	texto = texto.replace("Ö", "O")
	texto = texto.replace("Ü", "U")
	texto = texto.replace("Ã", "A")
	texto = texto.replace("Õ", "O")
	texto = texto.replace("Ç", "C")
	texto = texto.replace("Ñ", "N")
	return texto
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
	cenario_string = None
	arquivo_ref = open(resource_path("ptbr/all.json"), encoding="utf-8")
	todosRaw = arquivo_ref.read()
	todosList = todosRaw[2:-2].split(",\n  {")
	for i in range(1,len(todosList)):
		todosList[i] = "  {"+todosList[i]
	todos = {}
	for p in todosList:
		idi = p.find("_br")
		todos[p[15:idi]] = p
		arquivo_ref.close()
	try:
		filename = cenario_ingles.get()
		arquivo = open(filename)
		script = json.load(arquivo)
		cenario = "[\n"
		for p in script:
			if type(p) == type({}):
				if p["id"] == "_meta":
					cenario += "{"
					for item in p:
						if type(p[item]) == type(True):
							cenario += '"' + item + '": ' + str(p[item]).lower() + ', '
						else:
							cenario += '"' + item + '": "' + p[item] + '", ' 
					cenario = cenario[:-2] + "},\n"
				else:
					cenario += todos[p["id"].replace("_", "")] +",\n"
			else:
				cenario += todos[p.replace("_", "")] +",\n"
		cenario_traduzido.set("Script Traduzido com Sucesso")
		cenario_string = removeAcento(cenario)
	except Exception as erro:
		cenario_traduzido.set(erro)
	arquivo.close()
	filenamePortugues = filedialog.asksaveasfilename(defaultextension=".json", initialfile=filename[filename.rindex('/')+1:])
	f = open(filenamePortugues, "w", encoding="utf-8")
	f.write(cenario_string[:-2]+"\n]")
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

ttk.Button(mainframe, text="Traduzir", command=tradutor).grid(column=3, row=2, sticky=W)

root.bind("<Return>", tradutor)

root.mainloop()
