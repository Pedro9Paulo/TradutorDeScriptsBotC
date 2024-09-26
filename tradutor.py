import json
import os

# Função que lê o arquivo "f" com todos os papéis traduzidas e devolve um dicionário com as personagem indexado pelo id
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

# Função que a partir de um Json em inglês "f" e do dicionário com todos os papéis traduzidos "todos" monta um Json traduzido
def montaJson(f, todos):
	try:
		script = json.load(f)
		f.close()
		cenario = "[\n"
		for p in script:
			if type(p) == type({}):
				# Copia o meta (nome, autor, etc...) do script sem mudar nada
				if p["id"] == "_meta":
					cenario += "{"
					for item in p:
						if type(p[item]) == type(True):
							cenario += '"' + item + '": ' + str(p[item]).lower() + ', '
						else:
							cenario += '"' + item + '": "' + p[item] + '", ' 
					cenario = cenario[:-2] + "},\n"
				else:
					# Pega o id do Json no formato antigo
					cenario += todos[p["id"].replace("_", "")] +",\n"
			else:
				# Pega o id fo Json no formato novo
				cenario += todos[p.replace("_", "")] +",\n"
		cenario = cenario[:-2]+"\n]"
		return cenario
	except Exception as erro:
		return erro
