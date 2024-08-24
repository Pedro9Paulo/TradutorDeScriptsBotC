import json
import os
f = open("ptbr/all.json", encoding="utf-8")
todosRaw = f.read()
todosList = todosRaw[2:-2].split(",\n  {")
for i in range(1,len(todosList)):
	todosList[i] = "  {"+todosList[i]
todos = {}
for p in todosList:
	idi = p.find("_br")
	todos[p[15:idi]] = p
name = input("Insira o nome do arquivo que você quer traduzir\n")
f = open(name+".json")
try:
	script = json.load(f)
	f.close()
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
except Exception as erro:
	print("O script " + name + " tem o defeito: " + str(erro))

f = open(name+"_br", "w", encoding="utf-8")
f.write(cenario[:-2]+"\n]")
f.close()
