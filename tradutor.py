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
		cenario_string = cenario
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
