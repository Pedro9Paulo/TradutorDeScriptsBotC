import json
import os

def getTodos(f):
	todosRaw = f.read()
	todosList = todosRaw[2:-3].split(",\n  {")
	for i in range(1,len(todosList)):
		todosList[i] = "  {"+todosList[i]
	todos = {}
	for p in todosList:
		idi = p.find("_br")
		todos[p[15:idi]] = p
	f.close()
	return todos

def montaJson(f, todos):
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
		cenario = cenario[:-2]+"\n]"
		return cenario
	except Exception as erro:
		return erro
